# social_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tweet, UserProfile, Follow, Like, Retweet, Thread
from .forms import TweetForm

# nexus/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tweet, UserProfile, Follow, TrendingScore, TweetTopic
from django.db.models import Count
from django.db.models import OuterRef, Exists

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count, Exists, OuterRef
from .models import UserProfile, Tweet, Like, Retweet, Follow, TweetTopic

@login_required
def home(request):
    # Determine the feed type: 'for_you' or 'following'
    feed_type = request.GET.get('feed', 'for_you')
    
    # Ensure user_profile exists
    user_profile, created = UserProfile.objects.get_or_create(registration=request.user.registration)
    
    # Fetch users followed by the current user
    followed_users = Follow.objects.filter(follower=user_profile).values_list('follows_user', flat=True)
    
    if feed_type == 'following':
        # Fetch tweets, retweets, and replies from followed users
        tweets = Tweet.objects.filter(
            Q(registration__in=followed_users) |
            Q(parent_tweet__registration__in=followed_users) |
            Q(replies__registration__in=followed_users)
        ).annotate(
            is_liked=Exists(
                Like.objects.filter(tweet=OuterRef('pk'), registration=request.user.registration)
            ),
            is_retweeted=Exists(
                Retweet.objects.filter(tweet=OuterRef('pk'), registration=request.user.registration)
            )
        ).order_by('-created_at')[:50]
    else:
        # For You feed: could be all tweets or based on some algorithm
        tweets = Tweet.objects.annotate(
            is_liked=Exists(
                Like.objects.filter(tweet=OuterRef('pk'), registration=request.user.registration)
            ),
            is_retweeted=Exists(
                Retweet.objects.filter(tweet=OuterRef('pk'), registration=request.user.registration)
            )
        ).order_by('-created_at')[:50]

    # Prepare retweets with comments for each tweet
    retweets_with_comments = {
        tweet.id: Retweet.objects.filter(tweet=tweet, comment__isnull=False) for tweet in tweets
    }

    # Suggested users to follow
    suggested_users = UserProfile.objects.exclude(
        registration__in=followed_users
    ).exclude(
        registration=request.user.registration
    ).annotate(
        followers_count=Count('followers')
    ).order_by('-followers_count')[:5]

    # Fetch trending topics based on trending scores
    trending_topics = TweetTopic.objects.annotate(
        tweet_count=Count('tweet')
    ).order_by('-tweet_count')[:10]

    context = {
        'tweets': tweets,
        'feed_type': feed_type,
        'suggested_users': suggested_users,
        'retweets_with_comments': retweets_with_comments,
        'trending_topics': trending_topics
    }
    return render(request, 'nexus/nexus_home.html', context)


# nexus/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Tweet, Follow

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Tweet, Like, Retweet

from django.db.models import Q

@login_required
def profile_view(request, username):
    # Fetch the user profile being viewed
    user_profile = get_object_or_404(UserProfile, registration__user__username=username)
    current_user_profile, _ = UserProfile.objects.get_or_create(registration=request.user.registration)

    # Check if the current user is following the profile being viewed
    is_following = Follow.objects.filter(follower=current_user_profile, follows_user=user_profile).exists()

    # Tweets by the user (excluding replies and retweets)
    tweets = Tweet.objects.filter(
        registration=user_profile.registration,
        parent_tweet__isnull=True  # Exclude replies
    ).order_by('-created_at')

    # Replies by the user (tweets that are replies to others)
    replies = Tweet.objects.filter(
        registration=user_profile.registration,
        parent_tweet__isnull=False  # Only include replies
    ).order_by('-created_at')

    # Retweets by the user (fetching from the Retweet model)
    retweets = Retweet.objects.filter(
        registration=user_profile.registration
    ).select_related('tweet').order_by('-created_at')

    # Media tweets (tweets by the user with a non-empty media URL)
    media_tweets = tweets.exclude(media_url='').order_by('-created_at')

    # Liked tweets (only if the profile belongs to the logged-in user)
    liked_tweets = []
    if user_profile.registration == request.user.registration:
        liked_tweets = Tweet.objects.filter(
            like__registration=request.user.registration
        ).order_by('-created_at').distinct()

    # Combine replies and retweets for the replies tab
    replies_and_retweets = sorted(
        list(replies) + list(retweets),
        key=lambda x: x.created_at if isinstance(x, Tweet) else x.created_at,
        reverse=True
    )

    context = {
        'user_profile': user_profile,
        'tweets': tweets,
        'replies_and_retweets': replies_and_retweets,  # Merged data for replies tab
        'media_tweets': media_tweets,
        'liked_tweets': liked_tweets,
        'is_following': is_following,
    }
    return render(request, 'nexus/nexus_profile.html', context)



@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(UserProfile, registration__user__username=username)
    Follow.objects.get_or_create(follower=request.user.registration.userprofile, follows_user=user_to_follow.registration)
    return redirect('profile', username=username)

@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(UserProfile, registration__user__username=username)
    Follow.objects.filter(follower=request.user.registration.userprofile, follows_user=user_to_unfollow.registration).delete()
    return redirect('profile', username=username)
from django.http import JsonResponse

@login_required
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    tweet.likes_count += 1
    tweet.save()
    return JsonResponse({'success': True, 'likes_count': tweet.likes_count})

@login_required
def retweet(request, tweet_id):
    original_tweet = get_object_or_404(Tweet, id=tweet_id)
    print("function called")
    Tweet.objects.create(
        registration=request.user.registration,
        content=original_tweet.content,
        parent_tweet=original_tweet
    )
    return redirect('home')
@login_required
def trending_topics(request):
    trending_topics = TweetTopic.objects.annotate(tweet_count=Count('tweet')).order_by('-tweet_count')[:10]
    context = {'trending_topics': trending_topics}
    return render(request, 'nexus/trending_topics.html', context)
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tweet

@login_required
def tweet_detail(request, tweet_id):
    # Fetch the main tweet
    tweet = get_object_or_404(Tweet, id=tweet_id)
    
    # Fetch replies to create a threaded view
    replies = tweet.get_thread()  # Uses the `get_thread` method defined in the Tweet model
    
    context = {
        'tweet': tweet,
        'replies': replies,
    }
    return render(request, 'nexus/tweet_detail.html', context)
@login_required
def suggested_users(request):
    # Get the list of users the current user is already following
    followed_users = Follow.objects.filter(
        follower__registration=request.user.registration
    ).values_list('follows_user', flat=True)

    # Find popular users that the current user is not following
    suggested_users = UserProfile.objects.exclude(
        registration__in=followed_users
    ).exclude(
        registration=request.user.registration  # Exclude the current user
    ).annotate(
        followers_count=Count('follower')  # Count followers to get popular users
    ).order_by('-followers_count')[:10]  # Limit the results

    context = {
        'suggested_users': suggested_users,
    }
    return render(request, 'nexus/suggested_users.html', context)

# nexus/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tweet, TweetTopic

@login_required
def topic_detail(request, topic_id):
    # Get the topic by ID
    topic = get_object_or_404(TweetTopic, id=topic_id)
    
    # Fetch all tweets associated with this topic
    tweets = Tweet.objects.filter(topics=topic).order_by('-created_at')
    
    context = {
        'topic': topic,
        'tweets': tweets,
    }
    return render(request, 'nexus/topic_detail.html', context)
# nexus/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ActivityLog

@login_required
def notifications_view(request):
    # Fetch notifications related to the logged-in user
    notifications = ActivityLog.objects.filter(registration=request.user.registration).order_by('-timestamp')
    
    context = {
        'notifications': notifications,
    }
    return render(request, 'nexus/notifications.html', context)
# nexus/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserSettings
from .forms import SettingsForm

@login_required
def settings_view(request):
    # Get or create user settings
    user_settings, created = UserSettings.objects.get_or_create(registration=request.user.registration)

    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=user_settings)
        if form.is_valid():
            form.save()
            return redirect('settings')  # Redirect back to settings page after saving
    else:
        form = SettingsForm(instance=user_settings)

    context = {
        'form': form,
    }
    return render(request, 'nexus/settings.html', context)
# nexus/views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tweet, Like
from django.views.decorators.csrf import ensure_csrf_cookie

from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.csrf import csrf_protect

@csrf_protect
@login_required
def ajax_like(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    liked = Like.objects.filter(tweet=tweet, registration=request.user.registration).exists()

    if not liked:
        Like.objects.create(tweet=tweet, registration=request.user.registration)
        tweet.likes_count += 1
        tweet.save()
    else:
        Like.objects.filter(tweet=tweet, registration=request.user.registration).delete()
        tweet.likes_count -= 1
        tweet.save()

    return JsonResponse({
        'success': True,
        'likes_count': tweet.likes_count,
        'liked': not liked
    })

import json
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

@csrf_protect
@login_required
def ajax_retweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    retweeted = Retweet.objects.filter(tweet=tweet, registration=request.user.registration).exists()

    # Parse the JSON data from the request body
    data = json.loads(request.body)
    comment = data.get('comment',"")  # Get the optional comment

    if not retweeted:
        Retweet.objects.create(tweet=tweet, registration=request.user.registration, comment=comment)
        tweet.retweets_count += 1
        tweet.save()
    else:
        # If already retweeted, remove the retweet (like undo retweet)
        Retweet.objects.filter(tweet=tweet, registration=request.user.registration).delete()
        tweet.retweets_count -= 1
        tweet.save()

    return JsonResponse({
        'success': True,
        'retweets_count': tweet.retweets_count,
        'retweeted': not retweeted,
        'comment':comment,
    })
# nexus/views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Follow

from django.db.models import Count

@login_required
def ajax_follow(request, username):
    target_user_profile = get_object_or_404(UserProfile, registration__user__username=username)
    user_profile = request.user.registration.userprofile  # Current user's profile
    
    # Check if the user is already followed
    is_following = Follow.objects.filter(follower=user_profile, follows_user=target_user_profile).exists()

    if not is_following:
        # Create a new follow record
        Follow.objects.create(follower=user_profile, follows_user=target_user_profile)
    else:
        # If already followed, remove the follow record
        Follow.objects.filter(follower=user_profile, follows_user=target_user_profile).delete()

    # Updated follower and following counts
    followers_count = Follow.objects.filter(follows_user=target_user_profile).count()
    following_count = Follow.objects.filter(follower=user_profile).count()

    return JsonResponse({
        'success': True,
        'is_following': not is_following,  # Indicates if the user is followed after this request
        'followers_count': followers_count,
        'following_count': following_count,
    })

from django.shortcuts import render, get_object_or_404
from .models import UserProfile, Follow

@login_required
def followers_list(request, username):
    # Get the profile of the user whose followers are being viewed
    user_profile = get_object_or_404(UserProfile, registration__user__username=username)
    followers = Follow.objects.filter(follows_user=user_profile).select_related('follower')

    context = {
        'user_profile': user_profile,
        'followers': [follow.follower for follow in followers],
    }
    return render(request, 'nexus/followers_list.html', context)


@login_required
def following_list(request, username):
    # Get the profile of the user whose following list is being viewed
    user_profile = get_object_or_404(UserProfile, registration__user__username=username)
    following = Follow.objects.filter(follower=user_profile).select_related('follows_user')

    context = {
        'user_profile': user_profile,
        'following': [follow.follows_user for follow in following],
    }
    return render(request, 'nexus/following_list.html', context)
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet
import re
@login_required
def post_tweet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        print(content)
        media_file = request.FILES.get('media_file')

        if content:
            # Create the tweet
            tweet = Tweet.objects.create(
                registration=request.user.registration,
                content=content,
                media_file=media_file  # Save the uploaded file
            )
            print(tweet)

            # Extract hashtags from the content
            hashtags = re.findall(r'#(\S+)', content)
            for tag in hashtags:
                # Get or create the topic
                topic, created = TweetTopic.objects.get_or_create(name=tag.lower())
                # Associate the topic with the tweet
                tweet.topics.add(topic)

        return redirect('nexus_home') # Replace 'home' with your home feed URL name
@login_required
def post_comment(request, tweet_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        parent_tweet = get_object_or_404(Tweet, id=tweet_id)
        print(content)
        if content:
            Tweet.objects.create(
                registration=request.user.registration,
                content=content,
                parent_tweet=parent_tweet
            )
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Content cannot be empty.'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'})
    
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

@login_required
def unretweet(request, tweet_id):
    if request.method == "POST":
        retweet = get_object_or_404(Tweet, id=tweet_id, registration=request.user.registration, parent_tweet__isnull=False)
        parent_tweet_id = retweet.parent_tweet.id  # Get the original tweet ID
        retweet.delete()
        return JsonResponse({"success": True, "remove_from_feed": True, "parent_tweet_id": parent_tweet_id})
    return JsonResponse({"success": False, "error": "Invalid request"})
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from champion.models import Registration  
from django.conf import settings
import uuid


### USER-RELATED MODELS ###

class UserProfile(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE)
    badges = models.ManyToManyField('Badge', blank=True)
    engagement_score = models.FloatField(default=0)
    is_suspended = models.BooleanField(default=False)
    strike_count = models.PositiveIntegerField(default=0)  # Track repeated violations
    last_active = models.DateTimeField(default=timezone.now)  # For active user tracking

    def __str__(self):
        return f"{self.registration.user.username}"


class Badge(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.ImageField(upload_to='badges/')

    def __str__(self):
        return self.name


class UserSettings(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE)
    email_notifications = models.BooleanField(default=True)
    push_notifications = models.BooleanField(default=True)
    privacy_public = models.BooleanField(default=True)
    is_2fa_enabled = models.BooleanField(default=False)
    two_fa_method = models.CharField(max_length=10, choices=[('SMS', 'SMS'), ('Email', 'Email')])
    notification_preferences = models.JSONField(default=dict)  # Store preferences for different notification types

    def __str__(self):
        return f"Settings for {self.registration.user.username}"


### TWEET, THREADING, AND ENGAGEMENT MODELS ###

class Tweet(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    media_url = models.URLField(blank=True, null=True)
    media_file = models.FileField(upload_to='media_files/', blank=True, null=True)
    parent_tweet = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    likes_count = models.PositiveIntegerField(default=0)
    retweets_count = models.PositiveIntegerField(default=0)
    reply_count = models.PositiveIntegerField(default=0)
    trending_score = models.FloatField(default=0)  # For calculating tweet trends
    is_flagged = models.BooleanField(default=False)
    moderation_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Removed', 'Removed')], default='Pending')
    flagged_reason = models.CharField(max_length=100, blank=True, null=True)
    is_trending = models.BooleanField(default=False)
    engagement_score = models.FloatField(default=0)
    topics = models.ManyToManyField('TweetTopic', blank=True)
    forwards_count = models.PositiveIntegerField(default=0)

    class Meta:
        indexes = [models.Index(fields=['created_at']), models.Index(fields=['parent_tweet']), models.Index(fields=['likes_count'])]

    def __str__(self):
        return f"Tweet by {self.registration.user.username}: {self.content[:20]}"

    def get_thread(self):
        """ Returns a queryset of all replies to this tweet, recursively (i.e., a full thread) """
        return Tweet.objects.filter(parent_tweet=self).order_by('created_at')


class Retweet(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)  # The user retweeting
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)  # Optional comment field
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.registration.user.username} retweeted"


class Like(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Like by {self.registration.user.username}"


class SavedTweet(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.registration.user.username} saved Tweet {self.tweet.id}"


class TweetTopic(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


### THREADING AND CONVERSATION MANAGEMENT ###

class Thread(models.Model):
    original_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='thread_root')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Thread for Tweet {self.original_tweet.id}"

    def get_all_replies(self):
        """ Retrieve all replies recursively for the thread, creating a full thread view. """
        return Tweet.objects.filter(parent_tweet=self.original_tweet).order_by('created_at')


### CONTENT ENGAGEMENT AND ANALYTICS ###

class ContentView(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    view_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.registration.user.username} viewed Tweet {self.tweet.id}"


class Analytics(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    tweet_views = models.PositiveIntegerField(default=0)
    tweet_likes = models.PositiveIntegerField(default=0)
    tweet_retweets = models.PositiveIntegerField(default=0)
    profile_views = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Analytics for {self.registration.user.username}"


class TrendingScore(models.Model):
    tweet = models.OneToOneField(Tweet, on_delete=models.CASCADE)
    trending_score = models.FloatField(default=0)
    last_calculated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Trending Score for Tweet {self.tweet.id}"


### FOLLOWING, MUTE, AND BLOCK FUNCTIONALITY ###

# nexus/models.py

from django.db import models
from django.contrib.auth.models import User

class Follow(models.Model):
    follower = models.ForeignKey('UserProfile', related_name='following', on_delete=models.CASCADE)  # User who follows
    follows_user = models.ForeignKey('UserProfile', related_name='followers', on_delete=models.CASCADE)  # User being followed
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.follower} follows {self.follows_user}"



class Mute(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='muter')
    muted_user = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='muted')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.registration.user.username} muted {self.muted_user.user.username}"


class Block(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='blocker')
    blocked_user = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='blocked')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.registration.user.username} blocked {self.blocked_user.user.username}"


### MODERATION AND REPORTING ###

class Report(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    reporter = models.ForeignKey(Registration, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Reviewed', 'Reviewed'), ('Resolved', 'Resolved')], default='Pending')
    is_verified = models.BooleanField(default=False)  # Track verified reports for suspension logic

    def __str__(self):
        return f"Report on Tweet {self.tweet.id} by {self.reporter.user.username}"


class ActivityLog(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return f"Activity by {self.registration.user.username}: {self.action}"


### ADVERTISEMENT AND SUBSCRIPTION MODELS ###

class Advertisement(models.Model):
    ad_text = models.CharField(max_length=280)
    media_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    advertiser = models.ForeignKey(Registration, on_delete=models.CASCADE)
    clicks = models.PositiveIntegerField(default=0)
    impressions = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Ad by {self.advertiser.user.username}"


class Subscription(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    plan = models.ForeignKey('SubscriptionPlan', on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50)
    features = models.ManyToManyField('SubscriptionFeature')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    trial_period_days = models.PositiveIntegerField(default=0)  # Optional trial period

    def __str__(self):
        return self.name


class SubscriptionFeature(models.Model):
    feature_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.feature_name


class PinnedTweet(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    pinned_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Pinned tweet by {self.registration.user.username}"

from django.db import models
from django.conf import settings
from django.utils import timezone

class Notification(models.Model):
    """Stores a single notification for a user."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="notifications"
    )
    target_tweet = models.ForeignKey(
        "Tweet",  # or wherever your Tweet model is
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="notifications"
    )
    message = models.TextField()  # or 'description'
    timestamp = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    message = models.TextField()
    # If you want to link to a tweet, a comment, or some other object:
    # e.g. tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=True, blank=True)

    timestamp = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:30]}"
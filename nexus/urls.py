# social_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='nexus_home'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/<str:username>/follow/', views.follow_user, name='follow_user'),
    path('profile/<str:username>/unfollow/', views.unfollow_user, name='unfollow_user'),

    # Tweet Details and Actions
    path('tweet/<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),
    path('tweet/<int:tweet_id>/like/', views.like_tweet, name='like_tweet'),
    path('tweet/<int:tweet_id>/retweet/', views.retweet, name='retweet'),
    path('unretweet/<int:tweet_id>/', views.unretweet, name='unretweet'),

    # Suggested Users to Follow
    path('suggested/', views.suggested_users, name='suggested_users'),

    # Trending Topics
    path('trending/', views.trending_topics, name='trending_topics'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),

    # Notifications and Settings
    path('notifications/', views.notifications_view, name='notifications'),
    path('settings/', views.settings_view, name='settings'),
    path('profile/<str:username>/followers/', views.followers_list, name='followers_list'),
    path('profile/<str:username>/following/', views.following_list, name='following_list'),
    # AJAX Routes for Dynamic Interactions (optional for async actions)
    path('ajax/like/<int:tweet_id>/', views.ajax_like, name='ajax_like'),
    path('ajax/follow/<str:username>/', views.ajax_follow, name='ajax_follow'),
    path('ajax/retweet/<int:tweet_id>/', views.ajax_retweet, name='ajax_retweet'),
     path('post-tweet/', views.post_tweet, name='post_tweet'),
      path('ajax/comment/<int:tweet_id>/', views.post_comment, name='post_comment'),

]

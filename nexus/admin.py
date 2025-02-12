# social_app/admin.py
from django.contrib import admin
from .models import (
    UserProfile, Badge, UserSettings, Tweet, Retweet, Like, SavedTweet, 
    TweetTopic, Thread, ContentView, Analytics, TrendingScore, Follow, 
    Mute, Block, Report, ActivityLog, Advertisement, Subscription, 
    SubscriptionPlan, SubscriptionFeature, PinnedTweet
)

# Register models for management in Django Admin
admin.site.register(UserProfile)
admin.site.register(Badge)
admin.site.register(UserSettings)
admin.site.register(Tweet)
admin.site.register(Retweet)
admin.site.register(Like)
admin.site.register(SavedTweet)
admin.site.register(TweetTopic)
admin.site.register(Thread)
admin.site.register(ContentView)
admin.site.register(Analytics)
admin.site.register(TrendingScore)
admin.site.register(Follow)
admin.site.register(Mute)
admin.site.register(Block)
admin.site.register(Report)
admin.site.register(ActivityLog)
admin.site.register(Advertisement)
admin.site.register(Subscription)
admin.site.register(SubscriptionPlan)
admin.site.register(SubscriptionFeature)
admin.site.register(PinnedTweet)

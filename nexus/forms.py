# social_app/forms.py
from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'media_url', 'topics']
 # nexus/forms.py
from django import forms
from .models import UserSettings

class SettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ['email_notifications', 'push_notifications', 'privacy_public', 'is_2fa_enabled', 'two_fa_method']
        widgets = {
            'two_fa_method': forms.Select(choices=[('SMS', 'SMS'), ('Email', 'Email')]),
        }

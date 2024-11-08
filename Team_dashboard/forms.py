# dashboard/forms.py

from django import forms
from champion.models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        exclude = ['verification_token', 'is_email_verified', 'submission_date', 'user']

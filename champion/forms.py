from django import forms
from django.contrib.auth.models import User
from .models import Registration

class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone Number', max_length=15)
    day = forms.IntegerField(label='Day', min_value=1, max_value=31)
    month = forms.IntegerField(label='Month', min_value=1, max_value=12)
    year = forms.IntegerField(label='Year', min_value=1900, max_value=2100)
    champion_reason = forms.CharField(widget=forms.Textarea, label='Why do you want to be a champion?')
    achievements = forms.CharField(widget=forms.Textarea, label='Your Achievements')
    unique_trait = forms.CharField(widget=forms.Textarea, label='What makes you unique?')
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    class Meta:
        model = Registration
        fields = ['phone', 'day', 'month', 'year', 'champion_reason', 'achievements', 'unique_trait']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username

    def save(self, commit=True, request=None):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        registration = Registration(
            user=user,
            phone=self.cleaned_data['phone'],
            day=self.cleaned_data['day'],
            month=self.cleaned_data['month'],
            year=self.cleaned_data['year'],
            champion_reason=self.cleaned_data['champion_reason'],
            achievements=self.cleaned_data['achievements'],
            unique_trait=self.cleaned_data['unique_trait']
        )
        registration.generate_verification_token()
        if commit:
            registration.save()
            if request:
                registration.send_verification_email(request)
        return registration

from django import forms

class LoginForm(forms.Form):
    username_or_email = forms.CharField(label='Username or Email', max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
from django import forms
from .models import Registration

from django import forms
from .models import Registration

class SocialMediaForm(forms.ModelForm):
    discord_id = forms.CharField(label='Discord ID', max_length=50, required=True)
    telegram_username = forms.CharField(label='Telegram Username/Number', max_length=50, required=True)
    profile_image = forms.ImageField(label='Profile Image', required=False)  # New field

    class Meta:
        model = Registration
        fields = ['discord_id', 'telegram_username', 'profile_image']
from django import forms

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)
from django import forms
from .models import SupportRequest

# forms.py
from django import forms
from .models import SupportRequest

class SupportRequestForm(forms.ModelForm):
    class Meta:
        model = SupportRequest
        fields = ['name', 'email', 'category', 'subject', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(SupportRequestForm, self).__init__(*args, **kwargs)
        if user and user.is_authenticated:
            # For logged-in users, set 'name' and 'email' as initial values and hide the fields
            self.fields['name'].initial = f"{user.first_name} {user.last_name}"
            self.fields['email'].initial = user.email
            self.fields['name'].widget = forms.HiddenInput()
            self.fields['email'].widget = forms.HiddenInput()
        else:
            # For non-authenticated users, make 'name' and 'email' required
            self.fields['name'].required = True
            self.fields['email'].required = True

from django import forms
from .models import Registration

from django import forms
from .models import Registration

class InformationForm(forms.ModelForm):
    discord_id = forms.CharField(
        label='What is your Discord ID?', 
        max_length=50, 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Discord ID'})
    )
    telegram_username = forms.CharField(
        label='What is your Telegram Username/Number?', 
        max_length=50, 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Telegram Username/Number'})
    )
    profile_image = forms.ImageField(
        label='Please upload a profile image?', 
        required=False, 
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )
    personality_traits = forms.CharField(
        label='What are your personality traits?',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Analytical, Loyal'}),
        required=False
    )
    skills = forms.CharField(
        label='What skills do you possess?',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Leadership, Coding'}),
        required=False
    )
    designation = forms.CharField(
        label='What is your current designation?',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Software Engineer'}),
        required=False
    )
    motivations = forms.CharField(
        label='What motivates you?',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What motivates you?'}),
        required=False
    )
    goals = forms.CharField(
        label='What are your goals?',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What are your goals?'}),
        required=False
    )
    bio = forms.CharField(
        label='Please write a bio for your profile?',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us something about yourself'}),
        required=False
    )
    address_line_1 = forms.CharField(
        label='Address line 1',
        max_length=255, 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your street address'})
    )
    address_line_2 = forms.CharField(
        label='Address line 2',
        max_length=255, 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apartment, suite, etc. (optional)'})
    )
    city = forms.CharField(
        label='city',
        max_length=100, 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'})
    )
    state = forms.CharField(
        label='state',
        max_length=100, 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your state or province'})
    )
    postal_code = forms.CharField(
        label='Zip Code',
        max_length=20, 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your postal/ZIP code'})
    )
    country = forms.CharField(
        label='Country',
        max_length=100, 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your country'})
    )

    class Meta:
        model = Registration
        fields = [
            'discord_id', 
            'telegram_username', 
            'profile_image',
            'personality_traits', 
            'skills', 
            'designation', 
            'motivations', 
            'goals', 
            'bio', 
            'address_line_1', 
            'address_line_2', 
            'city', 
            'state', 
            'postal_code', 
            'country'
        ]


from django import forms
from .models import Registration

class PublicProfileForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['bio', 'personality_traits', 'skills', 'motivations', 'goals', 'champion_reason', 'achievements', 'unique_trait']
class AssociateRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone Number', max_length=15)
    day = forms.IntegerField(label='Day', min_value=1, max_value=31)
    month = forms.IntegerField(label='Month', min_value=1, max_value=12)
    year = forms.IntegerField(label='Year', min_value=1900, max_value=2100)
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    class Meta:
        model = Registration
        fields = ['phone', 'day', 'month', 'year']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username

    def save(self, commit=True, request=None):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        registration = Registration(
            user=user,
            phone=self.cleaned_data['phone'],
            day=self.cleaned_data['day'],
            month=self.cleaned_data['month'],
            year=self.cleaned_data['year'],
        )
        registration.generate_verification_token()
        if commit:
            registration.save()
            if request:
                registration.send_verification_email(request)
        return registration
    
from django import forms
from .models import Partner

class PartnerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['name', 'email', 'company_name', 'website', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website (optional)'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message (optional)', 'rows': 4}),
        }
from django import forms
from .models import ExceptionalDonation

class ExceptionalDonationForm(forms.ModelForm):
    class Meta:
        model = ExceptionalDonation
        fields = ['name', 'email', 'address', 'amount']  # Include amount in the form
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address (optional)', 'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'placeholder': 'Enter exceptional amount', 'class': 'form-control'}),
        }
from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email', 'phone', 'resume', 'cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 5}),
        }
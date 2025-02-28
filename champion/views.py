# from django.shortcuts import render
# from datetime import timedelta
# from django.utils import timezone
# from django.shortcuts import render
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
# from .utils import send_email
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.tokens import default_token_generator
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from django.template.loader import render_to_string
# from django.shortcuts import render
# from datetime import timedelta
# from .models import Course
# from django.contrib.auth.models import User
# from django.urls import reverse
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import messages
# from .forms import RegistrationForm
# from .models import Registration
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.models import User
# from .forms import RegistrationForm
# from .models import Registration
# from django.shortcuts import render
# from .models import Video, UserVideoStatus
# from django.shortcuts import render
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import RegistrationForm
# from django.contrib.auth import logout
# from django.shortcuts import render
# from django.shortcuts import redirect, render
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.auth import get_user_model
# from django.utils.http import urlsafe_base64_decode
# from django.utils.encoding import force_str
# from .models import Registration
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as auth_login
# from django.contrib import messages
# from .forms import LoginForm
# from .models import Registration
# from django.contrib.auth.models import User
# from django.db.models import Q
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Registration
# from .forms import SocialMediaForm
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Registration
# from .forms import SocialMediaForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import PasswordChangeForm
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .forms import SupportRequestForm
# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Enrollment, UserVideoStatus, Registration, Video
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash
# from django.contrib import messages
# from django.shortcuts import get_object_or_404
# from django.utils import timezone
# from .models import Coupon, Course
# from decimal import Decimal
# from django.utils import timezone
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.shortcuts import redirect
# from datetime import timedelta
# from paypal.standard.forms import PayPalPaymentsForm
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Video, UserVideoStatus
# from datetime import timedelta
# import razorpay
# from django.conf import settings
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from paypal.standard.forms import PayPalPaymentsForm
# from .models import Video, UserVideoStatus
# from datetime import timedelta
# from decimal import Decimal
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponseBadRequest
# from django.shortcuts import redirect
# import razorpay
# import razorpay
# from django.conf import settings
# from django.shortcuts import render, get_object_or_404, redirect
# from django.urls import reverse
# from .models import Course, Enrollment
# from django.shortcuts import render, get_object_or_404
# from .models import Course, Enrollment
# from django.http import JsonResponse
# from django.contrib.auth.decorators import login_required
# from .models import UserVideoStatus

# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Course, Enrollment, Lesson, Category
# from django.contrib.auth.decorators import login_required

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils import timezone
# import json
# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Video, UserVideoStatus
# from django.views.decorators.csrf import csrf_exempt

# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model
# from django.shortcuts import redirect, render
# from django.views.decorators.csrf import csrf_exempt
# import razorpay

# from django.contrib.auth.models import User

# from django.contrib.auth.models import User
# from django.shortcuts import redirect
# from django.views.decorators.csrf import csrf_exempt
# import razorpay

# from django.contrib.auth.models import User
# from django.shortcuts import redirect
# from django.views.decorators.csrf import csrf_exempt
# import razorpay

# from django.shortcuts import redirect
# from django.urls import reverse
# import os
# import re
# from django.http import HttpResponse, StreamingHttpResponse
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Video, UserVideoStatus
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Video, UserVideoStatus
# from django.contrib.auth.decorators import login_required
# from paypal.standard.forms import PayPalPaymentsForm
# from django.urls import reverse

# from paypal.standard.models import ST_PP_COMPLETED
# from paypal.standard.ipn.signals import valid_ipn_received
# from django.dispatch import receiver


# def home(request):
#     try:
#         registration = request.user.registration
#         reapply_date = registration.submission_date + timedelta(days=90)
#     except AttributeError:
#         registration = None
#         reapply_date= None
#     print(reapply_date)
#     context = {
#         'reapply_date': reapply_date,
#         'registration': registration,
#         # other context data
#     }
#     return render(request, 'index.html',context)
# def apply(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save(request=request)  # Pass request to save method
#             messages.success(request, 'Your application has been submitted successfully! Please check your email to verify your account.')
#             return redirect('success_page')  # Redirect to a success page
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = RegistrationForm()

#     return render(request, 'application.html', {'form': form})

# @login_required
# def champions_dashboard(request):
#     try:
#         registration = request.user.registration
#         if registration.approved != 1:  # Check if the user is approved
#             return redirect('home')  # Redirect to home if not approved
#     except Registration.DoesNotExist:
#         return redirect('home')  # Redirect to home if no registration found

#     if registration.discord_id and registration.telegram_username:
#         form = None  # No need to show the form
#     else:
#         if request.method == 'POST':
#             form = SocialMediaForm(request.POST, request.FILES, instance=registration)
#             if form.is_valid():
#                 form.save()
#                 return redirect('champions_dashboard')  # Redirect back to the dashboard after saving
#         else:
#             form = SocialMediaForm(instance=registration)

#     context = {
#         'registration': registration,
#         'form': form,
#     }
#     return render(request, 'champions_dashboard.html', context)

# @login_required
# def video_play(request, video_id):
#     video = get_object_or_404(Video, id=video_id)
#     user_status, created = UserVideoStatus.objects.get_or_create(user=request.user, video=video)
    
#     if not user_status.has_paid:
#         return redirect('video_payment', video_id=video.id)

#     context = {
#         'video': video,
#         'last_watched_time': user_status.last_watched_time.total_seconds(),
#     }
#     return render(request, 'video_play.html', context)
#     category = Category.objects.all()
#     courses = Course.objects.all()
#     return render(request, 'course_list.html', {'courses': courses,'category':category})
# from collections import defaultdict

# def course_list(request):
#     categories = Category.objects.all()
#     courses_by_category = defaultdict(list)

#     # Group courses by category
#     for course in Course.objects.all():
#         courses_by_category[course.category].append(course)
#     print(courses_by_category)
#     print(categories)
    
#     return render(request, 'course_list.html', {
#         'courses_by_category': courses_by_category,
#         'categories': categories
#     })

# @login_required 
# def enroll_in_course(request, course_id):
#     course = get_object_or_404(Course, id=course_id)

#     # Create a Razorpay Order
#     amount = int(course.price * 100)  # Razorpay works with paise, so convert the amount to paise
#     currency = 'INR'
#     client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
#     razorpay_order = client.order.create({
#         'amount': int(course.price * 100),  # Convert to paise (smallest currency unit)
#         'currency': 'INR',
#         'payment_capture': '1',  # Auto capture the payment
#         'notes': {
#             'user_id': str(request.user.id),  # Include user_id in metadata
#             'course_id': str(course_id)
#         }
#     })
   
#     context = {
#         'course': course,
#         'razorpay_order_id': razorpay_order['id'],
#         'razorpay_key_id': settings.RAZORPAY_KEY_ID,
#         'amount': course.price,
#         'currency': 'INR'
#     }
#     # Store the order ID in session for verification later
#     request.session['razorpay_order_id'] = razorpay_order['id']

#     # Pass the order details to the template
   
#     return render(request, 'course_payment.html', context)
# @login_required
# def course_content(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
#     sections = course.sections.all()

#     # Retrieve the current lesson, and find the next and previous lessons
#     current_lesson_id = request.GET.get('lesson_id')
#     if current_lesson_id:
#         current_lesson = get_object_or_404(Lesson, id=current_lesson_id, section__course=course)
#     else:
#         current_lesson = sections.first().lessons.first() if sections.exists() and sections.first().lessons.exists() else None

#     previous_lesson = Lesson.objects.filter(section__course=course, id__lt=current_lesson.id).order_by('-id').first() if current_lesson else None
#     next_lesson = Lesson.objects.filter(section__course=course, id__gt=current_lesson.id).order_by('id').first() if current_lesson else None

#     context = {
#         'course': course,
#         'sections': sections,
#         'current_lesson': current_lesson,
#         'previous_lesson': previous_lesson,
#         'next_lesson': next_lesson,
#     }
#     return render(request, 'course_content.html', context)

# def course_list(request):
# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username_or_email = form.cleaned_data['username_or_email']
#             password = form.cleaned_data['password']

#             # Check if the input is an email
#             try:
#                 user = User.objects.get(Q(username=username_or_email) | Q(email=username_or_email))
#             except User.DoesNotExist:
#                 user = None

#             if user:
#                 user = authenticate(request, username=user.username, password=password)
#                 if user is not None:
#                     try:
#                         registration = Registration.objects.get(user=user)
#                         if registration.is_email_verified:
#                             auth_login(request, user)
#                             return redirect('home')  # Redirect to the home page or dashboard
#                         else:
#                             messages.error(request, 'Your email is not verified. Please verify your email to login.')
#                     except Registration.DoesNotExist:
#                         messages.error(request, 'No registration data found. Please contact support.')
#                 else:
#                     messages.error(request, 'Invalid username or password.')
#             else:
#                 messages.error(request, 'No user found with the provided credentials.')
#     else:
#         form = LoginForm()
    
#     return render(request, 'login.html', {'form': form})
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout, update_session_auth_hash
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse, HttpResponseBadRequest
from django.conf import settings
from django.db.models import Q
from django.template.loader import render_to_string
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from datetime import timedelta
from decimal import Decimal
import json
import razorpay
import os
import re
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver

from .models import EMPLOYMENT_TYPE_CHOICES, QuizResponse, User,Course, Enrollment, Video, UserVideoStatus, Registration, Lesson, Category, Coupon, Transaction
from .forms import RegistrationForm, SocialMediaForm, SupportRequestForm, LoginForm
from .utils import send_email

def home(request):
    try:
        
        registration = request.user.registration
        reapply_date = registration.submission_date + timedelta(days=90)
    except AttributeError:
        registration = None
        reapply_date = None
    
    

    context = {
        'reapply_date': reapply_date,
        'registration': registration,
        'hide_special_button': True,
        'navbar_opacity': 0.6,
        # Pass the courses to the context
    }
    return render(request, 'index.html', context)

def learnmore(request):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    return render(request, 'learn_more.html',{'registration':registration})
def apply(request):
    return render(request, 'application.html')
from .forms import AssociateRegistrationForm, InformationForm, PasswordResetRequestForm, PublicProfileForm, RegistrationForm


# champions/views.py


def events(request):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    
    return render(request, 'events.html', {'registration': registration})

from django.db.models import Q
from django.core.paginator import Paginator
from .models import Video, VideoCategory, UserVideoStatus

from django.db.models import Q

from django.db.models import Q

def video_home(request):
    categories = VideoCategory.objects.all()
    search_query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')
    reels = Reel.objects.filter(category=4)
    print(reels)
    # If the user searches or applies category filters, show filtered results
    if search_query or category_filter:
        videos = Video.objects.all()

        # Filter by search query
        if search_query:
            videos = videos.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query)
            )

        # Filter by category if one is selected
        if category_filter:
            videos = videos.filter(videocategory__id=category_filter)
        
        videos_grouped = None  # No need for grouped view when filtering or searching
    else:
        # No search or category filter - group by category
        videos_grouped = {}
        for category in categories:
            videos_grouped[category] = Video.objects.filter(videocategory=category)
        videos = None  # No need for ungrouped video list when grouped by category

    registration = None
    if request.user.is_authenticated:
        user_video_statuses = UserVideoStatus.objects.filter(user=request.user)
        registration = request.user.registration
    else:
        user_video_statuses = UserVideoStatus.objects.none()

    context = {
        'categories': categories,
        'videos': videos,
        'reels':reels,  # List of videos when filtering or searching
        'videos_grouped': videos_grouped,  # Grouped videos when no filters/search
        'user_video_statuses': user_video_statuses,
        'registration': registration,
        'search_query': search_query,
        'selected_category': category_filter,
    }
    return render(request, 'video_home.html', context)



def logout_view(request):
    logout(request)
    return redirect('home')  

def apply(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(request=request)  # Pass request to save method
            messages.success(request, 'Your application has been submitted successfully! Please check your email to verify your account.')
            return redirect('success_page')  # Redirect to a success page
        else:
            # Add a message for each field error
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegistrationForm()

    return render(request, 'application.html', {'form': form})
def associate_reg(request):
    if request.method == 'POST':
        form = AssociateRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)  # Do not save to the database yet
            registration.approved = 2
            registration.joined_as = False  # Set the approval status to 'Rejected'
            registration.save()
            registration.send_verification_email(request)  # Now save the object to the database
            messages.success(request, 'Your application has been submitted successfully! Please check your email to verify your account.')
            return redirect('success_page')  # Redirect to a success page
        else:
            # Add a message for each field error
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = AssociateRegistrationForm()

    return render(request, 'associate_registration.html', {'form': form})

def success_page(request):
        
    return render(request, 'success.html', {'message': 'Thank you. Please check your email for a verification link. verify Email before sign in'})
# champions/views.py



def verify_email(request, uidb64, token):
    try:
        # Decode the uidb64 to get the user's ID
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
        registration = Registration.objects.get(user=user)
        
        # Check if the token is valid for the user
        if default_token_generator.check_token(user, token):
            if not registration.is_email_verified:
                registration.is_email_verified = True
                registration.save()
                messages.success(request, 'Your email has been verified successfully!')
            else:
                messages.info(request, 'Your email is already verified.')
        else:
            messages.error(request, 'The verification link is invalid or has expired.')
    except (TypeError, ValueError, OverflowError, Registration.DoesNotExist, get_user_model().DoesNotExist):
        messages.error(request, 'The verification link is invalid or has expired.')

    return redirect('login')  # Redirect to login or another appropriate page


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']

            # Check if the input matches either a username or an email
            try:
                user = User.objects.get(Q(username=username_or_email) | Q(email=username_or_email))
            except User.DoesNotExist:
                user = None

            if user:
                # Authenticate the user based on the username (from the retrieved user) and password
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    try:
                        registration = Registration.objects.get(user=user)
                        if registration.is_email_verified:
                            auth_login(request, user)
                            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
                            return redirect(next_url) # Redirect to the home page or dashboard
                        else:
                            messages.error(request, 'Your email is not verified. Please verify your email to login.')
                    except Registration.DoesNotExist:
                        messages.error(request, 'No registration data found. Please contact support.')
                else:
                    messages.error(request, 'Invalid password. Please try again.')
            else:
                messages.error(request, 'No user found with the provided username or email.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


from django.contrib import messages

@login_required
def champions_dashboard(request):
    user = request.user
    registration = user.registration
    enrollments = Enrollment.objects.filter(user=user)
    watched_videos = UserVideoStatus.objects.filter(user=user)
    
    # List of required fields to check
    required_fields = [
        registration.discord_id,
        registration.telegram_username,
        registration.personality_traits,
        registration.skills,
        registration.designation,
        registration.motivations,
        registration.goals,
        registration.address_line_1,
        registration.city,
        registration.state,
        registration.postal_code,
        registration.country
    ]

    # Redirect to information form if any required field is missing
    if not all(required_fields):
        return redirect('information_form')

    # Check if membership is paid, otherwise redirect to payment
    if not registration.membership_paid:
        return redirect('membership_payment')  # Redirect to payment if membership not paid

    if request.method == 'POST':
        print(request.POST)
        # Handle visibility update
        if 'update_visibility' in request.POST:
            registration.is_public = request.POST.get('is_public', '') == 'on'
            registration.save()
            messages.success(request, 'Visibility updated successfully.')
        
        # Handle profile info update
        elif 'update_info' in request.POST:
            form = PublicProfileForm(request.POST, instance=registration)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile information updated successfully.')
            else:
                messages.error(request, 'Please correct the errors in the form.')
        
        # Handle profile picture update
        elif 'profile_image' in request.FILES:
            profile_image = request.FILES['profile_image']
            registration.profile_image = profile_image
            registration.save()
            messages.success(request, 'Profile picture updated successfully.')
        else:
            print("No file found in request.FILES")

    # Instantiate form with current registration data
    form = PublicProfileForm(instance=registration)

    context = {
        'registration': registration,
        'form': form,
        'enrollments': enrollments,
        'watched_videos': watched_videos,
    }
    return render(request, 'champions_dashboard.html', context)



@login_required
def change_password(request):
    registration = request.user.registration
    enrollments = Enrollment.objects.filter(user=request.user)
    watched_videos = UserVideoStatus.objects.filter(user=request.user)
    form = PublicProfileForm(instance=registration)
    if request.method == 'POST':
        form_pass = PasswordChangeForm(user=request.user, data=request.POST)
        if form_pass.is_valid():
            user = form_pass.save()
            update_session_auth_hash(request, user)  # Prevents user from being logged out after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('champions_dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'champions_dashboard.html', {'form_pass': form_pass,'registration': registration,
        'form': form,
        'enrollments': enrollments,
        'watched_videos': watched_videos,})

@login_required
def deactivate_account(request):
    registration = request.user.registration
    if request.method == 'POST':
        # Deactivate the user account
        request.user.is_active = False
        request.user.save()

        # Set the deactivation date
        registration.deactivated_at = timezone.now()
        registration.save()

        messages.success(request, 'Your account has been deactivated. You can reactivate it within 90 days.')
        return redirect('home')

    return redirect('champions_dashboard')
@login_required
def reactivate_account(request):
    registration = request.user.registration
    if registration.is_deactivation_pending():
        request.user.is_active = True
        request.user.save()
        registration.deactivated_at = None
        registration.save()
        messages.success(request, 'Your account has been reactivated successfully.')
    else:
        messages.error(request, 'Reactivation period has expired. Please contact support.')
    return redirect('champions_dashboard')
@login_required
def membership_payment(request):
    if request.user.registration.membership_paid:
        return redirect('champions_dashboard')  # Redirect if the user has already paid

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    
    membership_price = 9999  # Rs. 99 in paise

    razorpay_order = client.order.create({
        'amount': membership_price,  # Amount in paise
        'currency': 'USD',
        'payment_capture': '1',  # Auto capture the payment
        'notes': {
            'user_id': str(request.user.id),
            'membership': 'Annual'
        }
    })

    context = {
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'amount': membership_price / 100,  # Convert back to INR
        'currency': 'USD'
    }
    return render(request, 'membership_payment.html', context)

@csrf_exempt
def razorpay_membership_return(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')

        # Verify the payment and signature with Razorpay
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        try:
            client.utility.verify_payment_signature(params_dict)

            # Retrieve the order details to get user_id and video_id
            order_details = client.order.fetch(order_id)
            user_id = order_details['notes']['user_id']
            membership = order_details['notes']['membership']
            payment_amount = order_details['amount'] / 100
            # Log the user back in
            user = User.objects.get(id=user_id)
            auth_login(request, user)

            # Update the user's video status to paid and redirect to the video play page
            registration = request.user.registration
            registration.membership_paid = True
            registration.paid_on = timezone.now()
            Transaction.objects.create(
                user=user,
                amount=payment_amount,
                description=f"Membership payment for {membership}."
            )
            registration.save()

        # Redirect to the information form or directly to the dashboard if already filled
            if registration.personality_traits and registration.skills:
                return redirect('champions_dashboard')
            else:
                return redirect('information_form')      
        except razorpay.errors.SignatureVerificationError:
            return redirect('error_page') 


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == ST_PP_COMPLETED:
        invoice = ipn.invoice.split('-')
        user_id = invoice[0]
        video_id = invoice[1]
        user_status_id = invoice[2]

        user_status = UserVideoStatus.objects.get(id=user_status_id)
        user_status.has_paid = True
        user_status.save()

def check_user_access(user, video):
    if user.is_authenticated:
        # Assuming you have a model that tracks purchases
        return UserVideoStatus.objects.filter(user=user, video=video).exists()
    return False
@login_required
def video_preview(request, video_id):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    video = get_object_or_404(Video, id=video_id)
    comments = Comment.objects.filter(video=video, is_hidden=False).order_by('-created_at')
    

    # Get suggested videos (e.g., other videos)
    suggested_videos = Video.objects.exclude(id=video.id)[:10]
    context = {
        'video': video,
        'comments': comments,
        'suggested_videos': suggested_videos,
        'registration':registration
    }
    return render(request, 'video_preview.html', context)
import uuid
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from .models import Video, VideoAccessToken
from .models import VideoAccessToken
def generate_video_access_token(user, video):
    print("Token genrated")
    token = uuid.uuid4().hex
    expires_at = timezone.now() + timedelta(minutes=1)  # Token valid for 10 minutes
    VideoAccessToken.objects.create(user=user, video=video, token=token, expires_at=expires_at)
    return token
from django.templatetags.static import static
@login_required
def video_play(request, video_id):
     
    services = [
        {
            'title': 'TCC ACADEMIA',
            'description': 'Recorded and Live coaching sessions to boost your performance.',
            'url': '/courses',
            'image_url': request.build_absolute_uri(static('images/android.png')),
        },
        {
            'title': 'Our Shorts',
            'description': 'Interactive short form videos.',
            'url': '/shorts',
            'image_url': request.build_absolute_uri(static('images/android.png')),
        },
        {
            'title': 'Online Courses',
            'description': 'Learn at your own pace with our comprehensive online courses.',
            'url': '/membership_portal',
            'image_url': request.build_absolute_uri(static('images/android.png')),
        },
        # Add more services as needed
    ]
    video = get_object_or_404(Video, id=video_id)
    print(video)
    user_has_access = check_user_access(request.user, video)
    token = None
    comments = Comment.objects.filter(video=video, is_hidden=False).order_by('-created_at')
    if request.method == 'POST' and request.user.is_authenticated:
        comment_text = request.POST.get('comment_text')
        if comment_text:
            Comment.objects.create(video=video, user=request.user, comment_text=comment_text)
            return redirect('video_preview', video_id=video.id)

    # Get suggested videos (e.g., other videos)
    suggested_videos = Video.objects.exclude(id=video.id)[:10]
    if user_has_access:
        token = generate_video_access_token(request.user, video)
    user_status, created = UserVideoStatus.objects.get_or_create(user=request.user, video=video)
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    
    if not user_status.has_paid:
        
        return redirect('video_payment', video_id=video.id)

    if user_status.has_completed:
        return redirect('video_payment', video_id=video.id)
    print("HEllo"+token)
    context = {
        'video': video,
        'token': token,
        'comments': comments,
        'suggested_videos': suggested_videos,
        'last_watched_time': user_status.last_watched_time.total_seconds() if user_status.last_watched_time else 0,
        'registration':registration,
        'services': services,
    }
    return render(request, 'video_play.html', context)
import re
import requests
from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Video, UserVideoStatus
from django.http import HttpResponseForbidden, StreamingHttpResponse
@login_required
def stream_video(request, video_id):
    token = request.GET.get('token')
    if not token:
        return HttpResponseForbidden('Access Denied')

    try:
        access_token = VideoAccessToken.objects.get(user=request.user, video_id=video_id, token=token)
        if access_token.expires_at < timezone.now():
            return HttpResponseForbidden('Token Expired')
    except VideoAccessToken.DoesNotExist:
        return HttpResponseForbidden('Invalid Token')
    video = get_object_or_404(Video, id=video_id)
    user_has_access = check_user_access(request.user, video)

    user_status = get_object_or_404(UserVideoStatus, user=request.user, video=video)

    if not user_status.has_paid:
        return redirect('video_payment', video_id=video.id)

    # Use the URL of the video stored in S3
    video_url = video.video_file.url  # Use .url to get the S3 URL of the video
    
    # Handle byte range requests (for video streaming)
    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)
    content_type = 'video/mp4'
    
    headers = {}  # S3 request headers
    
    if range_match:
        # For partial content requests (range headers)
        first_byte, last_byte = range_match.groups()
        first_byte = int(first_byte) if first_byte else 0
        last_byte = int(last_byte) if last_byte else None  # May be None, meaning to the end
        
        # Add range header to request
        headers['Range'] = f'bytes={first_byte}-{last_byte if last_byte else ""}'
        
        # Make a partial request to S3 using the Range header
        video_response = requests.get(video_url, headers=headers, stream=True)
        
        # Check if request is valid (S3 will return a 206 for partial content)
        if video_response.status_code == 206:
            response = StreamingHttpResponse(video_response.raw, status=206, content_type=content_type)
            response['Content-Range'] = video_response.headers.get('Content-Range')
        else:
            # If no range or invalid range, return the whole video
            response = StreamingHttpResponse(video_response.raw, content_type=content_type)
    else:
        # Serve the whole file if no range header is present
        video_response = requests.get(video_url, stream=True)
        response = StreamingHttpResponse(video_response.raw, content_type=content_type)

    response['Accept-Ranges'] = 'bytes'
    response['Content-Type'] = content_type
    return response

# @login_required
# def stream_video(request, video_id):
#     video = get_object_or_404(Video, id=video_id)
#     print(video)
#     user_status = get_object_or_404(UserVideoStatus, user=request.user, video=video)

#     if not user_status.has_paid:
#         return redirect('video_payment', video_id=video.id)

#     video_path = video.video_file.path
#     print(video_path)  # Assuming the Video model has a FileField named `file`
#     file_size = os.path.getsize(video_path)
#     print(file_size)
#     range_header = request.META.get('HTTP_RANGE', '').strip()
#     range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)
#     content_type = 'video/mp4'
#     response = HttpResponse()

#     if range_match:
#         first_byte, last_byte = range_match.groups()
#         first_byte = int(first_byte) if first_byte else 0
#         last_byte = int(last_byte) if last_byte else file_size - 1
#         length = last_byte - first_byte + 1
#         response.status_code = 206
#         response['Content-Range'] = f'bytes {first_byte}-{last_byte}/{file_size}'
#         response['Accept-Ranges'] = 'bytes'
#         response['Content-Length'] = str(length)

#         with open(video_path, 'rb') as video_file:
#             video_file.seek(first_byte)
#             response.write(video_file.read(length))
#     else:
#         response = StreamingHttpResponse(open(video_path, 'rb'), content_type=content_type)
#         response['Content-Length'] = str(file_size)

#     response['Content-Type'] = content_type
#     return response
import os
import re
from django.http import StreamingHttpResponse, HttpResponse, Http404
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def stream_static_video(request, video_filename):
    # For development, use STATICFILES_DIRS
    video_path = os.path.join(settings.STATICFILES_DIRS[0], 'videos', video_filename)
    
    video_path = "C:/Users/SHAGUN KALASH/Desktop/champions/champions/champion/static/videos/"+video_filename
    print(f"Serving video from: {video_path}")  # Add this for debugging
    
    if not os.path.exists(video_path):
        raise Http404(f"Video '{video_filename}' not found.")
    
    # Rest of the code
    # Check if the video exists
    if not os.path.exists(video_path):
        raise Http404(f"Video '{video_filename}' not found.")

    file_size = os.path.getsize(video_path)
    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)
    content_type = 'video/mp4'
    response = HttpResponse()

    if range_match:
        first_byte, last_byte = range_match.groups()
        first_byte = int(first_byte) if first_byte else 0
        last_byte = int(last_byte) if last_byte else file_size - 1
        length = last_byte - first_byte + 1
        response.status_code = 206
        response['Content-Range'] = f'bytes {first_byte}-{last_byte}/{file_size}'
        response['Accept-Ranges'] = 'bytes'
        response['Content-Length'] = str(length)

        with open(video_path, 'rb') as video_file:
            video_file.seek(first_byte)
            response.write(video_file.read(length))
    else:
        response = StreamingHttpResponse(open(video_path, 'rb'), content_type=content_type)
        response['Content-Length'] = str(file_size)

    response['Content-Type'] = content_type
    return response

@login_required
def video_payment(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    user_status, created = UserVideoStatus.objects.get_or_create(
        user=request.user, 
        video=video,
        defaults={'last_watched_time': timedelta(0)}
    )

    original_price = video.price
    discount = Decimal(0)

    # Apply 25% discount if membership is paid
    if request.user.registration.membership_paid:
        discount += Decimal(25)  # 25% discount

    # Apply additional 10% discount if video is completed
    if user_status.has_completed:
        discount += Decimal(10)  # Additional 10% discount

    # Calculate final price
    final_price = original_price * (Decimal(1) - discount / Decimal(100))

    # Redirect logic based on user video status
    if user_status.has_paid and not user_status.has_completed:
        return redirect('video_play', video_id=video.id)

    # Razorpay Integration
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    razorpay_order = client.order.create({
        'amount': int(final_price * 100),  # Convert to paise (smallest currency unit, assuming INR)
        'currency': 'USD',  # or 'USD' if your Razorpay account supports it
        'payment_capture': '1',  # Auto capture the payment
        'notes': {
            'user_id': str(request.user.id),  # Include user_id in metadata
            'video_id': str(video_id)
        }
    })

    context = {
        'video': video,
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'amount': final_price,
        'currency': 'USD'  # or 'USD'
    }
    return render(request, 'video_payment.html', context)


def paypal_return(request):
    # Extract the video_id from the GET parameters (or session, if stored there)
    video_id = request.GET.get('video_id')

    if not video_id:
        # Handle the error if video_id is not found
        # You might want to redirect to an error page or show a message
        return redirect('error_page')

    return redirect('video_play', video_id=video_id)

@csrf_exempt
def razorpay_return(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')

        # Verify the payment and signature with Razorpay
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        try:
            client.utility.verify_payment_signature(params_dict)

            # Retrieve the order details to get user_id and video_id
            order_details = client.order.fetch(order_id)
            user_id = order_details['notes']['user_id']
            video_id = order_details['notes']['video_id']
            payment_amount = order_details['amount'] / 100
            # Log the user back in
            user = User.objects.get(id=user_id)
            auth_login(request, user)

            # Update the user's video status to paid and redirect to the video play page
            user_status = UserVideoStatus.objects.get(video_id=video_id, user=user)
            user_status.has_paid = True
            user_status.has_completed=False
            user_status.last_watched_time = timedelta(0)
            Transaction.objects.create(
                user=user,
                amount=payment_amount,
                description=f"Membership payment for {video_id}."
            )
            user_status.save()

            return redirect('video_play', video_id=video_id)
        except razorpay.errors.SignatureVerificationError:
            return redirect('error_page')  # Handle the error as needed


# @login_required
# def video_play(request, video_id):
#     video = get_object_or_404(Video, id=video_id)
#     user_status = get_object_or_404(UserVideoStatus, user=request.user, video=video)

#     # Get the last watched time in seconds
#     last_watched_time = round(user_status.last_watched_time.total_seconds(), 2)
#     print(f"Last watched time: {last_watched_time}")
#     context = {
#         'video': video,
#         'last_watched_time': last_watched_time,
#     }
#     return render(request, 'video_play.html', context)

@csrf_exempt
@login_required
def update_video_time(request, video_id):
    if request.method == 'POST':
        video = get_object_or_404(Video, id=video_id)
        user_status = get_object_or_404(UserVideoStatus, user=request.user, video=video)
        data = json.loads(request.body)
        user_status.last_watched_time = timezone.timedelta(seconds=data.get('time', 0))
        user_status.save()
        return JsonResponse({'status': 'success'})

@csrf_exempt
@login_required
def complete_video(request, video_id):
    if request.method == 'POST':
        video = get_object_or_404(Video, id=video_id)
        user_status = get_object_or_404(UserVideoStatus, user=request.user, video=video)
        user_status.has_completed = True
        user_status.has_paid = False
        user_status.save()
        return JsonResponse({'status': 'success'})



from collections import defaultdict

def course_list(request):
    categories = Category.objects.all()
    courses_by_category = defaultdict(list)
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    # Group courses by category
    for course in Course.objects.all():
        courses_by_category[course.category].append(course)
    print(courses_by_category)
    for category in categories:
        print(category)
    return render(request, 'course_list.html', {
        'courses_by_category': courses_by_category.items(),
        'categories': categories,
        'registration':registration
    })


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrolled = False
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
        enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()
    
    # Fetch the sections and their related videos
    sections = course.sections.prefetch_related('lessons').all()
    print(sections)
    

    context = {
        'course': course,
        'enrolled': enrolled,
        'sections': sections,
        'registration':registration
    }

    return render(request, 'course_detail.html', context)


# Initialize Razorpay client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@login_required
@csrf_exempt
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    coupon_code = request.POST.get('coupon_code', '')
    discount = 0
    discount = 0
    if request.user.registration.membership_paid:
        discount=Decimal(25)

    # Check if a valid coupon was applied
    if coupon_code:
        try:
            coupon = Coupon.objects.get(code=coupon_code, is_active=True)
            print(coupon)
            if coupon.is_active:
                discount += coupon.discount
                print(discount)
            else:
                messages.error(request, "This coupon is no longer valid.")
        except Coupon.DoesNotExist:
            messages.error(request, "Invalid coupon code.")

    # Calculate the final price after applying the discount
    

    final_price = course.price * (Decimal(1) - Decimal(discount) / Decimal(100))

    print(final_price)
    # Proceed with the payment process using the discounted price
    amount = int(final_price * 100)  # Razorpay expects the amount in paise

    # Create Razorpay Order
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    razorpay_order = client.order.create({
        'amount': amount,
        'currency': 'USD',
        'payment_capture': '1',
        'notes': {
            'user_id': str(request.user.id),
            'course_id': str(course_id)
        }
    })

    # Pass necessary details to the template
    context = {
        'course': course,
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'amount': final_price,
        'currency': 'USD'
    }

    return render(request, 'course_payment.html', context)


@csrf_exempt
def razorpay_callback(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')

        # Verify the payment and signature with Razorpay
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        try:
            client.utility.verify_payment_signature(params_dict)

            # Retrieve the order details to get user_id and video_id
            order_details = client.order.fetch(order_id)
            user_id = order_details['notes']['user_id']
            course_id = order_details['notes']['course_id']
            payment_amount = order_details['amount'] / 100
            # Log the user back in
            user = User.objects.get(id=user_id)
            auth_login(request, user)
            # Payment was successful, create the enrollment
            Transaction.objects.create(
                user=user,
                amount=payment_amount,
                description=f"Membership payment for {course_id}."
            )
            course = get_object_or_404(Course, id=course_id)
            enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
            channel_layer = get_channel_layer()
            message = f"{user.username} has bought {course} and became part of The Champions Club!"
            async_to_sync(channel_layer.group_send)(
        "notifications", {
            "type": "send_notification",
            "message": message,
        }
    )
            return redirect('course_detail', course_id=course.id)
        except razorpay.errors.SignatureVerificationError:
            return HttpResponseBadRequest("Payment verification failed.")

    return HttpResponseBadRequest("Invalid request.")




# @login_required
# def course_content(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
#     sections = course.sections.all()
#     registration = None
#     if request.user.is_authenticated:
#         registration = request.user.registration

#     # Retrieve the current lesson, and find the next and previous lessons
#     current_lesson_id = request.GET.get('lesson_id')
#     if current_lesson_id:
#         current_lesson = get_object_or_404(Lesson, id=current_lesson_id, section__course=course)
#     else:
#         current_lesson = sections.first().lessons.first() if sections.exists() and sections.first().lessons.exists() else None

#     previous_lesson = Lesson.objects.filter(section__course=course, id__lt=current_lesson.id).order_by('-id').first() if current_lesson else None
#     next_lesson = Lesson.objects.filter(section__course=course, id__gt=current_lesson.id).order_by('id').first() if current_lesson else None

#     context = {
#         'course': course,
#         'sections': sections,
#         'current_lesson': current_lesson,
#         'previous_lesson': previous_lesson,
#         'next_lesson': next_lesson,
#         'registration':registration
#     }
#     return render(request, 'course_content.html', context)
from .models import Quiz,Review,Comment
@login_required
def course_content(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
    sections = course.sections.all()
    registration = None
    current_lesson = None
    current_quiz = None
    quiz_questions = None
    quiz_submitted = False
    quiz_results = {}
    quiz_already_submitted = False
    comments = []
    reviews = []

    if request.user.is_authenticated:
        registration = request.user.registration

    # Retrieve the current lesson or quiz based on the GET parameters
    current_lesson_id = request.GET.get('lesson_id')
    current_quiz_id = request.GET.get('quiz_id')

    if current_lesson_id:
        current_lesson = get_object_or_404(Lesson, id=current_lesson_id, section__course=course)
        comments = current_lesson.comments.all()
        reviews = current_lesson.reviews.all()
    elif current_quiz_id:
        current_quiz = get_object_or_404(Quiz, id=current_quiz_id, section__course=course)
        quiz_questions = current_quiz.questions.all()

        # Check if the quiz has already been submitted by the user
        quiz_responses = QuizResponse.objects.filter(user=request.user, quiz=current_quiz)
        if quiz_responses.exists():
            quiz_already_submitted = True
            # Populate the quiz_results to show the previously submitted answers
            for response in quiz_responses:
                quiz_results[response.question.id] = {
                    'question': response.question,
                    'selected_option': response.selected_option,
                    'correct': response.is_correct,
                }

    # Handle quiz submission or restart
    if request.method == 'POST':
        if 'submit_quiz' in request.POST:
            if quiz_already_submitted:
                # If the quiz was already submitted and the user wants to restart, delete previous responses
                QuizResponse.objects.filter(user=request.user, quiz=current_quiz).delete()
                quiz_already_submitted = False
                quiz_results = {}
                quiz_submitted = False
            else:
                # Handle quiz submission
                quiz_submitted = True
                for question in quiz_questions:
                    selected_option_id = request.POST.get(f'question_{question.id}')
                    if selected_option_id:
                        selected_option = question.answers.get(id=selected_option_id)
                        correct = selected_option.is_correct

                        quiz_results[question.id] = {
                            'question': question,
                            'selected_option': selected_option,
                            'correct': correct,
                        }

                        # Store the response
                        QuizResponse.objects.create(
                            user=request.user,
                            quiz=current_quiz,
                            is_correct=correct,
                            question=question,
                            selected_option=selected_option
                        )

        elif 'submit_comment' in request.POST:
            comment_text = request.POST.get('comment_text')
            if comment_text and current_lesson:
                Comment.objects.create(
                    user=request.user,
                    lesson=current_lesson,
                    comment_text=comment_text
                )
        
        elif 'submit_review' in request.POST:
            rating = request.POST.get('rating')
            review_text = request.POST.get('review_text')
            if rating and current_lesson:
                Review.objects.create(
                    user=request.user,
                    lesson=current_lesson,
                    rating=rating,
                    review_text=review_text
                )

    # Find the next and previous lessons if a lesson is selected
    previous_lesson = (
        Lesson.objects.filter(section__course=course, id__lt=current_lesson.id)
        .order_by('-id').first() if current_lesson else None
    )
    next_lesson = (
        Lesson.objects.filter(section__course=course, id__gt=current_lesson.id)
        .order_by('id').first() if current_lesson else None
    )

    context = {
        'course': course,
        'sections': sections,
        'current_lesson': current_lesson,
        'previous_lesson': previous_lesson,
        'next_lesson': next_lesson,
        'current_quiz': current_quiz,
        'quiz_questions': quiz_questions,
        'quiz_submitted': quiz_submitted,
        'quiz_results': quiz_results,
        'quiz_already_submitted': quiz_already_submitted,
        'registration': registration,
        'comments': comments,
        'reviews': reviews,
    }
    return render(request, 'course_content.html', context)
import requests

import re
import requests
from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lesson

@login_required
def stream_lesson(request, video_id):
    lesson = get_object_or_404(Lesson, id=video_id)
    
    # Use the URL of the video stored in S3
    video_url = lesson.video.url  # Assuming the Lesson model has a FileField for video
    
    # Handle byte range requests (for video streaming)
    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)
    content_type = 'video/mp4'
    
    headers = {}  # S3 request headers
    
    if range_match:
        # For partial content requests (range headers)
        first_byte, last_byte = range_match.groups()
        first_byte = int(first_byte) if first_byte else 0
        last_byte = int(last_byte) if last_byte else None  # May be None, meaning to the end
        
        # Add range header to request
        headers['Range'] = f'bytes={first_byte}-{last_byte if last_byte else ""}'
        
        # Make a partial request to S3 using the Range header
        video_response = requests.get(video_url, headers=headers, stream=True)
        
        # Check if request is valid (S3 will return a 206 for partial content)
        if video_response.status_code == 206:
            response = StreamingHttpResponse(video_response.raw, status=206, content_type=content_type)
            response['Content-Range'] = video_response.headers.get('Content-Range')
        else:
            # If no range or invalid range, return the whole video
            response = StreamingHttpResponse(video_response.raw, content_type=content_type)
    else:
        # Serve the whole file if no range header is present
        video_response = requests.get(video_url, stream=True)
        response = StreamingHttpResponse(video_response.raw, content_type=content_type)

    response['Accept-Ranges'] = 'bytes'
    response['Content-Type'] = content_type
    return response

# @login_required
# def stream_lesson(request, video_id):
#     lesson = get_object_or_404(Lesson, id=video_id)
    

#     video_path = lesson.video.path
#     print(video_path)  # Assuming the Video model has a FileField named `file`
#     file_size = os.path.getsize(video_path)
#     print(file_size)
#     range_header = request.META.get('HTTP_RANGE', '').strip()
#     range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)
#     content_type = 'video/mp4'
#     response = HttpResponse()

#     if range_match:
#         first_byte, last_byte = range_match.groups()
#         first_byte = int(first_byte) if first_byte else 0
#         last_byte = int(last_byte) if last_byte else file_size - 1
#         length = last_byte - first_byte + 1
#         response.status_code = 206
#         response['Content-Range'] = f'bytes {first_byte}-{last_byte}/{file_size}'
#         response['Accept-Ranges'] = 'bytes'
#         response['Content-Length'] = str(length)

#         with open(video_path, 'rb') as video_file:
#             video_file.seek(first_byte)
#             response.write(video_file.read(length))
#     else:
#         response = StreamingHttpResponse(open(video_path, 'rb'), content_type=content_type)
#         response['Content-Length'] = str(file_size)

#     response['Content-Type'] = content_type
#     return response




from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Registration, Enrollment, UserVideoStatus, Blog

@login_required
def user_profile(request):
    user = request.user
    registration = get_object_or_404(Registration, user=user)
    enrollments = Enrollment.objects.filter(user=user)
    watched_videos = UserVideoStatus.objects.filter(user=user)
    purchased_blogs = Blog.objects.filter(purchase__user=user).distinct()
    password_form = PasswordChangeForm(user=user)

    # Badge and progress bar calculation
    total_spent = registration.total_spent
    current_tier = registration.tier
    badge_image = None
    if total_spent >= 15000:
        percentage_spent = 100
        badge_image = 'images/7.png'
    elif total_spent >= 10000:
        percentage_spent = 80 + ((total_spent - 10000) / 5000) * 20
        badge_image = 'images/5.png'
    elif total_spent >= 5000:
        percentage_spent = 60 + ((total_spent - 5000) / 5000) * 20
        badge_image = 'images/6.png'
    elif total_spent >= 2500:
        percentage_spent = 40 + ((total_spent - 2500) / 2500) * 20
        badge_image = 'images/4.png'
    elif total_spent >= 1001:
        percentage_spent = 20 + ((total_spent - 1001) / 1500) * 20
        badge_image = 'images/2.png'
    else:
        percentage_spent = (total_spent / 1000) * 20
        badge_image = 'images/1.png'

    # Handle profile image update separately
    if request.method == 'POST':
        if 'profile_image' in request.FILES:
            profile_image = request.FILES['profile_image']
            registration.profile_image = profile_image
            registration.save()
            messages.success(request, 'Profile image updated successfully.')
        elif 'phone' in request.POST:
            phone = request.POST.get('phone')
            registration.phone = phone
            registration.save()
            messages.success(request, 'Phone number updated successfully.')
        elif 'old_password' in request.POST:
            # Handle password change
            password_form = PasswordChangeForm(user=user, data=request.POST)
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, password_form.user)  # Keep the user logged in
                messages.success(request, 'Password updated successfully.')
            else:
                messages.error(request, 'Please correct the errors below.')

    context = {
        'user': user,
        'registration': registration,
        'enrollments': enrollments,
        'watched_videos': watched_videos,
        'password_form': password_form,
        'percentage_spent': percentage_spent,
        'total_spent': total_spent,
        'badge_image': badge_image,
        'current_tier': current_tier,
        'purchased_blogs': purchased_blogs,
    }

    return render(request, 'user_profile.html', context)


@login_required
def update_profile_image(request):
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        registration = get_object_or_404(Registration, user=request.user)
        if profile_image:
            registration.profile_image = profile_image
            registration.save()
    return redirect('user_profile')
@login_required
def update_profile_info(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        registration = get_object_or_404(Registration, user=request.user)
        registration.phone = phone
        registration.save()
    return redirect('user_profile')

@csrf_exempt
def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    token = default_token_generator.make_token(user)
                    print(token)
                    uid = urlsafe_base64_encode(force_bytes(user.pk))
                    print(uid)
                    password_reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
                    full_url = request.build_absolute_uri(password_reset_url)
                    print(full_url)
                    print(user.email)
                    subject = "Password Reset Requested"
                    message = render_to_string('password_reset_email.html', {
                        'user': user,
                        'reset_url': full_url,
                    })
                    send_email(subject, message, user.email)
                messages.success(request, "A password reset link has been sent to your email address.")
            else:
                messages.error(request, "No account found with this email.")
    else:
        form = PasswordResetRequestForm()
    return render(request, 'password_reset_request.html', {'form': form})
from django.contrib.auth.forms import SetPasswordForm

def password_reset_confirm(request, uidb64=None, token=None):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your password has been set. You can now log in.')
                return redirect('login')
        else:
            form = SetPasswordForm(user)
    else:
        messages.error(request, 'The password reset link is invalid or has expired.')
        return redirect('password_reset')

    return render(request, 'password_reset_confirm.html', {'form': form})


# @login_required
# def support_request(request):
#     if request.method == 'POST':
#         form = SupportRequestForm(request.POST)
#         if form.is_valid():
#             support_request = form.save(commit=False)
#             support_request.user = request.user
#             support_request.save()
#             messages.success(request, 'Your support request has been submitted successfully.')
#             return redirect('support_request')
#     else:
#         form = SupportRequestForm()

#     return render(request, 'support_request.html', {'form': form})
# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SupportRequestForm
from .models import SupportRequest

def support_request(request):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    if request.method == 'POST':
        form = SupportRequestForm(request.POST, user=request.user)
        if form.is_valid():
            support_request = form.save(commit=False)
            if request.user.is_authenticated:
                support_request.user = request.user
                # Set name and email from the user
                support_request.name = f"{request.user.first_name} {request.user.last_name}"
                support_request.email = request.user.email
            support_request.save()
            messages.success(request, 'Your support request has been submitted successfully.')
            return redirect('support_request')
    else:
        form = SupportRequestForm(user=request.user)

    return render(request, 'support_request.html', {'form': form,'registration': registration,})

from django.shortcuts import render

def privacy_policy(request):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    return render(request, 'privacy_policy.html',{'registration': registration,})
from django.shortcuts import render

def terms_conditions(request):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    return render(request, 'terms_conditions.html',{'registration': registration,})
from django.shortcuts import render

# Other views...

def refund_policy(request):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    return render(request, 'refund_policy.html',{'registration':registration})
@login_required
def information_form(request):
    registration = request.user.registration
    if not registration.membership_paid:
        return redirect('membership_payment')

    if request.method == "POST":
        form = InformationForm(request.POST, request.FILES, instance=request.user.registration)
        if form.is_valid():
            form.save()
            return redirect('champions_dashboard')
    else:
        form = InformationForm(instance=registration)

    return render(request, 'information_form.html', {'form': form})
from django.shortcuts import render, get_object_or_404
from .models import Blog

# def blog_list(request):
#     blogs = Blog.objects.all().order_by('-created_at')
#     print(blogs)
#     return render(request, 'blog_list.html', {'blogs': blogs})

# def blog_detail(request, slug):
#     blog = get_object_or_404(Blog, slug=slug)
#     return render(request, 'blog_detail.html', {'blog': blog})
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog, Purchase
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def blog_list(request):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    blogs = Blog.objects.all().order_by('-created_at')

    # Get distinct categories for the filter
    categories = Blog.objects.values_list('category', flat=True).distinct()

    # Get search query and category filter from GET parameters
    search_query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')

    # Filter by search query
    if search_query:
        blogs = blogs.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))

    # Filter by category
    if category_filter:
        blogs = blogs.filter(category=category_filter)

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(blogs, 10)  # Show 10 blogs per page

    try:
        blogs_page = paginator.page(page)
    except PageNotAnInteger:
        blogs_page = paginator.page(1)
    except EmptyPage:
        blogs_page = paginator.page(paginator.num_pages)

    # Get user's purchased blogs
    purchased_blog_ids = []
    if request.user.is_authenticated:
        purchased_blog_ids = list(Purchase.objects.filter(user=request.user).values_list('blog_id', flat=True))

    context = {
        'blogs': blogs_page,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter,
        'purchased_blog_ids': purchased_blog_ids,
        'registration': registration,
    }
    return render(request, 'blog_list.html', context)
def blog_detail(request, slug):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    blog = get_object_or_404(Blog, slug=slug)
    is_purchased = False

    if blog.is_paid:
        if request.user.is_authenticated:
            # Check if the user has purchased the blog
            is_purchased = Purchase.objects.filter(user=request.user, blog=blog).exists()
        else:
            is_purchased = False

    context = {
        'blog': blog,
        'is_purchased': is_purchased,
        'registration': registration,
    }

    return render(request, 'blog_detail.html', context)

@login_required
def purchase_blog(request, slug):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    blog = get_object_or_404(Blog, slug=slug)

    if not blog.is_paid:
        messages.info(request, "This blog is free.")
        return redirect('blog_detail', slug=slug)

    if Purchase.objects.filter(user=request.user, blog=blog).exists():
        messages.info(request, "You have already purchased this blog.")
        return redirect('blog_detail', slug=slug)
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    razorpay_order = client.order.create({
        'amount': int(blog.price * 100),  # Convert to paise (smallest currency unit, assuming INR)
        'currency': 'USD',  # or 'USD' if your Razorpay account supports it
        'payment_capture': '1',  # Auto capture the payment
        'notes': {
            'user_id': str(request.user.id),  # Include user_id in metadata
            'blog_slug': str(blog.slug)
        }
    })
    print(razorpay_order)
    context = {
        'blog': blog,
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'amount': int(blog.price * 100),
        'currency': 'USD',
        'current_year': timezone.now().year,
        'registration': registration,
  # or 'USD'
    }
    print(context)
    # Create Razorpay client
    # client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    # # Create an order
    # order_amount = int(blog.price * 100)  # Convert to paise
    # order_currency = 'USD'
    # order_receipt = f'order_rcptid_{request.user.id}_{blog.id}'

    # razorpay_order = client.order.create({
    #     'amount': order_amount,
    #     'currency': order_currency,
    #     'receipt': order_receipt,
    #     'payment_capture': '1'
    # })

    # # Pass the order details to the template
    # context = {
    #     'blog': blog,
    #     'order_id': razorpay_order['id'],
    #     'razorpay_key_id': settings.RAZORPAY_KEY_ID,
    #     'amount': order_amount,
    #     'currency': order_currency,
    #     'callback_url': request.build_absolute_uri('/payment_handler/'),
    # }

    return render(request, 'purchase_blog.html', context)

@csrf_exempt
def payment_handler_blog(request):
    # Only accept POST requests
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')

        # Verify the payment and signature with Razorpay
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }
        print(params_dict)
        try:
            client.utility.verify_payment_signature(params_dict)


            # Retrieve the order details to get user_id and video_id
            order_details = client.order.fetch(order_id)
            user_id = order_details['notes']['user_id']
            blog_slug = order_details['notes']['blog_slug']
            payment_amount = order_details['amount'] / 100
            # Log the user back in
            user = User.objects.get(id=user_id)
            auth_login(request, user)
            blog = Blog.objects.get(slug=blog_slug)
            Purchase.objects.create(user=user, blog=blog)
            # Update the user's video status to paid and redirect to the video play page
            messages.success(request, "Payment successful! You can now read the full blog.")
            Transaction.objects.create(
                user=user,
                amount=payment_amount,
                description=f"payment for {blog_slug}."
            )
            

            return redirect('blog_detail', slug=blog_slug)
        except razorpay.errors.SignatureVerificationError:
            return redirect('error_page')










from django.shortcuts import render
from .models import champ_testimonial

def hear_from_champions(request):
    champions = champ_testimonial.objects.filter(approved=True)
    return render(request, 'hear_from_champions.html', {'champions': champions})
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import razorpay
from .models import Donation
from django.utils import timezone
from django.contrib import messages
from django.conf import settings
import razorpay
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Donation
from django.utils import timezone
from django.contrib import messages

# Donation view (this will generate a Razorpay order for donations)
# def donate(request):
#     razorpay_key_id = settings.RAZORPAY_KEY_ID
    
#     if request.method == "POST":
#         amount = float(request.POST['amount']) * 100  # Razorpay takes amount in the smallest unit (cents)
        
#         client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        
#         # Collect name and email based on whether the user is authenticated or not
#         if request.user.is_authenticated:
#             razorpay_order = client.order.create({
#             'amount': int(amount),
#             'currency': 'USD',  # Assuming you want donations in USD
#             'payment_capture': '1', 
#              'notes': {
#             'user_id': str(request.user.id),
            
#         } 
#         })
#             name = f"{request.user.first_name} {request.user.last_name}"

#             email = request.user.email
#         else:
            
#             name = request.POST['name']
#             email = request.POST['email']
#             razorpay_order = client.order.create({
#             'amount': int(amount),
#             'currency': 'USD',  # Assuming you want donations in USD
#             'payment_capture': '1', 
#             'notes': {
#             'user_id': None,
#             'name':name,
#             'email':email
            
#         } 
#         })

        
#         context = {
#             'razorpay_order_id': razorpay_order['id'],
#             'razorpay_key_id': razorpay_key_id,
#             'amount': amount / 100,  # Convert back to dollars for display
#             'currency': 'USD',
#             'name': name,
#             'email': email,

#         }
#         return render(request, 'donate_payment.html', context)

#     return render(request, 'donate.html', {'RAZORPAY_KEY_ID': razorpay_key_id})

import razorpay
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from razorpay.errors import BadRequestError

def donate(request):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    razorpay_key_id = settings.RAZORPAY_KEY_ID
    
    if request.method == "POST":
        # Convert amount to the smallest unit for Razorpay (e.g., cents or paise)
        amount = float(request.POST['amount']) * 100  # Razorpay requires smallest unit
        
        # Initialize Razorpay client
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        try:
            # If the user is authenticated, create an order with their info
            if request.user.is_authenticated:
                name = f"{request.user.first_name} {request.user.last_name}"
                email = request.user.email

                razorpay_order = client.order.create({
                    'amount': int(amount),
                    'currency': 'USD',  # Change to your currency if needed
                    'payment_capture': '1',
                    'notes': {
                        'user_id': str(request.user.id),
                    }
                })

            # If the user is not authenticated, create an order using the name and email they provided
            else:
                name = request.POST['name']
                email = request.POST['email']

                razorpay_order = client.order.create({
                    'amount': int(amount),
                    'currency': 'USD',  # Change to your currency if needed
                    'payment_capture': '1',
                    'notes': {
                        'user_id': None,
                        'name': name,
                        'email': email
                    }
                })

            # Prepare context for payment page
            context = {
                'razorpay_order_id': razorpay_order['id'],
                'razorpay_key_id': razorpay_key_id,
                'amount': amount / 100,  # Convert back to dollars for display
                'currency': 'USD',
                'name': name,
                'email': email,
            }

            return render(request, 'donate_payment.html', context)

        # Handle the case where the donation amount exceeds Razorpay's limit
        except BadRequestError as e:
            if "Amount exceeds maximum amount allowed" in str(e):
                messages.warning(request, 'The donation amount exceeds the maximum limit allowed by Razorpay. Please proceed with the exceptional donation form.')
                return redirect('exceptional_donation')  # Redirect to the exceptional donation form
            else:
                # Handle any other Razorpay errors
                messages.error(request, 'There was an issue processing your donation. Please try again.')
                return redirect('donate')

    # Render the normal donation page if the request is GET
    return render(request, 'donate.html', {'RAZORPAY_KEY_ID': razorpay_key_id,'registration': registration,})

@csrf_exempt
def razorpay_donation_callback(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')

        # Verify the payment and signature with Razorpay
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        try:
            client.utility.verify_payment_signature(params_dict)
            order_details = client.order.fetch(order_id)
            user_id = order_details['notes']['user_id']
            
            payment_amount = order_details['amount'] / 100
            # Log the user back in
            if user_id!=None:
                user = User.objects.get(id=user_id)
                auth_login(request, user)
            # Payment was successful, create the enrollment
                Transaction.objects.create(
                user=user,
                amount=payment_amount,
                description=f"Donation payment."
                )
                name = f"{request.user.first_name} {request.user.last_name}"

                email = request.user.email
            # If verification is successful, store the donation
            else:
                name = order_details['notes']['name']
                email = order_details['notes']['email']
            
            
            
            Donation.objects.create(
                user=request.user if request.user.is_authenticated else None,
                name=name,
                email=email,
                amount=payment_amount,
                payment_id=payment_id,
                order_id=order_id,
                created_at=timezone.now()
            )


            # Redirect to the thank you page after successful donation
            return redirect('thank_you')

        except razorpay.errors.SignatureVerificationError:
            messages.error(request, "Payment verification failed. Please contact support.")
            return redirect('donate')

    return redirect('donate')


def thank_you(request):
    return render(request, 'thank_you.html')
def membership_portal(request):
    return render(request,'membership_portal.html')
from django.shortcuts import render, redirect
from .forms import PartnerRegistrationForm

def register_partner(request):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    if request.method == 'POST':
        form = PartnerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you_partner')  # Redirect to a thank-you page after successful registration
    else:
        form = PartnerRegistrationForm()
    
    return render(request, 'register_partner.html', {'form': form,'registration': registration,})
    
def thank_you_partner(request):
    return render(request, 'thank_you_partner.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ExceptionalDonationForm

def exceptional_donation(request):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    if request.method == 'POST':
        form = ExceptionalDonationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your interest in donating. Our team will contact you soon.')
            return redirect('thank_you_exc')  # Redirect to a thank you page after submission
    else:
        form = ExceptionalDonationForm()

    return render(request, 'exceptional_donation.html', {'form': form,'registration': registration,})
def thank_you_exc(request):
    return render(request, 'thank_you_exc.html')



from django.shortcuts import render
from .models import JobPost, JobCategory

def careers_home(request):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    categories = JobCategory.objects.all()
    featured_jobs = JobPost.objects.filter(is_active=True)[:5]
    context = {
        'categories': categories,
        'featured_jobs': featured_jobs,
        'registration': registration,
         
    }
    return render(request, 'career_home.html', context)
# careers/views.py

from django.core.paginator import Paginator

def job_list(request):
    jobs = JobPost.objects.filter(is_active=True)
    categories = JobCategory.objects.all()
    employment_types = dict(EMPLOYMENT_TYPE_CHOICES)
    locations = JobPost.objects.values_list('location', flat=True).distinct()

    # Filters
    category_slug = request.GET.get('category')
    location = request.GET.get('location')
    employment_type = request.GET.get('employment_type')
    search_query = request.GET.get('search')

    if category_slug:
        jobs = jobs.filter(category__slug=category_slug)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if employment_type:
        jobs = jobs.filter(employment_type=employment_type)
    if search_query:
        jobs = jobs.filter(title__icontains=search_query)

    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'jobs': page_obj,
        'categories': categories,
        'employment_types': employment_types,
        'locations': locations,
    }
    return render(request, 'job_list.html', context)

# careers/views.py

from django.shortcuts import get_object_or_404

def job_detail(request, slug):
    job = get_object_or_404(JobPost, slug=slug, is_active=True)
    context = {
        'job': job,
    }
    return render(request, 'job_detail.html', context)

# careers/views.py

from .forms import JobApplicationForm
from django.shortcuts import redirect
from django.contrib import messages

def job_apply(request, slug):

    job = get_object_or_404(JobPost, slug=slug, is_active=True)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            messages.success(request, 'Your application has been submitted.')
            return redirect('job_detail', slug=job.slug)
    else:
        form = JobApplicationForm()
    context = {
        'job': job,
        'form': form,
    }
    return render(request, 'job_apply.html', context)
def about_us(request):
    registration = None
    if request.user.is_authenticated:
        registration = request.user.registration
    return render(request,'about_us.html',{'registration': registration})

from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Reel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# class ReelListView(ListView):
#     model = Reel

#     template_name = 'reel_list.html'
#     context_object_name = 'reels'
#     paginate_by = 10  # Number of reels to load per page

# def load_more_reels(request):
#     page = request.GET.get('page')
#     reels = Reel.objects.all().order_by('-created_at')
#     paginator = Paginator(reels, 10)
    
#     try:
#         reels_page = paginator.page(page)
#     except PageNotAnInteger:
#         reels_page = paginator.page(1)
#     except EmptyPage:
#         reels_page = []

#     reels_data = []
#     for reel in reels_page:
#         video_url = reel.compressed_video.url if reel.is_compressed and reel.compressed_video else reel.video.url
#         reels_data.append({
#             'id': reel.id,
#             'title': reel.title,
#             'video_url': video_url,
#             'thumbnail_url': reel.thumbnail.url if reel.thumbnail else '',
#         })

#     return JsonResponse({'reels': reels_data})
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render

from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Reel, ReelCategory

from django.db.models import Prefetch
from django.db.models import Prefetch

from django.shortcuts import render
from django.db.models import Prefetch
from .models import Reel, ReelCategory

def reel_grid_view(request):
    category_id = request.GET.get('category')

    if category_id:
        # If a specific category is selected, get the reels for that category
        reels_list = Reel.objects.filter(category_id=category_id,is_hidden=False).order_by('-created_at')
        categories = ReelCategory.objects.all()  # To display categories in the filter
    else:
        # If no category is selected, get all categories with their reels
        categories = ReelCategory.objects.prefetch_related(
            Prefetch('reels', queryset=Reel.objects.filter(is_hidden=False).order_by('-created_at'))
        )
        reels_list = None  # No specific list because we're displaying by category

    context = {
        'categories': categories,
        'reels': reels_list,  # Will be None when showing all categories
        'selected_category': category_id,
    }

    return render(request, 'reel_grid.html', context)


from django.http import JsonResponse

def load_more_reels(request):
    page = request.GET.get('page')
    category_id = request.GET.get('category', None)
    
    if category_id:
        reels_list = Reel.objects.filter(reel_category_id=category_id,is_hidden=False).order_by('-created_at')
    else:
        reels_list = Reel.objects.filter(is_hidden=False).order_by('-created_at')
        
    paginator = Paginator(reels_list, 10)
    
    try:
        reels_page = paginator.page(page)
    except PageNotAnInteger:
        reels_page = paginator.page(1)
    except EmptyPage:
        return JsonResponse({'reels': []})

    reels_data = []
    for reel in reels_page:
        video_url = reel.compressed_video.url if reel.is_compressed and reel.compressed_video else reel.video.url
        reels_data.append({
            'id': reel.id,
            'title': reel.title,
            'video_url': video_url,
            'thumbnail_url': reel.thumbnail.url if reel.thumbnail else '/static/images/default-thumbnail.jpg',
            'created_at': reel.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        })

    return JsonResponse({'reels': reels_data})
from django.shortcuts import render, get_object_or_404
from .models import Reel
from django.core.paginator import Paginator

def reel_shorts_view(request, reel_id=None):
    # Get all reels ordered by creation date and convert to a list
    reels_list = list(Reel.objects.order_by('-created_at'))
    
    selected_reel = None
    if reel_id:
        selected_reel = get_object_or_404(Reel, id=reel_id)
        # Move selected reel to the front if it exists
        if selected_reel in reels_list:
            reels_list.remove(selected_reel)
        else:
            # If the selected reel is not in the list, add it
            reels_list.insert(0, selected_reel)
        reels_list.insert(0, selected_reel)

    # Paginate the reels (e.g., 10 reels per page)
    paginator = Paginator(reels_list, 10)  # 10 reels per page
    page = request.GET.get('page', 1)
    reels = paginator.get_page(page)

    context = {
        'selected_reel': selected_reel,
        'reels': reels,
    }
    return render(request, 'reel_shorts.html', context)


# yourapp/views.py

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import NewsArticle

def news_feed(request):
    article_list = NewsArticle.objects.all()
    paginator = Paginator(article_list, 10)  # Show 10 articles per page

    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    return render(request, 'news_feed.html', {'articles': articles})
def tcc_academia_view(request):
    try:
        registration = request.user.registration
    except AttributeError:
        registration = None
        
    
    

    context = {
        
        'registration': registration,
        # Pass the courses to the context
    }
    return render(request, 'TCCACA.html',context)

def course_soon(request):

    return render(request,'courses_coming_soon.html')


def coming_soon_page(request):
    try:
        registration = request.user.registration
    except AttributeError:
        registration = None
        
    
    

    context = {
        
        'registration': registration,
        # Pass the courses to the context
    }
    return render(request,'coming_soon.html',context)
def credits(request):
    try:
        registration = request.user.registration
    except AttributeError:
        registration = None
        
    
    

    context = {
        
        'registration': registration,
        # Pass the courses to the context
    }
    return render(request,'credits_assets.html',context)
def epulum(request):
    try:
        registration = request.user.registration
    except AttributeError:
        registration = None
        
    
    

    context = {
        
        'registration': registration,
        # Pass the courses to the context
    }
    return render(request,'epulum.html',context)
def historia(request):
    try:
        registration = request.user.registration
    except AttributeError:
        registration = None
        
    
    

    context = {
        
        'registration': registration,
        # Pass the courses to the context
    }
    return render(request,'historia.html',context)
def vita(request):
    try:
        registration = request.user.registration
    except AttributeError:
        registration = None
        
    
    

    context = {
        
        'registration': registration,
        # Pass the courses to the context
    }
    return render(request,'vita.html',context)
def opus(request):
    try:
        registration = request.user.registration
    except AttributeError:
        registration = None
        
    
    

    context = {
        
        'registration': registration,
        # Pass the courses to the context
    }
    return render(request,'opus.html',context)
def tcc_resources(request):
    try:
        registration = request.user.registration
    except AttributeError:
        registration = None
        
    
    

    context = {
        
        'registration': registration,
        # Pass the courses to the context
    }
    return render(request,'TCC_resources.html',context)
def underreview(request):
    try:
        registration = request.user.registration
    except AttributeError:
        registration = None
        
    
    

    context = {
        
        'registration': registration,
        # Pass the courses to the context
    }
    return render(request,'underreview.html',context)

def associate_membership(request):
    try:
        registration = request.user.registration
    except AttributeError:
        registration = None
        
    
    

    context = {
        
        'registration': registration,
        # Pass the courses to the context
    }
    return render(request,'associate_membership.html',context)

from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def background_music(request):
    return render(request, 'background_music.html')
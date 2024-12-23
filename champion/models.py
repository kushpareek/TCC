from datetime import timedelta, timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from jsonschema import ValidationError
# from .utils import send_email
from .email_utils import send_email
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
class Registration(models.Model):
    APPROVAL_STATUS = (
        (0, 'Pending'),
        (1, 'Approved'),
        (2, 'Rejected'),
    )
    TIER_CHOICES = [
        ('Bronze', 'Bronze'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
        ('Titanium','Titanium'),
        ('Emerald','Emerald'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    day = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    joined_as = models.BooleanField(default=True)
    champion_reason = models.TextField()
    achievements = models.TextField()
    unique_trait = models.TextField()
    approved = models.PositiveSmallIntegerField(choices=APPROVAL_STATUS, default=0)
    verification_token = models.CharField(max_length=255, blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    submission_date = models.DateTimeField(auto_now_add=True)
    discord_id = models.CharField(max_length=50, blank=True, null=True)
    telegram_username = models.CharField(max_length=50, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    membership_paid = models.BooleanField(default=False)
    paid_on = models.DateTimeField(blank=True, null=True)
    personality_traits = models.CharField(max_length=500, blank=True, null=True)
    skills = models.CharField(max_length=500, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    motivations = models.TextField(blank=True, null=True)
    goals = models.TextField(blank=True, null=True)  # New field
    bio = models.TextField(blank=True, null=True)
    deactivated_at = models.DateTimeField(blank=True, null=True)  # New field to track deactivation date
    address_line_1 = models.CharField(max_length=255, blank=True, null=True)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tier = models.CharField(max_length=10, choices=TIER_CHOICES, default='Bronze')
    def is_deactivation_pending(self):
        if self.deactivated_at:
            return timezone.now() < self.deactivated_at + timedelta(days=90)
        return False
    def generate_verification_token(self):
        self.verification_token = default_token_generator.make_token(self.user)
        self.save()
    def update_tier(self):
        if self.total_spent >=15000:
            self.tier = 'Emerald'
        elif self.total_spent >=10000:
            self.tier='Titanium'
        elif self.total_spent >= 5000:
            self.tier = 'Platinum'
        elif self.total_spent >= 2500:
            self.tier = 'Gold'
        elif self.total_spent >= 1001:
            self.tier = 'Silver'
        else:
            self.tier = 'Bronze'
        self.save()
    def send_verification_email(self, request):
        subject = "Welcome to The Champions Club"
        verification_url = self.get_verification_url(request)

    # HTML email content with escaped curly braces
        html_message = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome to The Global Elite Circle – Verify Your Membership</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: 'Montserrat', sans-serif;
            background-color: #000;
            color: #333;
            margin: 0;
            padding: 20px;
        }}
        .email-container {{
            background-color: #000;
            padding: 20px;
            border-radius: 8px;
            max-width: 600px;
            margin: auto;
        }}
        .email-header {{
            text-align: center;
            background-color: #333;
            padding: 20px;
            color: #ffffff;
            border-radius: 8px 8px 0 0;
        }}
        .email-header h1 {{
            font-size: 24px;
            margin: 0;
        }}
        .email-body {{
            padding: 20px;
            background-color: #fff;
            color: #333;
        }}
        .email-body h2 {{
            color: #ffcc00;
            margin-top: 0;
        }}
        .email-body p {{
            line-height: 1.6;
            font-size: 16px;
        }}
        .email-list {{
            margin: 20px 0;
        }}
        .email-list ul {{
            list-style-type: disc;
            padding-left: 20px;
        }}
        .email-button {{
            text-align: center;
            margin-top: 20px;
        }}
        .email-button a {{
            background-color: #ffcc00;
            color: #000;
            padding: 12px 20px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 18px;
            font-weight: bold;
        }}
        .email-footer {{
            text-align: center;
            padding: 20px;
            background-color: #333;
            color: #fff;
            border-radius: 0 0 8px 8px;
        }}
        .email-footer p {{
            margin: 0;
            font-size: 14px;
        }}
        .email-signature {{
            margin-top: 40px;
        }}
        a {{
            color: #ffcc00;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <div class="email-header">
            <h1>Welcome to The Champions Club</h1>
        </div>
        <div class="email-body">
            <h2>Dear {self.user.first_name},</h2>
            <p>
                We are honored to extend a personal invitation to you to join <strong>The Champions Club</strong>, an exclusive, invitation-only network uniting the world's most influential and accomplished individuals.
            </p>
            <p>
                Your interest in our distinguished community has been received with great enthusiasm. As a prospective member, you are poised to access unparalleled opportunities to connect with visionary leaders, engage in transformative experiences, and forge meaningful relationships that transcend borders and industries.
            </p>
            <p>
                To complete your membership activation, please verify your email address by clicking the button below:
            </p>
            <div class="email-button">
                <a href="{verification_url}">Verify Your Membership</a>
            </div>
            <p>
                As a member of The Champions Club, you will enjoy privileges that are simply unattainable elsewhere:
            </p>
            <div class="email-list">
                <ul>
                    <li><strong>Exclusive Events:</strong> Gain access to private gatherings, symposiums, and galas featuring thought leaders and luminaries across various fields.</li>
                    <li><strong>Global Connections:</strong> Network with a curated group of peers who share your level of success and sophistication.</li>
                    <li><strong>Bespoke Opportunities:</strong> Receive personalized invitations to unique experiences tailored to your interests and aspirations.</li>
                </ul>
            </div>
            <p>
                We believe your exceptional achievements and discerning perspective will greatly enrich our community. We look forward to welcoming you into our circle of excellence.
            </p>
            <p class="email-signature">
                Warmest regards,<br><br>
                Shagun Kalash<br>
                <br>
                Founder & CEO.                
                The Champions Club
            </p>
        </div>
        <div class="email-footer">
            <p>
                Should you have any questions or require assistance, please contact our dedicated membership concierge at <a href="mailto:support@thechampionsclub.com">support@thechampionsclub.com</a>.
            </p>
            <p style="margin-top: 20px; font-size: 12px;">
                *This email and any attachments are confidential and intended solely for the use of the individual or entity to whom they are addressed.*
            </p>
        </div>
    </div>
</body>
</html>
"""
        send_email(
        subject=subject,
        body=html_message,
        to_email=self.user.email,
        from_email=settings.DEFAULT_FROM_EMAIL  # Ensure this is a verified sender in Brevo
    )

    def get_verification_url(self, request):
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = self.verification_token
        relative_url = reverse('verify_email', kwargs={'uidb64': uid, 'token': token})
        absolute_url = request.build_absolute_uri(relative_url)
        return absolute_url

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.username})"
from django.db import models
from django.contrib.auth.models import User

from django.db import models

from django.db import models

from django.db import models

class VideoCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='podcasts/')
    preview_file = models.FileField(upload_to='podcasts/previews/')
    thumbnail = models.ImageField(upload_to='podcasts/thumbnails/', blank=True, null=True)
    duration = models.DurationField()  # Total duration of the video
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    videocategory = models.ForeignKey(VideoCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='videos')  # Changed to VideoCategory

    def __str__(self):
        return self.title



class UserVideoStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    last_watched_time = models.DurationField(default=0)  # Last watched position in the video
    has_paid = models.BooleanField(default=False)
    has_completed = models.BooleanField(default=False)  # Track if the user has completed the video

    def __str__(self):
        return f'{self.user.username} - {self.video.title}'
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
from decimal import Decimal

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Ensure the amount is a Decimal before adding it
        self.amount = Decimal(self.amount)
        registration = self.user.registration
        if registration.total_spent is None:
            registration.total_spent = Decimal(0)
        registration.update_tier()
        registration.total_spent += self.amount
        registration.save()
        super().save(*args, **kwargs)

from django.db import models
from django.contrib.auth.models import User

class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation of {self.amount} by {self.name} ({self.email})"

class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='course_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=255)
    order = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class Lesson(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='lesson_videos/')
    order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    transcript = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class Quiz(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['order']

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Review(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 stars
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.lesson.title}'

# models.py
# models.py
class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.video.title if self.video else "No Video"}'



from django.db import models
from django.contrib.auth.models import User

class QuizResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - {self.question.text}"

    class Meta:
        unique_together = ('user', 'quiz', 'question')

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"
from django.db import models
from django.contrib.auth.models import User
# models.py
from django.db import models
from django.contrib.auth.models import User

class SupportRequest(models.Model):
    CATEGORY_CHOICES = [
        ('billing', 'Billing'),
        ('technical', 'Technical Support'),
        ('general', 'General Inquiry'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_requests', null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Open')

    def __str__(self):
        if self.user:
            return f"{self.subject} - {self.user.username}"
        else:
            return f"{self.subject} - {self.email or 'Anonymous'}"

from django.db import models

from django.db import models
from django.utils import timezone
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # Discount as a percentage
    is_active = models.BooleanField(default=True)
    expiration_date = models.DateTimeField(null=True, blank=True)  # Optional expiration date

    def __str__(self):
        return self.code

    def is_valid(self):
        if not self.is_active:
            return False
        if self.expiration_date and self.expiration_date < timezone.now():
            return False
        return True
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField  # Use this if you're using CKEditor

from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField  # Import RichTextField

from django.core.exceptions import ValidationError

class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    content = RichTextField()  # Use RichTextField for rich text editing
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def clean(self):
        if self.is_paid and not self.price:
            raise ValidationError('Price must be set for paid blogs.')
        if not self.is_paid:
            self.price = None  # Ensure price is None for free blogs

    def __str__(self):
        return self.title
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} purchased {self.blog.title}"

from django.db import models
from django.contrib.auth.models import User

class champ_testimonial(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='champions_images/')
    designation = models.CharField(max_length=255)
    testimonial = models.TextField()
    approved = models.BooleanField(default=False)  # Admin approval for display

    def __str__(self):
        return self.user.username
from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.name}"
    

from django.db import models

class ExceptionalDonation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)  # Optional
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # For capturing the exceptional amount
    submitted_at = models.DateTimeField(auto_now_add=True)  # Automatically adds the timestamp when submitted

    def __str__(self):
        return f"Exceptional Donation by {self.name} - {self.amount} USD"



# careers/models.py

from django.db import models
from django.utils.text import slugify

class JobCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Job Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
# careers/models.py

from django.db import models
from django.utils.text import slugify
from django.utils import timezone

EMPLOYMENT_TYPE_CHOICES = [
    ('FT', 'Full-time'),
    ('PT', 'Part-time'),
    ('CT', 'Contract'),
    ('IN', 'Internship'),
]

class JobPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, related_name='jobs')
    location = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=2, choices=EMPLOYMENT_TYPE_CHOICES)
    description = models.TextField()
    responsibilities = models.TextField()
    qualifications = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)
    application_deadline = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-posted_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
# careers/models.py

from django.db import models

class JobApplication(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='applications')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True, null=True)
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job.title}"
from django.db import models

# class Reel(models.Model):
#     title = models.CharField(max_length=255)
#     video = models.FileField(upload_to='reels/')
#     thumbnail = models.ImageField(upload_to='reels/thumbnails/', null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
from django.db import models
from django.utils import timezone

class ReelCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Reel(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='reels/originals/')
    compressed_video = models.FileField(upload_to='reels/compressed/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='reels/thumbnails/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_compressed = models.BooleanField(default=False)
    compression_error = models.TextField(null=True, blank=True)
    visit_now_url = models.URLField(max_length=500, blank=True, null=True)
    show_visit_now_button = models.BooleanField(default=False)
    # Foreign key to ReelCategory
    is_hidden = models.BooleanField(default=False)
    category = models.ForeignKey(ReelCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='reels')

    def __str__(self):
        return self.title


from django.db import models
from django.core.validators import FileExtensionValidator

def validate_video(file):
    valid_extensions = ['mp4', 'mov', 'avi']
    if not file.name.split('.')[-1].lower() in valid_extensions:
        raise ValidationError('Unsupported video format.')

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=280)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    video = models.FileField(
        upload_to='news_videos/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi'])]
    )
    publish_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title
# models.py
from django.db import models
from django.contrib.auth.models import User

class VideoAccessToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"Token for {self.user.username} - {self.video.title}"

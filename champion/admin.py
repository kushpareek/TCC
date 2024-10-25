# champions/admin.py

from django.contrib import admin
from .models import Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'get_last_name', 'get_email', 'phone', 'get_username')

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.admin_order_field = 'user__first_name'  # Allows column order sorting
    get_first_name.short_description = 'First Name'  # Renames column head

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.admin_order_field = 'user__last_name'  # Allows column order sorting
    get_last_name.short_description = 'Last Name'  # Renames column head

    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field = 'user__email'  # Allows column order sorting
    get_email.short_description = 'Email'  # Renames column head

    def get_username(self, obj):
        return obj.user.username
    get_username.admin_order_field = 'user__username'  # Allows column order sorting
    get_username.short_description = 'Username'  # Renames column head

admin.site.register(Registration, RegistrationAdmin)
from django.contrib import admin
from .models import Video

from django.contrib import admin
from .models import Video, VideoCategory

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'videocategory', 'duration', 'price')
    search_fields = ('title', 'description')
    list_filter = ('videocategory',)  # Filter by VideoCategory

@admin.register(VideoCategory)
class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

from django.contrib import admin
from .models import Category, Course, Section, Lesson, Quiz, Question, Answer

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
from django.contrib import admin
from .models import Category, Course, Section, Lesson, Quiz, Question, Answer, Review, Comment

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'rating', 'created_at')
    search_fields = ('user__username', 'lesson__title')

# admin.py
from django.contrib import admin
from .models import Video, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'created_at', 'is_hidden')
    list_filter = ('is_hidden', 'created_at', 'video')
    search_fields = ('user__username', 'comment_text')
    actions = ['hide_comments', 'unhide_comments']

    def hide_comments(self, request, queryset):
        queryset.update(is_hidden=True)
    hide_comments.short_description = "Hide selected comments"

    def unhide_comments(self, request, queryset):
        queryset.update(is_hidden=False)
    unhide_comments.short_description = "Unhide selected comments"


admin.site.register(Comment, CommentAdmin)


from django.contrib import admin
from .models import Coupon
from .models import Blog

admin.site.register(Blog)
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'is_active', 'expiration_date')
    search_fields = ('code',)
    list_filter = ('is_active', 'expiration_date')
from django.contrib import admin
from .models import champ_testimonial

class ChampionAdmin(admin.ModelAdmin):
    list_display = ('user', 'designation', 'approved')
    search_fields = ('user__username', 'designation')
    list_filter = ('approved',)

admin.site.register(champ_testimonial, ChampionAdmin)

from django.contrib import admin
from .models import Partner

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'name', 'email', 'phone', 'registered_at')
    search_fields = ('company_name', 'name', 'email')
# careers/admin.py

from django.contrib import admin
from .models import JobCategory, JobPost, JobApplication

@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'employment_type', 'posted_date', 'is_active')
    list_filter = ('category', 'employment_type', 'is_active')
    search_fields = ('title', 'description', 'responsibilities', 'qualifications')

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'job', 'applied_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('job', 'applied_date')
from django.contrib import admin
from .models import Reel

# reels/admin.py

from django.contrib import admin
from .models import Reel
 # Ensure this import is correct

# reels/admin.py

from django.contrib import admin
from .models import Reel
  # Ensure this import is correct
from django.contrib import admin
from .models import Reel, ReelCategory

from django.contrib import admin
from .models import Reel, ReelCategory

from django.contrib import admin
from .models import Reel

class ReelAdmin(admin.ModelAdmin):
    list_display = ['title',  'show_visit_now_button','is_hidden']
    list_filter = ['show_visit_now_button','is_hidden']
    search_fields = ['title']
    fields = ['title','category', 'video', 'compressed_video', 'thumbnail', 'visit_now_url', 'show_visit_now_button', 'is_hidden']

admin.site.register(Reel, ReelAdmin)

@admin.register(ReelCategory)
class ReelCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    fields = ('name',)


    # Remove the exclude line if present to avoid conflicts
    # exclude = ('is_compressed', 'compression_error')

    
# yourapp/admin.py

from django.contrib import admin
from .models import NewsArticle

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date')
    search_fields = ('title', 'content')
    list_filter = ('publish_date',)

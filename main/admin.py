"""
Django Admin configuration for Pavis Mugo Muruga Portfolio.
Full media management: image previews, inline screenshots, file uploads, and validation.
"""
from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteSettings, SocialLink, Skill, Experience, ExperienceProject,
    Education, Project, ProjectScreenshot, CurrentlyBuilding,
    Recommendation, Certification, GalleryImage,
    Achievement, BlogPost, Testimonial, ContactMessage, LearningTopic,
    Goal, TimelineEvent, PlaygroundExperiment
)


# ==============================================================================
# HELPER: Reusable image thumbnail renderer
# ==============================================================================

def image_preview_html(image_field, width=80, height=55):
    """Return a formatted image thumbnail for Django Admin list display."""
    if image_field:
        return format_html(
            '<img src="{}" style="width:{}px;height:{}px;object-fit:cover;'
            'border-radius:6px;border:1px solid #333;" alt="preview" />',
            image_field.url, width, height
        )
    return format_html('<span style="color:#666;font-size:12px;">No image</span>')


# ==============================================================================
# ADMIN SITE CUSTOMIZATION
# ==============================================================================

admin.site.site_header = 'Pavis Mugo Muruga — Portfolio Admin'
admin.site.site_title  = 'Portfolio Admin'
admin.site.index_title = 'Manage Your Portfolio Content'


# ==============================================================================
# SITE SETTINGS
# ==============================================================================

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Site Metadata', {
            'fields': ('site_name', 'site_title', 'site_description')
        }),
        ('Personal Information', {
            'fields': ('full_name', 'profession', 'location', 'bio')
        }),
        ('Hero Section', {
            'fields': ('hero_greeting', 'hero_title', 'hero_subtitle', 'hero_status')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'whatsapp_number')
        }),
        ('Social & External', {
            'fields': ('github_url', 'github_username', 'linkedin_url')
        }),
        ('Profile Photo', {
            'fields': ('profile_image', 'profile_image_preview'),
            'description': '✅ Allowed: JPG, JPEG, PNG, WEBP — Max file size: 3 MB',
        }),
        ('CV / Resume Document', {
            'fields': ('resume', 'resume_download_link'),
            'description': '✅ Allowed: PDF — Max file size: 10 MB',
        }),
        ('Open Graph / Social Sharing Image', {
            'fields': ('og_image', 'og_image_preview'),
            'description': '✅ Recommended size: 1200 × 630px — Max file size: 5 MB',
        }),
        ('Footer', {
            'fields': ('footer_tagline',)
        }),
        ('WhatsApp Button', {
            'fields': ('whatsapp_message',)
        }),
    )
    readonly_fields = ('profile_image_preview', 'og_image_preview', 'resume_download_link')

    def profile_image_preview(self, obj):
        return image_preview_html(obj.profile_image, 120, 120)
    profile_image_preview.short_description = 'Profile Photo Preview'

    def og_image_preview(self, obj):
        return image_preview_html(obj.og_image, 240, 126)
    og_image_preview.short_description = 'OG Image Preview'

    def resume_download_link(self, obj):
        if obj.resume:
            return format_html(
                '<a href="{}" target="_blank" rel="noopener noreferrer" '
                'style="padding:4px 12px;background:#0d6efd;color:#fff;border-radius:4px;text-decoration:none;">'
                '📄 Download / View CV</a>',
                obj.resume.url
            )
        return format_html('<span style="color:#888;">No CV uploaded yet</span>')
    resume_download_link.short_description = 'Current CV File'

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# ==============================================================================
# SOCIAL LINKS
# ==============================================================================

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter   = ('platform', 'is_active')
    ordering      = ('order',)


# ==============================================================================
# SKILLS
# ==============================================================================

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ('name', 'category', 'level', 'icon', 'order', 'is_active')
    list_editable = ('level', 'order', 'is_active')
    list_filter   = ('category', 'level', 'is_active')
    search_fields = ('name',)
    ordering      = ('category', 'order')


# ==============================================================================
# EXPERIENCE
# ==============================================================================

class ExperienceProjectInline(admin.TabularInline):
    model  = ExperienceProject
    extra  = 1
    fields = ('name', 'description', 'responsibilities', 'technologies', 'lessons', 'order')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display  = ('organization', 'role', 'duration', 'start_date', 'is_current', 'is_active', 'image_preview')
    list_filter   = ('is_current', 'is_active')
    search_fields = ('organization', 'role')
    inlines       = [ExperienceProjectInline]
    readonly_fields = ('image_preview',)
    fieldsets = (
        (None, {
            'fields': ('organization', 'role', 'duration', 'location', 'description')
        }),
        ('Experience Photo', {
            'fields': ('image', 'image_preview', 'alt_text'),
            'description': '✅ Allowed: JPG, PNG, WEBP — Max file size: 5 MB',
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Display', {
            'fields': ('order', 'is_active')
        }),
    )

    def image_preview(self, obj):
        return image_preview_html(obj.image, 120, 80)
    image_preview.short_description = 'Photo Preview'


# ==============================================================================
# EDUCATION
# ==============================================================================

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display  = ('institution', 'course', 'level', 'is_current', 'is_active')
    list_filter   = ('is_current', 'is_active')
    search_fields = ('institution', 'course')
    fieldsets = (
        (None, {
            'fields': ('institution', 'course', 'level', 'description')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Details', {
            'fields': ('relevant_areas', 'achievements')
        }),
        ('Display', {
            'fields': ('order', 'is_active')
        }),
    )


# ==============================================================================
# PROJECTS — with inline screenshot gallery
# ==============================================================================

class ProjectScreenshotInline(admin.TabularInline):
    model   = ProjectScreenshot
    extra   = 1
    fields  = ('image', 'caption', 'alt_text', 'order', 'screenshot_preview')
    readonly_fields = ('screenshot_preview',)

    def screenshot_preview(self, obj):
        return image_preview_html(obj.image, 100, 65)
    screenshot_preview.short_description = 'Preview'


@admin.register(ProjectScreenshot)
class ProjectScreenshotAdmin(admin.ModelAdmin):
    list_display  = ('project', 'caption', 'order', 'screenshot_preview')
    list_editable = ('order',)
    list_filter   = ('project',)
    readonly_fields = ('screenshot_preview',)

    def screenshot_preview(self, obj):
        return image_preview_html(obj.image, 100, 65)
    screenshot_preview.short_description = 'Preview'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('title', 'category', 'status', 'role', 'is_featured', 'is_active', 'order', 'cover_preview')
    list_editable = ('status', 'is_featured', 'is_active', 'order')
    list_filter   = ('status', 'category', 'is_featured', 'is_active')
    search_fields = ('title', 'short_description', 'technologies', 'role')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('cover_preview', 'ss1_preview', 'ss2_preview', 'ss3_preview')
    inlines = [ProjectScreenshotInline]
    fieldsets = (
        ('Project Info', {
            'fields': ('title', 'slug', 'role', 'status', 'short_description', 'category')
        }),
        ('Case Study Content', {
            'fields': ('overview', 'problem', 'solution', 'features',
                       'technologies', 'development_process', 'challenges',
                       'lessons_learned', 'results'),
            'classes': ('collapse',),
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Cover Image', {
            'fields': ('image', 'cover_preview'),
            'description': '✅ Allowed: JPG, PNG, WEBP — Max file size: 5 MB',
        }),
        ('Quick Screenshots (up to 3)', {
            'fields': (
                'screenshot_1', 'ss1_preview',
                'screenshot_2', 'ss2_preview',
                'screenshot_3', 'ss3_preview',
            ),
            'description': '✅ For more screenshots, use the Screenshots section below.',
            'classes': ('collapse',),
        }),
        ('Display', {
            'fields': ('is_featured', 'order', 'is_active')
        }),
    )

    def cover_preview(self, obj):
        return image_preview_html(obj.image, 180, 110)
    cover_preview.short_description = 'Cover Preview'

    def ss1_preview(self, obj):
        return image_preview_html(obj.screenshot_1, 120, 80)
    ss1_preview.short_description = 'Screenshot 1 Preview'

    def ss2_preview(self, obj):
        return image_preview_html(obj.screenshot_2, 120, 80)
    ss2_preview.short_description = 'Screenshot 2 Preview'

    def ss3_preview(self, obj):
        return image_preview_html(obj.screenshot_3, 120, 80)
    ss3_preview.short_description = 'Screenshot 3 Preview'


# ==============================================================================
# TECH PLAYGROUND
# ==============================================================================

@admin.register(PlaygroundExperiment)
class PlaygroundExperimentAdmin(admin.ModelAdmin):
    list_display  = ('title', 'status', 'technology', 'order', 'is_active')
    list_editable = ('status', 'order', 'is_active')
    list_filter   = ('status', 'is_active')
    search_fields = ('title', 'description', 'technology')
    prepopulated_fields = {'slug': ('title',)}


# ==============================================================================
# CURRENTLY BUILDING
# ==============================================================================

@admin.register(CurrentlyBuilding)
class CurrentlyBuildingAdmin(admin.ModelAdmin):
    list_display  = ('name', 'status', 'progress_percent', 'technologies', 'order', 'is_active')
    list_editable = ('status', 'progress_percent', 'order', 'is_active')
    list_filter   = ('status', 'is_active')
    search_fields = ('name', 'description', 'technologies')
    fieldsets = (
        (None, {
            'fields': ('name', 'status', 'progress_percent', 'description', 'technologies')
        }),
        ('Media & Links', {
            'fields': ('image', 'github_url', 'live_url')
        }),
        ('Display', {
            'fields': ('order', 'is_active')
        }),
    )


# ==============================================================================
# PROFESSIONAL RECOMMENDATION
# ==============================================================================

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display  = ('supervisor_name', 'supervisor_role', 'organization', 'recommendation_date', 'has_letter', 'letter_link', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter   = ('organization', 'is_active')
    search_fields = ('supervisor_name', 'organization', 'quote', 'highlights')
    readonly_fields = ('letter_download_link',)
    fieldsets = (
        ('Supervisor & Organization', {
            'fields': ('supervisor_name', 'supervisor_role', 'organization', 'organization_note')
        }),
        ('Dates & Timeline', {
            'fields': ('recommendation_date', 'attachment_duration')
        }),
        ('Commendations & Highlights', {
            'fields': ('quote', 'highlights')
        }),
        ('Recommendation Letter PDF', {
            'fields': ('recommendation_letter', 'letter_download_link'),
            'description': '✅ Allowed: PDF — Max file size: 10 MB',
        }),
        ('Display', {
            'fields': ('order', 'is_active')
        }),
    )

    def has_letter(self, obj):
        return bool(obj.recommendation_letter)
    has_letter.boolean = True
    has_letter.short_description = 'PDF Uploaded'

    def letter_link(self, obj):
        if obj.recommendation_letter:
            return format_html(
                '<a href="{}" target="_blank" rel="noopener noreferrer" '
                'style="padding:2px 8px;background:#198754;color:#fff;border-radius:4px;text-decoration:none;font-size:11px;">'
                '📄 View PDF</a>',
                obj.recommendation_letter.url
            )
        return '—'
    letter_link.short_description = 'Download Link'

    def letter_download_link(self, obj):
        if obj.recommendation_letter:
            return format_html(
                '<a href="{}" target="_blank" rel="noopener noreferrer" '
                'style="padding:4px 14px;background:#198754;color:#fff;border-radius:4px;text-decoration:none;">'
                '📄 Open Recommendation Letter PDF</a>',
                obj.recommendation_letter.url
            )
        return format_html('<span style="color:#888;">No PDF uploaded yet</span>')
    letter_download_link.short_description = 'Current Letter File'


# ==============================================================================
# CERTIFICATIONS
# ==============================================================================

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display  = ('name', 'organization', 'date', 'has_image', 'has_pdf', 'order', 'is_active', 'image_preview')
    list_editable = ('order', 'is_active')
    list_filter   = ('organization', 'is_active')
    search_fields = ('name', 'organization')
    ordering      = ('order', '-date')
    readonly_fields = ('image_preview', 'pdf_download_link')
    fieldsets = (
        ('Certificate Info', {
            'fields': ('name', 'organization', 'date', 'description', 'verification_url')
        }),
        ('Certificate Image', {
            'fields': ('image', 'image_preview', 'alt_text'),
            'description': '✅ Allowed: JPG, PNG, WEBP — Max file size: 5 MB',
        }),
        ('Certificate PDF Document', {
            'fields': ('certificate_pdf', 'pdf_download_link'),
            'description': '✅ Allowed: PDF — Max file size: 10 MB',
        }),
        ('Display', {
            'fields': ('order', 'is_active')
        }),
    )

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Image'

    def has_pdf(self, obj):
        return bool(obj.certificate_pdf)
    has_pdf.boolean = True
    has_pdf.short_description = 'PDF'

    def image_preview(self, obj):
        return image_preview_html(obj.image, 180, 120)
    image_preview.short_description = 'Certificate Preview'

    def pdf_download_link(self, obj):
        if obj.certificate_pdf:
            return format_html(
                '<a href="{}" target="_blank" rel="noopener noreferrer" '
                'style="padding:4px 14px;background:#0d6efd;color:#fff;border-radius:4px;text-decoration:none;">'
                '📄 Open Certificate PDF</a>',
                obj.certificate_pdf.url
            )
        return format_html('<span style="color:#888;">No PDF uploaded yet</span>')
    pdf_download_link.short_description = 'PDF File'


# ==============================================================================
# GALLERY IMAGES
# ==============================================================================

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display  = ('title_or_auto', 'category', 'is_featured', 'is_active', 'order', 'image_preview')
    list_editable = ('is_featured', 'is_active', 'order')
    list_filter   = ('category', 'is_featured', 'is_active')
    search_fields = ('title', 'caption', 'alt_text')
    readonly_fields = ('image_preview',)
    fieldsets = (
        ('Gallery Image', {
            'fields': ('image', 'image_preview', 'title', 'caption', 'alt_text'),
            'description': '✅ Allowed: JPG, PNG, WEBP — Max file size: 5 MB. '
                           'Always fill in alt_text with a descriptive description of the photo for accessibility.',
        }),
        ('Categorization', {
            'fields': ('category', 'is_featured')
        }),
        ('Display', {
            'fields': ('order', 'is_active')
        }),
    )

    def title_or_auto(self, obj):
        return obj.title or f'{obj.get_category_display()} photo'
    title_or_auto.short_description = 'Title'

    def image_preview(self, obj):
        return image_preview_html(obj.image, 160, 110)
    image_preview.short_description = 'Preview'


# ==============================================================================
# ACHIEVEMENTS
# ==============================================================================

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display  = ('title', 'category', 'date', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter   = ('category', 'is_active')
    search_fields = ('title', 'description')
    ordering      = ('order', '-date')


# ==============================================================================
# BLOG POSTS
# ==============================================================================

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'category', 'author', 'reading_time', 'published', 'featured', 'created_at', 'image_preview')
    list_editable = ('published', 'featured')
    list_filter   = ('published', 'featured', 'category', 'created_at')
    search_fields = ('title', 'content', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy  = 'created_at'
    readonly_fields = ('image_preview',)
    fieldsets = (
        ('Post Content', {
            'fields': ('title', 'slug', 'author', 'excerpt', 'content')
        }),
        ('Featured Image', {
            'fields': ('featured_image', 'image_preview', 'featured_image_alt'),
            'description': '✅ Allowed: JPG, PNG, WEBP — Max file size: 5 MB. '
                           'Fill in the alt text to describe the image.',
        }),
        ('Organization', {
            'fields': ('category', 'tags', 'reading_time')
        }),
        ('Publishing', {
            'fields': ('published', 'featured')
        }),
    )

    def image_preview(self, obj):
        return image_preview_html(obj.featured_image, 200, 120)
    image_preview.short_description = 'Featured Image Preview'


# ==============================================================================
# TESTIMONIALS
# ==============================================================================

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display  = ('name', 'position', 'organization', 'featured', 'is_active', 'order')
    list_editable = ('featured', 'is_active', 'order')
    list_filter   = ('featured', 'is_active')
    search_fields = ('name', 'organization', 'message')


# ==============================================================================
# CONTACT MESSAGES
# ==============================================================================

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display  = ('subject', 'name', 'email', 'is_read', 'created_at')
    list_editable = ('is_read',)
    list_filter   = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'created_at'
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'created_at')

    def has_add_permission(self, request):
        return False

    actions = ['mark_as_read', 'mark_as_unread']

    @admin.action(description='Mark selected messages as read')
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    @admin.action(description='Mark selected messages as unread')
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)


# ==============================================================================
# LEARNING TOPICS
# ==============================================================================

@admin.register(LearningTopic)
class LearningTopicAdmin(admin.ModelAdmin):
    list_display  = ('name', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)


# ==============================================================================
# GOALS
# ==============================================================================

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display  = ('title', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title',)


# ==============================================================================
# TIMELINE / MY JOURNEY
# ==============================================================================

@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display  = ('title', 'date', 'category', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter   = ('category', 'is_active')
    search_fields = ('title', 'description')
    ordering      = ('order',)

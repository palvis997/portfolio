"""
Django models for Pavis Mugo Muruga Portfolio.
All content is manageable through Django Admin.
"""
import math
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from .validators import validate_image_file, validate_document_file, validate_avatar_file


# ==============================================================================
# SITE SETTINGS (Singleton)
# ==============================================================================

class SiteSettings(models.Model):
    """
    Singleton model for site-wide settings.
    Manages all personal info, contact details, and site metadata from one place.
    """
    # Site metadata
    site_name = models.CharField(max_length=200, default='Pavis Mugo Muruga')
    site_title = models.CharField(
        max_length=200,
        default='Information Technology Student | Python & Django Developer | IT Support'
    )
    site_description = models.TextField(
        default='Pavis Mugo Muruga — Information Technology student at Kirinyaga University, '
                'Python & Django developer, and IT support professional with practical industry experience.'
    )

    # Personal info
    full_name = models.CharField(max_length=200, default='Pavis Mugo Muruga')
    profession = models.CharField(
        max_length=300,
        default='Information Technology Student | Python & Django Developer | IT Support'
    )
    location = models.CharField(max_length=200, default='Kenya')
    bio = models.TextField(
        blank=True,
        default='I am a dedicated Information Technology student at Kirinyaga University, '
                'currently in Year 2 pursuing a Bachelor of Science in Information Technology '
                '(Expected Graduation: 2028). I possess practical industry experience gained during '
                'a 13-week industrial attachment at the ICT Authority of Kenya, where I contributed to '
                'software systems in Python and Django, database workflows, and IT support services. '
                'I am passionate about clean code, continuous learning, and building practical technology solutions.'
    )

    # Hero section
    hero_greeting = models.CharField(max_length=200, default="Hi, I'm Pavis Mugo Muruga")
    hero_title = models.CharField(
        max_length=300,
        default='Information Technology Student | Python & Django Developer | IT Support'
    )
    hero_subtitle = models.TextField(
        default='Aspiring technology professional with hands-on industrial attachment experience at the '
                'ICT Authority of Kenya. Passionate about software development with Python & Django, database management, and IT infrastructure.'
    )
    hero_status = models.CharField(max_length=200, default='Available for opportunities & collaboration')

    # Contact info
    email = models.EmailField(blank=True, default='palvismugo06@gmail.com')
    phone = models.CharField(max_length=50, blank=True, default='0711652479')
    whatsapp_number = models.CharField(
        max_length=50, blank=True, default='254711652479',
        help_text='Include country code without +, e.g., 254XXXXXXXXX'
    )

    # Social / external
    github_url = models.URLField(blank=True, default='https://github.com/palvis997')
    github_username = models.CharField(max_length=100, blank=True, default='palvis997')
    linkedin_url = models.URLField(blank=True, default='')

    # Files & Media
    profile_image = models.ImageField(
        upload_to='profile/', blank=True, validators=[validate_avatar_file],
        help_text='Profile photo for Hero and About sections (JPG, PNG, WEBP max 3MB)'
    )
    resume = models.FileField(
        upload_to='resume/', blank=True, validators=[validate_document_file],
        help_text='Upload official CV/Resume (PDF max 10MB)'
    )
    og_image = models.ImageField(
        upload_to='og/', blank=True, validators=[validate_image_file],
        help_text='Open Graph image for social sharing (1200x630px recommended)'
    )

    # Footer
    footer_tagline = models.CharField(
        max_length=300,
        default='Building practical solutions. Learning continuously. Growing as a developer.'
    )

    # WhatsApp button
    whatsapp_message = models.CharField(
        max_length=500,
        default='Hello Pavis, I visited your portfolio and would like to connect with you.'
    )

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


# ==============================================================================
# SOCIAL LINKS
# ==============================================================================

class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('whatsapp', 'WhatsApp'),
        ('email', 'Email'),
        ('twitter', 'Twitter/X'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('youtube', 'YouTube'),
        ('other', 'Other'),
    ]

    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.CharField(max_length=500, help_text='Full URL, mailto:, tel:, or https://wa.me/ link')
    icon = models.CharField(
        max_length=100,
        help_text='Font Awesome class, e.g., fab fa-github'
    )
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.get_platform_display()


# ==============================================================================
# SKILLS
# ==============================================================================

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming'),
        ('framework', 'Frameworks'),
        ('database', 'Databases'),
        ('data', 'Data & Information Management'),
        ('tool', 'Tools'),
        ('it', 'IT & Systems'),
        ('other', 'Other Skills'),
    ]

    LEVEL_CHOICES = [
        ('learning', 'Learning'),
        ('intermediate', 'Intermediate'),
        ('proficient', 'Proficient'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, default='intermediate')
    icon = models.CharField(max_length=100, blank=True, help_text='Font Awesome class or icon class')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return f'{self.name} ({self.get_category_display()})'


# ==============================================================================
# EXPERIENCE
# ==============================================================================

class Experience(models.Model):
    organization = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100, help_text='e.g., 13 weeks (4 May 2026 – 31 July 2026)')
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    location = models.CharField(max_length=200, blank=True)
    image = models.ImageField(
        upload_to='experience/', blank=True, validators=[validate_image_file],
        help_text='Photos related to industrial attachment/work (JPG, PNG, WEBP max 5MB)'
    )
    alt_text = models.CharField(
        max_length=200, blank=True,
        help_text='Descriptive alt text for accessibility'
    )
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-order', '-start_date']
        verbose_name_plural = 'Experience'

    def __str__(self):
        return f'{self.role} at {self.organization}'


class ExperienceProject(models.Model):
    experience = models.ForeignKey(
        Experience, on_delete=models.CASCADE, related_name='exp_projects'
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True, help_text='Your responsibilities in this project')
    technologies = models.CharField(max_length=500, blank=True, help_text='Comma-separated technologies')
    lessons = models.TextField(blank=True, help_text='What you learned from this project')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Experience Project'
        verbose_name_plural = 'Experience Projects'

    def __str__(self):
        return self.name

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]


# ==============================================================================
# EDUCATION
# ==============================================================================

class Education(models.Model):
    institution = models.CharField(max_length=200, default='Kirinyaga University')
    course = models.CharField(max_length=200, default='Bachelor of Science in Information Technology')
    level = models.CharField(max_length=100, default='Year 2', help_text='e.g., Year 2')
    description = models.TextField(blank=True)
    start_date = models.CharField(max_length=100, blank=True, default='Current')
    end_date = models.CharField(max_length=100, blank=True, default='2028 (Expected)')
    achievements = models.TextField(blank=True, help_text='Academic achievements, one per line')
    relevant_areas = models.TextField(
        blank=True,
        help_text='Relevant course areas, comma-separated'
    )
    is_current = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-order']
        verbose_name_plural = 'Education'

    def __str__(self):
        return f'{self.course} — {self.institution}'

    def get_areas_list(self):
        return [a.strip() for a in self.relevant_areas.split(',') if a.strip()]

    def get_achievements_list(self):
        return [a.strip() for a in self.achievements.split('\n') if a.strip()]


# ==============================================================================
# PROJECTS
# ==============================================================================

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('django', 'Django'),
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('web', 'Web'),
        ('database', 'Database'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('live', '🟢 Live'),
        ('in_development', '🔵 In Development'),
        ('temporarily_unavailable', '🟡 Temporarily Unavailable'),
        ('archived', '⚫ Archived'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    short_description = models.TextField(help_text='Brief description for project cards')
    role = models.CharField(max_length=200, blank=True, default='Developer / Attachment Student', help_text='Your role in this project')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='live', help_text='Current project operational status')
    is_featured = models.BooleanField(default=True, help_text='Show in Featured Projects on Homepage')

    # Case study fields
    overview = models.TextField(blank=True, help_text='Detailed project overview')
    problem = models.TextField(blank=True, help_text='Problem this project solves')
    solution = models.TextField(blank=True, help_text='How this project solves the problem')
    features = models.TextField(blank=True, help_text='Key features, one per line')
    technologies = models.CharField(max_length=500, help_text='Comma-separated technologies')
    development_process = models.TextField(blank=True)
    challenges = models.TextField(blank=True)
    lessons_learned = models.TextField(blank=True)
    results = models.TextField(blank=True)

    # Links
    github_url = models.URLField(blank=True, default='', help_text='GitHub repository URL (leave blank if none)')
    live_url = models.URLField(blank=True, default='', help_text='Live demo URL (leave blank if none)')

    # Media
    image = models.ImageField(
        upload_to='projects/', blank=True, validators=[validate_image_file],
        help_text='Main project cover image (JPG, PNG, WEBP max 5MB)'
    )
    screenshot_1 = models.ImageField(
        upload_to='projects/screenshots/', blank=True, validators=[validate_image_file],
        help_text='Project screenshot 1 (JPG, PNG, WEBP max 5MB)'
    )
    screenshot_2 = models.ImageField(
        upload_to='projects/screenshots/', blank=True, validators=[validate_image_file],
        help_text='Project screenshot 2 (JPG, PNG, WEBP max 5MB)'
    )
    screenshot_3 = models.ImageField(
        upload_to='projects/screenshots/', blank=True, validators=[validate_image_file],
        help_text='Project screenshot 3 (JPG, PNG, WEBP max 5MB)'
    )

    # Meta
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='django')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]

    def get_features_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]

    @property
    def status_badge_class(self):
        return {
            'live': 'badge-status-live',
            'in_development': 'badge-status-in-dev',
            'temporarily_unavailable': 'badge-status-unavail',
            'archived': 'badge-status-archived',
        }.get(self.status, 'badge-status-live')

    @property
    def status_display_with_icon(self):
        icons = {
            'live': '🟢 Live',
            'in_development': '🟡 In Development',
            'temporarily_unavailable': '🟠 Maintenance',
            'archived': '⚪ Archived',
        }
        return icons.get(self.status, self.get_status_display())


class ProjectScreenshot(models.Model):
    """Multiple gallery screenshots per project."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(
        upload_to='projects/screenshots/', validators=[validate_image_file],
        help_text='Detailed system screenshot (JPG, PNG, WEBP max 5MB)'
    )
    caption = models.CharField(max_length=200, blank=True, help_text='Screenshot caption/title')
    alt_text = models.CharField(max_length=200, blank=True, help_text='Descriptive text for accessibility')
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Project Screenshot'
        verbose_name_plural = 'Project Screenshots'

    def __str__(self):
        return f'{self.project.title} - Screenshot {self.order + 1}'


# ==============================================================================
# TECH PLAYGROUND EXPERIMENTS
# ==============================================================================

class PlaygroundExperiment(models.Model):
    STATUS_CHOICES = [
        ('live', '🟢 Live Demo'),
        ('in_development', '🟡 In Development'),
        ('experimental', '🔵 Experimental'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(help_text='Short description of the mini tool or experiment')
    icon = models.CharField(max_length=100, default='fas fa-flask', help_text='Font Awesome icon class')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='in_development')
    technology = models.CharField(max_length=200, default='JavaScript, HTML5, CSS3')
    demo_url = models.URLField(blank=True, default='', help_text='Direct demo or live interactive link')
    code_url = models.URLField(blank=True, default='', help_text='GitHub or code snippet URL')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Playground Experiment'
        verbose_name_plural = 'Playground Experiments'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# ==============================================================================
# CURRENTLY BUILDING
# ==============================================================================

class CurrentlyBuilding(models.Model):
    STATUS_CHOICES = [
        ('Planning', 'Planning'),
        ('In Development', 'In Development'),
        ('Testing', 'Testing'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(help_text='What is this project and what problem does it solve?')
    technologies = models.CharField(max_length=500, help_text='Technologies being used, comma-separated')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='In Development')
    progress_percent = models.IntegerField(default=50, help_text='Estimated progress from 0 to 100')
    image = models.ImageField(upload_to='building/', blank=True, help_text='Project preview or architecture diagram')
    github_url = models.URLField(blank=True, default='', help_text='GitHub URL if available')
    live_url = models.URLField(blank=True, default='', help_text='Live demo/staging URL if available')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Currently Building Project'
        verbose_name_plural = 'Currently Building Projects'

    def __str__(self):
        return f'{self.name} [{self.status}]'

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]


# ==============================================================================
# PROFESSIONAL RECOMMENDATION
# ==============================================================================

class Recommendation(models.Model):
    """
    Official recommendation letter and commendations from supervisors / organizations.
    Supervisor personal phone and email are kept private and not displayed publicly.
    """
    supervisor_name = models.CharField(max_length=200, default='Scholastica Mutuku')
    supervisor_role = models.CharField(max_length=200, default='Software Engineer')
    organization = models.CharField(max_length=200, default='ICT Authority of Kenya')
    organization_note = models.CharField(
        max_length=300,
        blank=True,
        default='State Corporation under Kenya State Corporations Act 446'
    )
    recommendation_date = models.CharField(max_length=100, default='20 July 2026')
    attachment_duration = models.CharField(max_length=100, default='4 May 2026 – 31 July 2026 (13 Weeks)')
    quote = models.TextField(
        help_text='Main excerpt or recommendation statement from supervisor',
        default='Pavis Mugo Muruga successfully completed a 13-week industrial attachment '
                'at the ICT Authority of Kenya from 4 May 2026 to 31 July 2026. He demonstrated '
                'exceptional enthusiasm, commitment, strong willingness to learn, and practical technical competency '
                'in Python, Django, ICT support, and system development.'
    )
    highlights = models.TextField(
        blank=True,
        help_text='Supervisor highlighted attributes, one per line',
        default='Enthusiasm and strong commitment\n'
                'Strong willingness to learn and adapt quickly\n'
                'Proficiency in Python and Django development\n'
                'Solid ICT support and troubleshooting capabilities\n'
                'High level of professionalism and positive attitude\n'
                'Excellent problem-solving abilities\n'
                'Ability to work independently and as part of a team\n'
                'Effective communication and collaborative skills\n'
                'Quick comprehension of new concepts and technologies\n'
                'Dedication to delivering quality and dependable work'
    )
    recommendation_letter = models.FileField(
        upload_to='recommendations/',
        blank=True,
        validators=[validate_document_file],
        help_text='Upload the official recommendation letter PDF (max 10MB)'
    )
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Professional Recommendation'
        verbose_name_plural = 'Professional Recommendations'

    def __str__(self):
        return f'{self.supervisor_name} ({self.organization})'

    def get_highlights_list(self):
        return [h.strip() for h in self.highlights.split('\n') if h.strip()]


# ==============================================================================
# CERTIFICATIONS
# ==============================================================================

class Certification(models.Model):
    name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(
        upload_to='certifications/', blank=True, validators=[validate_image_file],
        help_text='Certificate image (JPG, PNG, WEBP max 5MB)'
    )
    certificate_pdf = models.FileField(
        upload_to='certifications/pdfs/', blank=True, validators=[validate_document_file],
        help_text='Certificate document PDF (max 10MB)'
    )
    alt_text = models.CharField(max_length=200, blank=True, help_text='Descriptive alt text for the certificate image')
    verification_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-date']

    def __str__(self):
        return f'{self.name} — {self.organization}'


# ==============================================================================
# GALLERY
# ==============================================================================

class GalleryImage(models.Model):
    """Professional and project-related gallery photos."""
    CATEGORY_CHOICES = [
        ('professional', 'Professional'),
        ('project', 'Project'),
        ('experience', 'Experience / Attachment'),
        ('education', 'Education'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200, blank=True, help_text='Optional short title')
    image = models.ImageField(
        upload_to='gallery/', validators=[validate_image_file],
        help_text='Gallery photo (JPG, PNG, WEBP max 5MB)'
    )
    alt_text = models.CharField(
        max_length=200, blank=True,
        help_text='Descriptive alt text for accessibility — describe what is in the photo'
    )
    caption = models.CharField(max_length=300, blank=True, help_text='Optional display caption')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='professional')
    is_featured = models.BooleanField(default=False, help_text='Show in featured gallery sections')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.title or f'{self.get_category_display()} photo — {self.created_at.strftime("%Y-%m-%d")}'


# ==============================================================================
# ACHIEVEMENTS
# ==============================================================================

class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic'),
        ('project', 'Project'),
        ('competition', 'Competition'),
        ('professional', 'Professional'),
        ('certification', 'Certification'),
        ('award', 'Award'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='project')
    icon = models.CharField(max_length=100, blank=True, default='fas fa-trophy')
    date = models.DateField(null=True, blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-date']

    def __str__(self):
        return self.title


# ==============================================================================
# BLOG
# ==============================================================================

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    excerpt = models.TextField(blank=True, help_text='Short summary for listing pages')
    content = models.TextField()
    featured_image = models.ImageField(
        upload_to='blog/', blank=True, validators=[validate_image_file],
        help_text='Featured image for this blog post (JPG, PNG, WEBP max 5MB)'
    )
    featured_image_alt = models.CharField(
        max_length=200, blank=True,
        help_text='Descriptive alt text for the featured image'
    )
    category = models.CharField(max_length=100, blank=True)
    tags = models.CharField(max_length=500, blank=True, help_text='Comma-separated tags')
    author = models.CharField(max_length=200, default='Pavis Mugo Muruga')
    reading_time = models.IntegerField(default=5, help_text='Estimated reading time in minutes')
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.content and not self.reading_time:
            word_count = len(self.content.split())
            self.reading_time = max(1, math.ceil(word_count / 200))
        super().save(*args, **kwargs)


# ==============================================================================
# TESTIMONIALS
# ==============================================================================

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, blank=True)
    organization = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True)
    featured = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f'{self.name} — {self.organization}'


# ==============================================================================
# CONTACT MESSAGES
# ==============================================================================

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.subject} — {self.name}'


# ==============================================================================
# CURRENTLY LEARNING
# ==============================================================================

class LearningTopic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, blank=True, default='fas fa-book-open')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Learning Topic'
        verbose_name_plural = 'Learning Topics'

    @property
    def title(self):
        return self.name

    def __str__(self):
        return self.name


# ==============================================================================
# GOALS
# ==============================================================================

class Goal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, blank=True, default='fas fa-bullseye')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


# ==============================================================================
# TIMELINE / MY JOURNEY
# ==============================================================================

class TimelineEvent(models.Model):
    CATEGORY_CHOICES = [
        ('education', 'Education'),
        ('experience', 'Industrial Attachment / Experience'),
        ('project', 'Project & System Development'),
        ('achievement', 'Achievement'),
        ('goal', 'Future Milestone'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.CharField(max_length=100, help_text='e.g., 2026, May – Jul 2026, 2028 (Expected)')
    icon = models.CharField(max_length=100, blank=True, default='fas fa-circle')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='education')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Timeline Event'
        verbose_name_plural = 'Timeline Events'

    def __str__(self):
        return f'{self.date} — {self.title}'


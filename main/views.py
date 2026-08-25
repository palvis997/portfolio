"""
Views for Pavis Mugo Muruga Multi-Page Portfolio Website.
Structured with concise landing page and dedicated pages for all sections.
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import (
    SiteSettings, SocialLink, Skill, Experience, Education,
    Project, CurrentlyBuilding, Recommendation, Certification, Achievement,
    BlogPost, Testimonial, LearningTopic, Goal, TimelineEvent, PlaygroundExperiment
)
from .forms import ContactForm


# ==============================================================================
# 1. HOMEPAGE (SHORT & CONCISE LANDING PAGE)
# ==============================================================================

def home(request):
    """
    Concise, high-impact landing page:
    1. Hero Section
    2. Short About Me (3-5 lines + link to /about/)
    3. What I Do (compact cards + link to /skills/)
    4. 3 Featured Projects (with real live links + status + link to /projects/)
    5. ICT Authority Experience Summary (+ link to /experience/)
    6. Currently Learning (4-5 items + link to /about/)
    7. Call To Action (link to /contact/)
    8. Compact Footer
    """
    featured_projects = Project.objects.filter(is_active=True, is_featured=True)[:3]
    if not featured_projects.exists():
        featured_projects = Project.objects.filter(is_active=True)[:3]

    learning_topics = LearningTopic.objects.filter(is_active=True)[:5]
    latest_posts = BlogPost.objects.filter(published=True)[:3]

    stats = {
        'projects_count': Project.objects.filter(is_active=True).count(),
        'skills_count': Skill.objects.filter(is_active=True).count(),
        'learning_count': LearningTopic.objects.filter(is_active=True).count(),
        'attachment_weeks': 13,
    }

    context = {
        'featured_projects': featured_projects,
        'learning_topics': learning_topics,
        'latest_posts': latest_posts,
        'stats': stats,
        'ict_experience': Experience.objects.filter(is_active=True).first(),
    }
    return render(request, 'main/home.html', context)


# ==============================================================================
# 2. ABOUT PAGE
# ==============================================================================

def about_page(request):
    """
    Dedicated About Page:
    - Who I Am & My Story
    - My IT Journey & Values
    - Education & Academic Focus
    - Industrial Experience Overview
    - Career Goals (Short-term, Medium-term, Long-term)
    - Full Currently Learning Topics
    - Professional Timeline
    """
    context = {
        'education_list': Education.objects.filter(is_active=True),
        'experiences': Experience.objects.filter(is_active=True).prefetch_related('exp_projects'),
        'learning_topics': LearningTopic.objects.filter(is_active=True),
        'goals': Goal.objects.filter(is_active=True),
        'timeline_events': TimelineEvent.objects.filter(is_active=True),
    }
    return render(request, 'main/about.html', context)


# ==============================================================================
# 3. WHAT I DO (SERVICES PAGE)
# ==============================================================================

def services_page(request):
    """
    Dedicated What I Do / Services Page:
    - Web Development
    - Python & Django Development
    - System Development
    - ICT Support
    - Database Management
    - Data Capturing & Information Management
    """
    return render(request, 'main/services_page.html')


# ==============================================================================
# 4. SKILLS PAGE
# ==============================================================================

def skills_page(request):
    """
    Dedicated Complete Skills Page with categorized skills and verified levels:
    - Programming
    - Web Development
    - Frameworks
    - Databases
    - Data & Information Management (Data Capturing)
    - ICT Support & Systems
    - Networking
    - Development Tools
    - Professional Strengths
    """
    skills_active = Skill.objects.filter(is_active=True)
    context = {
        'skills_programming': skills_active.filter(category='programming'),
        'skills_framework': skills_active.filter(category='framework'),
        'skills_database': skills_active.filter(category='database'),
        'skills_data': skills_active.filter(category='data'),
        'skills_it': skills_active.filter(category='it'),
        'skills_tool': skills_active.filter(category='tool'),
        'skills_other': skills_active.filter(category='other'),
    }
    return render(request, 'main/skills_page.html', context)


# ==============================================================================
# 5. EXPERIENCE PAGE
# ==============================================================================

def experience_page(request):
    """
    Dedicated Experience Page:
    - ICT Authority of Kenya (4 May 2026 – 31 July 2026, 13 Weeks)
    - Systems worked on (Library Management, ICT Asset Management, GBV System, ICT Support)
    - Key responsibilities, technical tasks, and lessons learned
    - Timeline of practical experience
    """
    context = {
        'experiences': Experience.objects.filter(is_active=True).prefetch_related('exp_projects'),
        'recommendations': Recommendation.objects.filter(is_active=True),
    }
    return render(request, 'main/experience_page.html', context)


# ==============================================================================
# 6. PROJECTS PAGE (ALL PROJECTS WITH FILTERS & PAGINATION)
# ==============================================================================

def projects_page(request):
    """
    Dedicated All Projects Page:
    - Category filtering (ALL, PYTHON, DJANGO, JAVASCRIPT, WEB, DATABASE, ICT)
    - Search functionality
    - Status badges (🟢 Live, 🔵 In Development, 🟡 Temporarily Unavailable, ⚫ Archived)
    - Real Live Demo and GitHub links
    - Case study detail links
    """
    projects_qs = Project.objects.filter(is_active=True)

    category_filter = request.GET.get('category', 'all').strip().lower()
    search_query = request.GET.get('q', '').strip()

    if category_filter and category_filter != 'all':
        projects_qs = projects_qs.filter(category=category_filter)

    if search_query:
        projects_qs = projects_qs.filter(
            Q(title__icontains=search_query) |
            Q(short_description__icontains=search_query) |
            Q(technologies__icontains=search_query) |
            Q(role__icontains=search_query)
        )

    paginator = Paginator(projects_qs, 6)
    page_number = request.GET.get('page', 1)
    projects = paginator.get_page(page_number)

    context = {
        'projects': projects,
        'category_filter': category_filter,
        'search_query': search_query,
        'categories': Project.CATEGORY_CHOICES,
        'total_count': projects_qs.count(),
    }
    return render(request, 'main/projects_page.html', context)


# ==============================================================================
# 7. PROJECT DETAIL (CASE STUDY)
# ==============================================================================

def project_detail(request, slug):
    """Detailed Case Study Breakdown for an individual project."""
    project = get_object_or_404(Project, slug=slug, is_active=True)
    related_projects = Project.objects.filter(
        category=project.category, is_active=True
    ).exclude(pk=project.pk)[:3]
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'main/project_detail.html', context)


# ==============================================================================
# 8. PROJECT LAB (DEVELOPER WORKSPACE)
# ==============================================================================

def project_lab_page(request):
    """
    Dedicated Project Lab / Developer Workspace:
    - Deep dive into software engineering workflows
    - Active development tracking
    - Currently Building status indicators
    - Systems architecture & technical features
    """
    context = {
        'projects': Project.objects.filter(is_active=True),
        'currently_building': CurrentlyBuilding.objects.filter(is_active=True),
    }
    return render(request, 'main/project_lab.html', context)


# ==============================================================================
# 9. TECH PLAYGROUND
# ==============================================================================

def playground_page(request):
    """
    Dedicated Tech Playground:
    - Interactive card demonstrations
    - Technical experiments & utilities
    - "More experiments coming soon" section
    """
    experiments = PlaygroundExperiment.objects.filter(is_active=True)
    context = {
        'experiments': experiments,
    }
    return render(request, 'main/playground.html', context)


# ==============================================================================
# 10. DEVELOPER DASHBOARD
# ==============================================================================

def developer_dashboard(request):
    """
    Dedicated Pavis Developer Dashboard:
    - Displays real, database-driven metrics and live analytics only
    - No fabricated statistics
    """
    projects_count = Project.objects.filter(is_active=True).count()
    skills_count = Skill.objects.filter(is_active=True).count()
    posts_count = BlogPost.objects.filter(published=True).count()
    learning_count = LearningTopic.objects.filter(is_active=True).count()
    building_count = CurrentlyBuilding.objects.filter(is_active=True).count()

    context = {
        'projects_count': projects_count,
        'skills_count': skills_count,
        'posts_count': posts_count,
        'learning_count': learning_count,
        'building_count': building_count,
        'recent_projects': Project.objects.filter(is_active=True)[:4],
        'recent_posts': BlogPost.objects.filter(published=True)[:3],
        'learning_topics': LearningTopic.objects.filter(is_active=True),
        'currently_building': CurrentlyBuilding.objects.filter(is_active=True),
    }
    return render(request, 'main/dashboard.html', context)


# ==============================================================================
# 11. CREDENTIALS PAGE
# ==============================================================================

def credentials_page(request):
    """
    Dedicated Credentials Page:
    - Professional Recommendation (Scholastica Mutuku - Software Engineer, ICT Authority of Kenya)
    - Recommendation Letter viewing/downloading
    - Verified Industrial Attachment credentials
    - Certifications (Placeholder / No TVET CDACC)
    - Achievements & Training
    """
    context = {
        'recommendations': Recommendation.objects.filter(is_active=True),
        'certifications': Certification.objects.filter(is_active=True),
        'achievements': Achievement.objects.filter(is_active=True),
    }
    return render(request, 'main/credentials.html', context)


# ==============================================================================
# 12. RESUME / CV PAGE
# ==============================================================================

def resume_page(request):
    """Dedicated printable and downloadable CV/Resume page."""
    skills_active = Skill.objects.filter(is_active=True)
    context = {
        'site': SiteSettings.get_instance(),
        'social_links': SocialLink.objects.filter(is_active=True),
        'education_list': Education.objects.filter(is_active=True),
        'experiences': Experience.objects.filter(is_active=True).prefetch_related('exp_projects'),
        'projects': Project.objects.filter(is_active=True),
        'skills_programming': skills_active.filter(category='programming'),
        'skills_framework': skills_active.filter(category='framework'),
        'skills_database': skills_active.filter(category='database'),
        'skills_data': skills_active.filter(category='data'),
        'skills_tool': skills_active.filter(category='tool'),
        'skills_it': skills_active.filter(category='it'),
        'skills_other': skills_active.filter(category='other'),
        'recommendations': Recommendation.objects.filter(is_active=True),
    }
    return render(request, 'main/cv.html', context)


# Alias for backward compatibility
cv_view = resume_page


# ==============================================================================
# 13. BLOG LIST & DETAIL
# ==============================================================================

def blog_list(request):
    """Blog listing with search, category filtering, and pagination."""
    posts = BlogPost.objects.filter(published=True)

    query = request.GET.get('q', '').strip()
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(excerpt__icontains=query) |
            Q(tags__icontains=query)
        )

    category = request.GET.get('category', '').strip()
    if category:
        posts = posts.filter(category=category)

    tag = request.GET.get('tag', '').strip()
    if tag:
        posts = posts.filter(tags__icontains=tag)

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    all_categories = (
        BlogPost.objects.filter(published=True)
        .values_list('category', flat=True)
        .distinct()
    )

    all_tags = set()
    for t_str in BlogPost.objects.filter(published=True).values_list('tags', flat=True):
        if t_str:
            for t in t_str.split(','):
                if t.strip():
                    all_tags.add(t.strip())

    context = {
        'posts': page_obj,
        'query': query,
        'current_category': category,
        'current_tag': tag,
        'categories': all_categories,
        'tags': sorted(list(all_tags)),
        'recent_posts': BlogPost.objects.filter(published=True)[:5],
    }
    return render(request, 'main/blog_list.html', context)


def blog_detail(request, slug):
    """Single blog post view with related articles."""
    post = get_object_or_404(BlogPost, slug=slug, published=True)

    related_posts = BlogPost.objects.filter(
        category=post.category, published=True
    ).exclude(pk=post.pk)[:3]

    recent_posts = BlogPost.objects.filter(published=True).exclude(pk=post.pk)[:5]

    context = {
        'post': post,
        'related_posts': related_posts,
        'recent_posts': recent_posts,
    }
    return render(request, 'main/blog_detail.html', context)


# ==============================================================================
# 14. CONTACT PAGE & SUBMISSION HANDLER
# ==============================================================================

def contact_page(request):
    """Dedicated Contact Page."""
    form = ContactForm()
    return render(request, 'main/contact_page.html', {'form': form})


def contact_submit(request):
    """Handle contact form submission."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save(commit=False)
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                contact_msg.ip_address = x_forwarded_for.split(',')[0].strip()
            else:
                contact_msg.ip_address = request.META.get('REMOTE_ADDR')
            contact_msg.user_agent = request.META.get('HTTP_USER_AGENT', '')[:500]
            contact_msg.save()

            messages.success(
                request,
                f"Thank you, {contact_msg.name}! Your message has been received. "
                "I will get back to you promptly."
            )
            return redirect('contact_success')
        else:
            messages.error(request, "Please correct the errors in the form below.")
            return render(request, 'main/contact_page.html', {'form': form})
    return redirect('contact_page')


def contact_success(request):
    """Confirmation page after successful contact submission."""
    return render(request, 'main/contact_success.html')


def accessibility_statement_page(request):
    """Dedicated Accessibility Statement explaining website compliance and tools."""
    return render(request, 'main/accessibility_statement.html')


def robots_txt(request):
    """Generate robots.txt."""
    content = """User-agent: *
Allow: /
Disallow: /admin/

Sitemap: {scheme}://{host}/sitemap.xml
""".format(scheme=request.scheme, host=request.get_host())
    return HttpResponse(content, content_type='text/plain')


# ==============================================================================
# ERROR HANDLERS
# ==============================================================================

def custom_404(request, exception):
    return render(request, 'main/404.html', status=404)


def custom_403(request, exception):
    return render(request, 'main/403.html', status=403)


def custom_500(request):
    return render(request, 'main/500.html', status=500)

"""
URL patterns for Pavis Mugo Muruga Multi-Page Portfolio Website.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
    path('what-i-do/', views.services_page, name='what_i_do'),
    path('services/', views.services_page, name='services'),
    path('skills/', views.skills_page, name='skills'),
    path('experience/', views.experience_page, name='experience'),
    path('projects/', views.projects_page, name='projects'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail_alias'),
    path('project-lab/', views.project_lab_page, name='project_lab'),
    path('playground/', views.playground_page, name='playground'),
    path('dashboard/', views.developer_dashboard, name='dashboard'),
    path('credentials/', views.credentials_page, name='credentials'),
    path('resume/', views.resume_page, name='resume'),
    path('cv/', views.resume_page, name='cv_view'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact_page, name='contact'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('accessibility/', views.accessibility_statement_page, name='accessibility'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
]

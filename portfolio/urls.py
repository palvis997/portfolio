"""
URL configuration for portfolio project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.static import serve
from main.sitemaps import StaticViewSitemap, ProjectSitemap, BlogPostSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'projects': ProjectSitemap,
    'blog': BlogPostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('main.urls')),
]

# Always serve media files (profile photos, project screenshots, recommendation PDF)
# For a portfolio site with minimal media, serving via Django is perfectly fine.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]

# Custom error handlers
handler404 = 'main.views.custom_404'
handler403 = 'main.views.custom_403'
handler500 = 'main.views.custom_500'


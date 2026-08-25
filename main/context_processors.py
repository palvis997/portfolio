"""
Context processor to make SiteSettings available in all templates.
"""
from .models import SiteSettings


def site_settings(request):
    """Add site settings to every template context."""
    try:
        settings = SiteSettings.get_instance()
    except Exception:
        settings = None
    return {'site': settings}

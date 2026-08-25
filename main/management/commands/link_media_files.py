"""
Management command: link_media_files
Links existing media images to their corresponding database records:
  - profile/pavis_profile_1.jpeg  -> SiteSettings.profile_image
  - projects/gbv_landing.jpeg     -> GBV project image
  - projects/library_landing.jpeg -> Library project image
"""
from django.core.management.base import BaseCommand
from main.models import SiteSettings, Project


class Command(BaseCommand):
    help = 'Link uploaded media files to their database records'

    def handle(self, *args, **options):
        self.link_profile()
        self.link_projects()

    # ------------------------------------------------------------------
    def link_profile(self):
        """Set profile photo on SiteSettings."""
        site = SiteSettings.get_instance()
        site.profile_image = 'profile/pavis_profile_1.jpeg'
        site.save(update_fields=['profile_image'])
        self.stdout.write(self.style.SUCCESS(
            '[OK] Profile photo linked -> SiteSettings.profile_image = profile/pavis_profile_1.jpeg'
        ))

    # ------------------------------------------------------------------
    def link_projects(self):
        """Link landing page screenshots to the matching projects."""
        links = [
            {
                'slug': 'gbv-system',
                'image': 'projects/gbv_landing.jpeg',
                'label': 'GBV / Digital Safe Space System',
            },
            {
                'slug': 'library-management-system',
                'image': 'projects/library_landing.jpeg',
                'label': 'Library Management System',
            },
        ]

        for item in links:
            try:
                project = Project.objects.get(slug=item['slug'])
                project.image = item['image']
                project.save(update_fields=['image'])
                self.stdout.write(self.style.SUCCESS(
                    f"[OK] Project image linked -> {item['label']} (slug={item['slug']})"
                ))
            except Project.DoesNotExist:
                # Try a looser title match
                keyword = item['slug'].replace('-', ' ').split()[0]
                qs = Project.objects.filter(title__icontains=keyword)
                if qs.exists():
                    project = qs.first()
                    project.image = item['image']
                    project.save(update_fields=['image'])
                    self.stdout.write(self.style.SUCCESS(
                        f"[OK] Project image linked (fuzzy match) -> {project.title}"
                    ))
                else:
                    self.stdout.write(self.style.WARNING(
                        f"[WARNING] Project not found for slug '{item['slug']}'. "
                        f"Assign manually via Admin -> Projects -> {item['label']}."
                    ))

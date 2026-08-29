# Generated manually because the local Python launcher is unavailable.

import main.validators
from django.db import migrations, models


def set_profile_three(apps, schema_editor):
    SiteSettings = apps.get_model('main', 'SiteSettings')
    SiteSettings.objects.filter(pk=1).update(profile_image='images/profile 3.jpeg')


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_media_management_gallery_screenshots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='profile_image',
            field=models.ImageField(
                blank=True,
                default='images/profile 3.jpeg',
                help_text='Profile photo for Hero and About sections (JPG, PNG, WEBP max 3MB)',
                upload_to='profile/',
                validators=[main.validators.validate_avatar_file],
            ),
        ),
        migrations.RunPython(set_profile_three, migrations.RunPython.noop),
    ]

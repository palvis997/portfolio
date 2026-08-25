"""
Media file validators for Pavis Mugo Muruga Portfolio.
Enforces allowed extensions and maximum file size limits for secure uploads.
"""
import os
from django.core.exceptions import ValidationError


def validate_image_file(value):
    """Validate uploaded images for format and file size (max 5MB)."""
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.jpg', '.jpeg', '.png', '.webp']
    if ext not in valid_extensions:
        raise ValidationError(
            f'Unsupported image format "{ext}". Allowed formats are: JPG, JPEG, PNG, WEBP.'
        )

    # 5MB limit
    max_size = 5 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError(
            f'File size ({value.size / (1024 * 1024):.1f} MB) exceeds maximum allowed limit of 5 MB.'
        )


def validate_document_file(value):
    """Validate uploaded documents for format and file size (max 10MB)."""
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.pdf']
    if ext not in valid_extensions:
        raise ValidationError(
            f'Unsupported document format "{ext}". Allowed format is: PDF.'
        )

    # 10MB limit
    max_size = 10 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError(
            f'File size ({value.size / (1024 * 1024):.1f} MB) exceeds maximum allowed limit of 10 MB.'
        )


def validate_avatar_file(value):
    """Validate avatar/profile photos (max 3MB, JPG/PNG/WEBP)."""
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.jpg', '.jpeg', '.png', '.webp']
    if ext not in valid_extensions:
        raise ValidationError(
            f'Unsupported photo format "{ext}". Allowed formats are: JPG, JPEG, PNG, WEBP.'
        )

    # 3MB limit
    max_size = 3 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError(
            f'Profile photo size ({value.size / (1024 * 1024):.1f} MB) exceeds maximum allowed limit of 3 MB.'
        )

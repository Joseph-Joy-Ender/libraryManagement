from django.core.validators import ValidationError


def validate_file_size(file):
    max_size = 100
    if file.size > max_size * 1024:
        raise ValidationError(f"Image size cannot be more than {max_size}KB")

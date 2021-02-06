from django.core.exceptions import ValidationError


def validate_file_extension(value):
    result = value.name.endswith('.bin') or value.name.endswith('.zip')
    if not result:
        raise ValidationError('File extension not allowed.')


def validate_version_format(value):
    result = value.split('.')
    if len(result) < 3:
        raise ValidationError('The Version must follow the standard X.Y.Z (MAJOR.MINOR.PATCH).')


def validate_version_only_number(value):
    result = value.replace('.', '')
    if not result.isdecimal():
        raise ValidationError('The version must contain only numbers')

from django.core.exceptions import ValidationError

def validate_content(value):
    content=value
    if content== " " or content.__contains__('fuck') or content.__contains__('FUCK'):
        raise ValidationError('Hash word')
        return value

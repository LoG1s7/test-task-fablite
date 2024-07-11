import re

from django.core.exceptions import ValidationError


def validate_me_name(username):
    """ Проверяет, чтобы имя пользователя не являлось me """
    if username.lower() == 'me':
        raise ValidationError(f'Некорректное имя пользователя {username}')
    return username


def validate_name(value):
    """
    Проверяет, чтобы имя пользователя не содержало только цифры ил символы
    """
    pattern = re.compile(r'^[\d\W]+$')
    if pattern.match(value):
        raise ValidationError(
            'Имя пользователя не должно содержать '
            'только цифры или специальные символы'
        )

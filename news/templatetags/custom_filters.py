from django import template

from news.models import Category

register = template.Library()


class APIException(Exception):
    pass



BAD_STR = ['нигер', 'ху']


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise APIException(f'Указанный id статьи, не является строкой: {value}')

    for bad in BAD_STR:

        value = value.replace(f'{bad[:1].upper()}{bad[1:]}', f'{bad[:1].upper()}{"*" * (len(bad) - 1)}')

        value = value.replace(f'{bad[:1].lower()}{bad[1:]}', f'{bad[:1].lower()}{"*" * (len(bad) - 1)}')

    return value


@register.filter()
def get_category(category_id):
    return Category.objects.get(id=category_id).name
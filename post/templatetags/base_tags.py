from django import template
from post.models import Category

register = template.Library()


@register.simple_tag
def title(data='وبلاگ'):
    return data


@register.inclusion_tag('site/partials/_navbar.html')
def category():
    categories_list = Category.objects.filter(status=True)
    return {'categories': categories_list}

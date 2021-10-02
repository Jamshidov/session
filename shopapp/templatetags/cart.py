from django import template
register = template.Library()


@register.filter()
def summary(value, arg):
    return float(value) * arg










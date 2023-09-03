from django import template

register = template.Library()

@register.filter
def modulus(value, arg):
    return value % arg

# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()


#自定义过滤器

@register.filter(name='upper_case')
def upper_case(value):
    """将字符串转换为大写"""
    if isinstance(value, str):
        return value.upper()
    return value

from django import template
register = template.library()


@register.filter
def index(list, element):
    return list.index(element)
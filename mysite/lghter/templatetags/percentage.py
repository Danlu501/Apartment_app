from django import template

register = template.Library()


@register.filter
def percentage(end, start):
    diff = end - start
    perc = (diff / start) * 100
    perc = round(perc, 2)
    return perc

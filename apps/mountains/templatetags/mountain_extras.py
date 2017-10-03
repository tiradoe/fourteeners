from django import template
from pprint import pprint

register = template.Library()

@register.filter
def getClimb(mountain, id):
    return mountain.calculateClimbs(id)


@register.filter
def formatClimb(inputField, value):
    print(inputField)
    return value


@register.filter
def cap(word):
    cap_word = word.capitalize()
    return cap_word

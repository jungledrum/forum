from django import template
from django.utils.html import escape


register = template.Library()
  

def mongo_id(value):
    return value.get('_id','')
register.filter(mongo_id)


def editor(value):
    return escape(value).replace('\n', '<br>')
register.filter(editor)



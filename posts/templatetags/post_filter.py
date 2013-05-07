from django import template
register = template.Library()
  
def mongo_id(value):
    return value.get('_id','')
register.filter(mongo_id)
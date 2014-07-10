from django.conf import settings
from django import template
from chump.forms import ChumpSubscribeForm

register = template.Library()

@register.assignment_tag
def get_chump_form(list_id=None):
    list_id = list_id or settings.CHUMP_LIST_ID  # Throw an error if no value
    return ChumpSubscribeForm(list_id)

@register.inclusion_tag(['chump/chump_form.html', 'includes/chump_form.html', 'inc/chump_form.html', 'partial/chump_form.html', 'chump_form.html'])
def chump_form(list_id=None):
    list_id = list_id or settings.CHUMP_LIST_ID  # Throw an error if no value
    return {'chump_form':ChumpSubscribeForm(list_id)}


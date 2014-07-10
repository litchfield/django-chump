from django.conf import settings
from django import template
from chump.forms import ChumpSubscribeForm
from chump import get_template_names

register = template.Library()

@register.assignment_tag
def get_chump_form():
    return ChumpSubscribeForm()

@register.inclusion_tag(get_template_names('chump_form.html'))
def chump_form():
	return {'chump_form':ChumpSubscribeForm()}


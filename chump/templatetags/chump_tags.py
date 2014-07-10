from django.conf import settings
from django import template
from chump.forms import ChumpSubscribeForm

register = template.Library()

@register.assignment_tag
def get_chump_form():
    return ChumpSubscribeForm()

@register.inclusion_tag(['chump/chump_form.html', 'includes/chump_form.html', 'inc/chump_form.html', 'partial/chump_form.html', 'chump_form.html'])
def chump_form():
	return {'chump_form':ChumpSubscribeForm()}


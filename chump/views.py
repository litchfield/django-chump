from mailchimp import utils
from urllib2 import URLError
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from mailchimp.chimpy.chimpy import ChimpyException
from chump import get_template_names
from forms import ChumpSubscribeForm

DONE_URL = getattr(settings, 'MAILCHIMP_DONE_URL', '/chump/done/')
ERROR_URL = getattr(settings, 'MAILCHIMP_ERROR_URL', '/chump/error/')

def subscribe_done(request):
    return render(request, get_template_names('chump_done.html'), {})

def subscribe_error(request):
    return render(request, get_template_names('chump_error.html'), {})

def subscribe_process(request, list_id=None):
    list_id = list_id or getattr(settings, 'MAILCHIMP_LIST_ID', None)
    if not list_id:
        error_msg = 'Missing subscription list ID'
    else:
        form = ChumpSubscribeForm(data=request.POST or None)
        error_msg = 'Invalid entry'
        if form.is_valid():
            try:
                lst = utils.get_connection().get_list_by_id(list_id)
                opt = {
                    'EMAIL': form.cleaned_data['email'],
                    'NAME': form.cleaned_data['name'],
                }
                lst.subscribe(form.cleaned_data['email'], opt)
                url = request.POST.get('next', DONE_URL)
                # It worked!
                if request.is_ajax():
                    # For ajax, return target URL as plain text
                    return HttpResponse(url, content_type='text/plain')
                return HttpResponseRedirect(url)
            except URLError:
                error_msg = 'Subscription temporarily unavailable'
            except ChimpyException, e:
                # Chimpy library appends too much shit after first colon
                error_msg = unicode(e).split(':')[0]
    messages.error(request, error_msg)
    if request.is_ajax():
        # For ajax, return error message as plain text
        return HttpResponse(error_msg, status=400, content_type='text/plain')
    return HttpResponseRedirect(ERROR_URL)

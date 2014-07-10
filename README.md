django-chump
============

Yet another little app for throwing a MailChimp subscribe form into a Django project

Works with django-mailchimp-v1.3 (specifically)

Required settings --

	MAILCHIMP_API_KEY = '...'

Optional settings --

	MAILCHIMP_LIST_ID = '...'
	MAILCHIMP_DONE_URL = '/thanks/'
	MAILCHIMP_ERROR_URL = '/oops/'
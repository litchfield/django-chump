# Lets place nice and not make any assumptions on style

PREFIXES = [
	'chump/',
	'includes/',
	'inc/',
	'partial/',
]

def get_template_names(template, prefixes=PREFIXES):
	templates = []
	for prefix in prefixes:
		templates.append(prefix + template)
	templates.append(template)
	return templates

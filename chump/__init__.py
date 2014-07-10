PREFIXES = [
	'chump/',
	'includes/',
	'inc/',
	'partial/',
]

def get_template_names(template, prefixes=PREFIXES):
	templates = []
	for prefix in prefixes:
		templates.add(prefix + template)
	templates.add(template)
	return templates

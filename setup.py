from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os

root = os.path.dirname(os.path.abspath(__file__))
os.chdir(root)

VERSION = '0.1'

# Make data go to the right place.
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']


setup(
    name='django-chump',
    version=VERSION,
    description="MailChimp subscribe form for Django",
    long_description="Yet another little app for throwing a MailChimp subscribe form into a Django project",
    author="Simon Litchfield",
    author_email="simon@s29.com.au",
    url="http://github.com/litchfield/django-chump",
    license="MIT License",
    platforms=["any"],
    packages=['chump'],
    install_requires=[
          'django-mailchimp-v1.3==1.3.0',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
)

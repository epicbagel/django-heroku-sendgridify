from setuptools import setup, find_packages
import sendgridify
setup(name='django-heroku-sendgridify',
	version=sendgridify.__version__,
	packages = find_packages(),
	license='The MIT License',
	platforms=['OS Independent'],
	keywords='django, send grid',
	author='Jon Bolt',
	author_email='jon@epicbagel.com',
	url="https://github.com/epicbagel/django-heroku-sendgridify",
)

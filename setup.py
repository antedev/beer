try: 
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Learning Python',
	'author': 'ante',
	'author_email': 'andreas.danielsson@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['learning'],
	'scripts': [],
	'name': 'Dev proj 1'
}

setup(**config)
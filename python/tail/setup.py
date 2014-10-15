try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Implementing tail command in python',
    'author': 'Sayali Lunkad',
    'url': 'https://github.com/sayalilunkad',
    'download_url': 'https://github.com/sayalilunkad/mycodes/archive/master.zip',
    'author_email': 'sayali.92720@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['tail'],
    'scripts': [],
    'name': 'tail'
}

setup(**config)

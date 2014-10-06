try:
        from setuptools import setup
except ImportError:
        from distutils.core import setup

        config = {
                'description': 'Implementing Binary Search Tree',
                'author': 'Sayali Lunkad',
                'url': 'https://github.com/sayalilunkad',
                'download_url': 'https://github.com/sayalilunkad/mycodes/archive/master.zip',
                'author_email': 'sayali.92720@gmail.com',
                'version': '0.1',
                'install_requires': ['nose'],
                'packages': ['bst'],
                'scripts': [],
                'name': 'BinarySearchTree'
        }

        setup(**config)

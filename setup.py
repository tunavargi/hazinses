import os
from setuptools import setup


# allow setup.py to be run from any path

setup(
    name='hazinses',
    version='0.5.2',
    packages=['hazinses'],
    include_package_data=True,
    license='BSD License',
    description='A simple Django app for connecting AMAZON SES-CELERY AND BOTO.',
    author='Tuna VARGI',
    author_email='tunavargi@gmail.com',
    install_requires=['django', 'boto', 'django-celery'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # replace these appropriately if you are using Python 3
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

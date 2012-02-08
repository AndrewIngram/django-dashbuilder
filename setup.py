from setuptools import setup

setup(
    name='django-dashbuilder',
    version='0.0.1',
    url='https://github.com/AndrewIngram/django-dashbuilder',
    description="Views and templates for building a bespoke admin interface for Django",
    long_description=open('README.rst', 'r').read(),
    license="MIT",
    author="Andrew Ingram",
    author_email="andy@andrewingram.net",
    packages=['dashbuilder'],
    package_dir={'': '.'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',   
        'Programming Language :: Python']
)

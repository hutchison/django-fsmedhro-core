import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-fsmedhro-core',
    version='0.3.1',
    packages=find_packages(),
    include_package_data=True,
    description='Basisapp für die Webseite des FSR Medizin der Uni Rostock',
    long_description=README,
    license='MIT License',
    url='https://github.com/hutchison/django-fsmedhro-core',
    install_requires=[
        'Django>=3.1',
        'django-crispy-forms',
        'ldap3>=2.6',
        'djangorestframework',
    ],
    python_requires=">=3.9",
    author='Martin Darmüntzel',
    author_email='martin@trivialanalog.de',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

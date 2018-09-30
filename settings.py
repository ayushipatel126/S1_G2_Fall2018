import os

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp'
]

TEMPLATES = [
    {

        'DIRS': [os.path.join("E:\Masters\Sem 3\Internet Applications and Distributed Systems\Labs\Lab 3\S1_G2_Fall2018",'templates')]

    }
]

DEBUG = True

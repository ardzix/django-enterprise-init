'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# File: local_setting.py
# Project: kur.bri.co.id
# File Created: Tuesday, 5th May 2020 1:52:30 pm
#
# Author: Arif Dzikrullah
#         ardzix@hotmail.com>
#         https://github.com/ardzix/>
#
# Last Modified: Tuesday, 5th May 2020 1:52:31 pm
# Modified By: Arif Dzikrullah (ardzix@hotmail.com>)
#
# Handcrafted and Made with Love - Ardz
# Copyright - 2020 PT Bank Rakyat Indonesia, bri.co.id
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

# Environment
DEBUG = True
PRODUCTION = False
NEWS_ENABLED = False
SECRET_KEY = 'secret'

ALLOWED_HOSTS = ["*"]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'default_db',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
            'NAME': 'default_db_test'
        }
    }
}


# Rackspace
RACKSPACE_CLOUD_FILES = {
    "username": "askme",
    "key": "askme",
    "region": "askme",
    "default_container": "askme",
}

RACKSPACE_BASE_URL = "askme"
USE_RACKSPACE = False


AUTH_USER_MODEL = 'authentication.User'

SITE_ID = 1

BASE_URL = "http://127.0.0.1:8000/"

# Nexmo
NEXMO_API_KEY = "askme"
NEXMO_API_SECRET = "askme"

# SOCIAL AUTH
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_FACEBOOK_KEY = 'askme'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'askme'  # App Secret
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'askme'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'askme'
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = 'askme'  # Client ID
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'askme'  # Client Secret

# recaptcha
RECAPTCHA_SITE_KEY = "askme"
RECAPTCHA_SECRET_KEY = "askme"

# Admin Error
ADMINS = [
    # ("Admin", "admin@kur.bri.co.id"),
    ("Arif", "ardzyix@gmail.com"),
]

IS_CELERY = False
BROKER_URL = "askme"

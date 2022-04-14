from ._secrets import *
from .paths import *
from .apps import *


"""
Resources:

    See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

    https://docs.djangoproject.com/en/4.0/ref/settings/#databases

    https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

    https://docs.djangoproject.com/en/4.0/topics/i18n/

    https://docs.djangoproject.com/en/4.0/howto/static-files/

    https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

"""

DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'config.urls'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Denver'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

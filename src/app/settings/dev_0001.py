from app.settings.components.base import * # noqa

import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECRET_KEY = 'dev secret key'
SECRET_KEY = os.environ['SECRET_KEY']

# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'core.middlewares.TimeLog'
]


LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

# CRISPY_TEMPLATE_PACK = 'bootstrap4'
# LOGIN_REDIRECT_URL = '/'
#
# AUTH_USER_MODEL = 'user_account.User'
#
# MESSAGE_TAGS = {
#     messages.DEBUG: 'alert-info',
#     messages.INFO: 'alert-info',
#     messages.SUCCESS: 'alert-success',
#     messages.WARNING: 'alert-warning',
#     messages.ERROR: 'alert-danger',
# }
#
# SESSION_COOKIE_AGE = 2 * 3600

# FIXTURE_DIRS = (os.path.join(BASE_DIR, 'tests/fixtures'),)


# try:
#     from app.settings_local import *
#     # from app.settings.old.settings_local import *
# except ImportError:
#     pass

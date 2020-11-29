from app.settings.components.base import * # noqa

from app.settings.components.database import * # noqa

# from app.settings.components.email import * # noqa

import os

SECRET_KEY = os.environ['SECRET_KEY']
# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DEBUG = False

print('')


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         # 'NAME': 'prod',
#         # 'HOST': '10.30.0.5',
#         # 'USER': 'admin-prod',
#         # 'PASS': 'passw-prod',
#         'NAME': os.environ['NAME'],
#         'HOST': os.environ['HOST'],
#         'USER': os.environ['USER'],
#         'PASS': os.environ['PASS'],
#     }
# }

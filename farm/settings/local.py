from.base import *

ALLOWED_HOSTS = ['*']


# DATABASES = {
#    'default': {
#     'ENGINE': 'djongo',
#     'NAME': 'product_delivery',
#  }
# }

DATABASES = {
    'default':{
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'product_delivery',
    'USER':     'postgres',
    'PASSWORD': 'ankita',
    'HOST':     'localhost',
    'PORT':     5432,

    }
}

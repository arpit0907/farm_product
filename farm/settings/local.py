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
    'NAME': 'product_farm',
    'USER':     'postgres',
    'PASSWORD': 'psql',
    'HOST':     'localhost',
    'PORT':     5432,

    }
}

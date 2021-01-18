from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['muebleriavasquez.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd98tast1pqbkmd',
        'USER': 'kcjmkruhhlspxe',
        'PASSWORD': 'd65f8373da11d1051fc5c1df8b25faa9dca724db7322caf6b9ec7c731b503d4f',
        'HOST': 'ec2-52-204-20-42.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)



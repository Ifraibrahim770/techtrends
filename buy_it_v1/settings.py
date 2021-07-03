"""
Django settings for buy_it_v1 project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$0f4=_aor-%hugor7+@kmy)5cc_6bxx&-%+=xd*b0-k$w+-t^!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store.apps.StoreConfig',
    'allauth',
    'newstore',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'buy_it_v1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect',  # <--
            ],
        },
    },
]

WSGI_APPLICATION = 'buy_it_v1.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#   'default': {
#    'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#  }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbhidvu24jslrk',
        'HOST': 'ec2-174-129-225-160.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'feqwgasvdpdktq',
        'PASSWORD': '3c516dcb7c25eb53b8164b50a6fa2f2d6a7bc7792be044ba2560ee995c883bb3'

    }
}

# postgres://feqwgasvdpdktq:3c516dcb7c25eb53b8164b50a6fa2f2d6a7bc7792be044ba2560ee995c883bb3@ec2-174-129-225-160.compute-1.amazonaws.com:5432/dbhidvu24jslrk


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'static')
]

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'store/templates/store'),
    os.path.join(BASE_DIR, 'newstore/templates')
]

EMAIL_HOST = '64.233.184.108'
EMAIL_HOST_USER = 'dibaibrahim8@gmail.com'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'dibaibrahim8@gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = 'context99'

EMAIL_ACTIVE_FIELD = 'is_active'
EMAIL_SERVER = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_ADDRESS = 'dibaibrahim8@gmail.com'
EMAIL_PASSWORD = 'context99'  # os.environ['password_key'] suggested
EMAIL_MAIL_SUBJECT = 'Confirm your email'
EMAIL_MAIL_HTML = 'mail_body.html'
EMAIL_MAIL_PLAIN = 'mail_body.txt'
EMAIL_PAGE_TEMPLATE = 'confirm_template.html'
EMAIL_PAGE_DOMAIN = 'http://mydomain.com/'

ACCOUNT_EMAIL_REQUIRED = True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

SITE_ID = 1

SOCIAL_AUTH_FACEBOOK_KEY = '625419248353366'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '08d2ebef6c7e0972bfb3f7231c89483d'
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
    'user_friends',
    'friends_location',
]

LOGIN_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'facebook':
        {'METHOD': 'oauth2',
         'SCOPE': ['email', 'public_profile', 'user_friends'],
         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
         'FIELDS': [
             'id',
             'email',
             'name',
             'first_name',
             'last_name',
             'verified',
             'locale',
             'timezone',
             'link',
             'gender',
             'updated_time'],
         'EXCHANGE_TOKEN': True,
         'LOCALE_FUNC': lambda request: 'kr_KR',
         'VERIFIED_EMAIL': False,
         'VERSION': 'v2.4'},
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }

}
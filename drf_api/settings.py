"""
Django settings for drf_ap project.

Generated by 'django-admin startproject' using Django 3.2.21.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

if os.path.exists('env.py'):
    import env
    print('Import env')

# CLOUDINARY_STORAGE = {
#     'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
# }

CLOUDINARY_URL = 'cloudinary://944931775593423:huq1ZGsG3PII3T1ul4wjH_HozKY@dib6k8rhm'
CLOUDINARY_STORAGE = 'cloudinary://944931775593423:huq1ZGsG3PII3T1ul4wjH_HozKY@dib6k8rhm'
CLOUD_NAME = "my-cloud"
API_KEY = "my-api-key"
API_SECRET = "my-api-secret"

# Standard folder for Django media files
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
# if 'DEV' not in os.environ:
#     REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
#         'rest_framework.renderers.JSONRenderer',
#     ]

REST_USE_JWT = False
JWT_AUTH_SECURE = False
JWT_AUTH_COOKIE = 'jwt-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None',

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv('SECRET_KEY')
SECRET_KEY = "ghghghghgh"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = 'DEV' in os.environ
DEBUG = True

ALLOWED_HOSTS = [
    '8000-jatoad-drfapi-jmeq3hfqsnn.ws-eu106.gitpod.io',
    'full-stack-django-0f48f57393c6.herokuapp.com',
    'localhost',
    'django-full-stack.herokuapp.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://8000-jatoad-drfapi-jmeq3hfqsnn.ws-eu106.gitpod.io',
    'https://full-stack-django-0f48f57393c6.herokuapp.com'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'rest_framework',

    'rest_framework.authtoken',
    'dj_rest_auth', 

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_filters',
    'dj_rest_auth.registration',
    'corsheaders',

    'profiles',
    'drawers',
    'items',
    'likes',
    'followers',

]
SITE_ID = 1
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]
     
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]
else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://.*\.gitpod\.io$",
    ]

    

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'drf_api.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'drf_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# if 'DEV' in os.environ:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
#  else:
#      DATABASES = {
#          'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
#      }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
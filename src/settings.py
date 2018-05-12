import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'QW5kcmV5RWJ1bkxlaGFSYXpyYWJvdGNoaWtCZWtlbmRh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = (
        'x-requested-with',
        'content-type',
        'accept',
        'origin',
        'authorization',
        'x-csrftoken'
)

# CORS_ORIGIN_WHITELIST = (
#     '127.0.0.1:4000',
#     '127.0.0.1:8000',
#     'localhost:4000',
# )


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'djoser',
    'rest_framework_jwt',
    'rest_auth',
    'django.contrib.sites',
    'api'   
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), '/root/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'acey',
#         'USER': 'acey_admin',
#         'PASSWORD': 'ethereum_admin',
#         'HOST': 'localhost',
#         'PORT': ''
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'acey',
    }
}

DEFAULT_FROM_EMAIL = 'nananaBoston@gmail.com'
SERVER_EMAIL = 'nananaBoston@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = '12345678'
EMAIL_HOST_USER = 'nananaBoston@gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

TEMPLATE_DIRS = (
    '/root/',
)



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR,
)

# STATICFILES_STORAGE = 'whitenoise.django.CompressedManifestStaticFilesStorage'
# WHITENOISE_ROOT = os.path.join(PROJECT_DIR, 'staticfiles', 'root') 

MEDIA_ROOT = '/user_pictures/'

REST_FRAMEWORK = {}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'api.serializers.UserSerializer'
}

JWT_AUTH = {
    'JWT_GET_USER_SECRET_KEY': 'api.models.jwt_get_secret_key',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes = 15),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days = 1),
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

CORS_ALLOW_CREDENTIALS = True

# REST_USE_JWT = True

SITE_ID = 1

# import django_heroku
# django_heroku.settings(locals())
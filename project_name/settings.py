from configurations import Configuration, values, importer

import djcelery

import os

# Importer needed for Celery
importer.install()

class Development(Configuration):
    """
    Django settings for {{ project_name }} project.

    """
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    ADMINS = (
        ('Full name', 'admin@example.com'),
    )
    MANAGERS = ADMINS

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '{{ secret_key }}'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = []

    # Email
    DEFAULT_FROM_EMAIL = "{{ project_name}} <hello@example.com>"
    SERVER_EMAIL = "{{ project_name }} <errors@example.com>"

    # We use 1025 as the port because we can use the Python mail server for
    # debugging. Run the following command an the command line:
    #
    #    python -m smtpd -n -c DebuggingServer 127.0.0.1:1025
    #
    EMAIL_PORT = 1025

    # Application definition
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Utility applications
        'configurations',
        'django_extensions',
        'south',
        'debug_toolbar',
        'compressor',

        # Celery
        'djcelery',
        'kombu.transport.django',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    ROOT_URLCONF = '{{ project_name }}.urls'

    WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # Internationalization
    # https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Locale translation files
    LOCALE_PATHS = (
        os.path.join(BASE_DIR, '../locale'),
    )

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, '../public/static')
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    # Media files
    MEDIA_ROOT = os.path.join(BASE_DIR, '../public/media')
    MEDIA_URL = '/media/'

    # Templates
    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates'),
    )

    # Debug toolbar
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
    
    # Celery
    djcelery.setup_loader()
    BROKER_URL = 'django://'
    CELERY_ALWAYS_EAGER = True

    # Compression
    COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.SlimItFilter']
    COMPRESS_OUTPUT_DIR = "cache"

    # We use the compression method of content because this works better when
    # you have multiple application servers.
    COMPRESS_CSS_HASHING_METHOD = 'content'

class Production(Development):
    """
    Production settings.

    """
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG

    # Empty by design to trigger a warning to fill it with something sensible.
    SECRET_KEY = values.SecretValue()

    # Switch the Celery broker URL to RabbitMQ
    BROKER_URL = 'amqp://guest:guest@localhost:5672//'
    CELERY_ALWAYS_EAGER = False

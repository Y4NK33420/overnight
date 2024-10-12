# edating_platform/settings.py

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your_secret_key'  # Replace with your actual secret key

DEBUG = True  # Set to False in production

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    # Default Django apps...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Our custom app
    'accounts.apps.AccountsConfig',  # Use the app config to load signals
]

MIDDLEWARE = [
    # Default middleware...
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'e_dating_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Templates directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Default context processors...
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required for auth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'e_dating_platform.wsgi.application'

# Database configuration (default is SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation (default settings)
AUTH_PASSWORD_VALIDATORS = [
    # ... (You can keep the default validators)
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # URL to use when referring to static files

# Directories where Django will look for static files in development
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Your project-level static directory
]

# This is the directory where Django will collect all static files
# when you run the 'collectstatic' command in production
STATIC_ROOT = BASE_DIR / "staticfiles"

# Ensure STATIC_ROOT is properly configured for production
# Django will copy all static files from STATICFILES_DIRS to STATIC_ROOT


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Messages framework configuration
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}

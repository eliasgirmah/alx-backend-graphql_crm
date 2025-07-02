
<<<<<<< HEAD

=======
>>>>>>> 275468b69b688680d4983880ca426f02ac258e14
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
<<<<<<< HEAD
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z1r#@+=r+%h=r^8=!&to9vrbjy76rioy5wi-y+hwj@kwe#tfov'
=======
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--g996synogh$2g7tg@g(5tnp$f238m=ll+wct_&ci7%opu)9(s'
>>>>>>> 275468b69b688680d4983880ca426f02ac258e14

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'crm',  # Your CRM app
    'graphene_django',  # GraphQL library
    'django_filters',
=======
    'crm',
    'graphene_django',
>>>>>>> 275468b69b688680d4983880ca426f02ac258e14
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'alx_backend_graphql_crm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
<<<<<<< HEAD
                'django.template.context_processors.debug',
=======
>>>>>>> 275468b69b688680d4983880ca426f02ac258e14
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'alx_backend_graphql_crm.wsgi.application'


# Database
<<<<<<< HEAD
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
=======
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
>>>>>>> 275468b69b688680d4983880ca426f02ac258e14

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
<<<<<<< HEAD
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
=======
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
>>>>>>> 275468b69b688680d4983880ca426f02ac258e14

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
<<<<<<< HEAD
# https://docs.djangoproject.com/en/5.1/topics/i18n/
=======
# https://docs.djangoproject.com/en/5.2/topics/i18n/
>>>>>>> 275468b69b688680d4983880ca426f02ac258e14

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
<<<<<<< HEAD
# https://docs.djangoproject.com/en/5.1/howto/static-files/
=======
# https://docs.djangoproject.com/en/5.2/howto/static-files/
>>>>>>> 275468b69b688680d4983880ca426f02ac258e14

STATIC_URL = 'static/'

# Default primary key field type
<<<<<<< HEAD
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

=======
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


>>>>>>> 275468b69b688680d4983880ca426f02ac258e14
GRAPHENE = {
    'SCHEMA': 'alx_backend_graphql_crm.schema.schema'
}

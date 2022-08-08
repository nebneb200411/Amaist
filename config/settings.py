"""
Django settings for WebApp project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# メディアの設定
MEDIA_URL = '/media/'

# staticファイルの読み込み
STATIC_URL = '/static/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#ALLOWED_HOSTS = ['66.42.44.44', 'amaist-service.com']

try:
    from .local_settings import *
except ImportError:
    pass


if not DEBUG:
    import environ
    env = environ.Env()
    env.read_env(os.path.join(BASE_DIR, '.env'))

    SECRET_KEY = env('SECRET_KEY')
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = 'rhxkwasvmumhnutc'
    EMAIL_USE_TLS = True

    STATIC_ROOT = '/usr/share/nginx/html/static'
    MEDIA_ROOT = '/usr/share/nginx/html/media'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

# Application definition
# 上から順に読み込まれるので注意
INSTALLED_APPS = [
    'notifications',
    'ckeditor',
    'ckeditor_uploader',
    'question',
    'profiles',
    'data_library',
    'article',
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'data_library.templatetags.filename',
    'django_cleanup',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    #'django_summernote',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
ROOT_URLCONF = 'config.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # os.path.join(BASE_DIR, 'templates')
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# connect to emailsurver
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreply.datalabo@gmail.com'
EMAIL_HOST_PASSWORD = 'rhxkwasvmumhnutc'
EMAIL_USE_TLS = True
DEFAUL_FROM_EMAIL = 'noreply.datalabo@gmail.com'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


# 本プロジェクトで用いるユーザーモデル
AUTH_USER_MODEL = 'registration.User'

# ログイン成功時のURLおよび，ログアウト後のURL
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

X_FRAME_OPTIONS = 'SAMEORIGIN'

# global variables which we can use through this project
ARTICLE_GENRE_CHOICES = {
    '1':'AI',
    '2':'機械学習', 
    '4':'ディープラーニング',
    '5':'強化学習',
    '6':'確率統計',
    '7':'データ分析', 
    '8':'その他',
}

# site maps
SITE_ID = 1

CKEDITOR_UPLOAD_PATH = "ckeditor/"

CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False

CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_BROWSE_SHOW_DIRS = True

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_CONFIGS = {

    'default': {
        # css path
        #'contentsCss': os.path.join(BASE_DIR, '/static/ckeditor/ckeditor.css'),

        'width': '100%',
        'skin': 'moono-lisa',
        #'codeSnippet_theme': 'ir_black',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_Custom': [
            #{'name': 'document', 'items': [
                #'Source', '-', 'NewPage', 'Save', 'Preview', 'Print', '-', 'Templates']},
            #{'name': 'clipboard', 'items': [
                #'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            #{'name': 'editing', 'items': [
                #'Find', 'Replace', '-', 'SelectAll']},
            #{'name': 'forms',
             #'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       #'HiddenField']},
            #'/',
            {'name': 'styles', 'items': [
                'Format', 'Font', 'FontSize','lineheight']},
            {'name': 'basicstyles',
             'items': ['TextColor', 'BGColor', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                        'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', ]},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            '/',
            {'name': 'insert',
                'items': ['Table', 'HorizontalRule', 'SpecialChar', 'Iframe', '-', 'RemoveFormat', 'pbckcode']},
            {'name': 'mathtools', 'items': ['Mathjax']},
            {'name': 'tools', 'items': ['Maximize']},
            {'name': 'about', 'items': ['About', 'Source', 'Image']},
        ],
        'toolbar': 'Custom',
        #x'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            #'image2', 
            'balloonpanel',
            'balloontoolbar',
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'pbckcode',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'codesnippet',
            'ckeditor_wiris',
            #'MathType',
            #'ChemType',
            'mathjax',
            'uicolor',
            'lineheight',
            'contents',
        ]),

        'allowedContent': True,
    },

    ### pbckcode ###
}

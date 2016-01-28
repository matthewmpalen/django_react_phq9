from os.path import abspath, basename, dirname, join, normpath

BASE_DIR = dirname(dirname(abspath(__file__)))
SECRET_KEY = 'am0s!v$(v*iud7rd19!u)+dxzxj&%!11s**4wehsp%dz9)%xn('
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
    # External
    #'pipeline', 
    'rest_framework', 
    # Local
    'django_phq9_screener', 
    'django_phq9_screener.questionnaire'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_phq9_screener.urls'

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

WSGI_APPLICATION = 'django_phq9_screener.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
#STATIC_ROOT = normpath(join(dirname(BASE_DIR), 'static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    join(BASE_DIR, 'static'), 
)
#STATICFILES_DIRS = ()

# External
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication', 
        'rest_framework.authentication.SessionAuthentication'
    ), 
    'DEFAULT_MODEL_SERIALIZER_CLASS': (
        'rest_framewor.serializers.HyperlinkModelSerializer', 
    ), 
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly', 
    )
}

"""
# django-pipeline
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder', 
    'django.contrib.staticfiles.finders.AppDirectoriesFinder', 
    'pipeline.finders.PipelineFinder'
)

# browserify
PIPELINE = {
    'PIPELINE_ENABLED': True, 
    'COMPILERS': (
        'pipeline_browserify.compiler.BrowserifyCompiler', 
    ), 
    'CSS_COMPRESSOR': 'pipeline.compressors.NoopCompressor', 
    'JS_COMPRESSOR': 'pipeline.compressors.uglifyjs.UglifyJSCompressor', 
    'JAVASCRIPT': {
        'phq9_screener_js': {
            'source_filenames': (
                'bower_components/jquery/dist/jquery.min.js', 
                'bower_components/react/JSXTransformer.js', 
                'bower_components/react/react-with-addons.js' 
            ), 

            'output_filename': 'phq9_site.js'
        } 
    }
}

if DEBUG:
    PIPELINE['BROWSERIFY_ARGUMENTS'] = '-t [ babelify --presets [ react ] ]'
"""

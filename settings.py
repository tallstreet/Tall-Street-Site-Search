# -*- coding: utf-8 -*-
from ragendja.settings_pre import *

DEFAULT_FROM_EMAIL = "tallstreet@gmail.com"

ADMINS = (
	('Gary', 'tallstreet@gmail.com'),
)
MANAGERS = ADMINS
# Increase this when you update your media on the production site, so users
# don't have to refresh their cache. By setting this your MEDIA_URL
# automatically becomes /media/MEDIA_VERSION/
MEDIA_VERSION = 1

# Make this unique, and don't share it with anybody.
SECRET_KEY = '1234567890'

#ENABLE_PROFILER = True
#ONLY_FORCED_PROFILE = True
#PROFILE_PERCENTAGE = 25
#SORT_PROFILE_RESULTS_BY = 'cumulative' # default is 'time'
#PROFILE_PATTERN = 'ext.db..+\((?:get|get_by_key_name|fetch|count|put)\)'

# Enable I18N and set default language to 'en'
USE_I18N = True
LANGUAGE_CODE = 'en'
#DEBUG = True

#Restrict supported languages (and JS media generation)
_ = lambda s: s

LANGUAGES = (
    ('en', _('English')),
)

# Combine media files
COMBINE_MEDIA = {
    # Create a combined JS file which is called "combined-en.js" for English,
    # "combined-de.js" for German, and so on
    'combined-%(LANGUAGE_CODE)s.js': (
    ),
    # Create a combined CSS file which is called "combined-ltr.css" for
    # left-to-right text direction
    'combined-%(LANGUAGE_DIR)s.css': (
        'global/css/style.css',
    ),
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    "grappelli.context_processors.admin_url",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Django authentication
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    # Google authentication
    'ragendja.auth.middleware.GoogleAuthenticationMiddleware',
    # Hybrid Django/Google authentication
    #'ragendja.auth.middleware.HybridAuthenticationMiddleware',
    #'ragendja.middleware.LoginRequiredMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    #'ragendja.sites.dynamicsite.DynamicSiteIDMiddleware',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

# Google authentication
AUTH_USER_MODULE = 'ragendja.auth.google_models'
AUTH_ADMIN_MODULE = 'ragendja.auth.google_admin'
# Hybrid Django/Google authentication
#AUTH_USER_MODULE = 'ragendja.auth.hybrid_models'

GLOBALTAGS = (
    'ragendja.templatetags.ragendjatags',
    'django.templatetags.i18n',
    'search.templatetags.searchtags',
)

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ADMIN_URL = 'settings'

INSTALLED_APPS = (
    #'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
    'grappelli',
    #'django.contrib.webdesign',
    #'django.contrib.flatpages',
    #'django.contrib.redirects',
    #'django.contrib.sites',
    'appenginepatcher',
    'search',
    'mediautils',
)

# List apps which should be left out from app settings and urlsauto loading
IGNORE_APP_SETTINGS = IGNORE_APP_URLSAUTO = (
    # Example:
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'yetanotherapp',
)

CACHE_BACKEND = 'memcached://'


# Remote access to production server (e.g., via manage.py shell --remote)
DATABASE_OPTIONS = {
    # Override remoteapi handler's path (default: '/remote_api').
    # This is a good idea, so you make it not too easy for hackers. ;)
    # Don't forget to also update your app.yaml!
    'remote_url': '/remote_api',

    # !!!Normally, the following settings should not be used!!!

    # Always use remoteapi (no need to add manage.py --remote option)
    #'use_remote': True,

    # Change appid for remote connection (by default it's the same as in your app.yaml)
    #'remote_id': 'otherappid',

    # Change domain (default: <remoteid>.appspot.com)
    #'remote_host': 'bla.com',
}

from ragendja.settings_post import *

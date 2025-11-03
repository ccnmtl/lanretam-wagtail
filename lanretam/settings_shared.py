# Django settings for lanretam project.
import os.path
from ctlsettings.shared import common

project = 'lanretam'
base = os.path.dirname(__file__)

locals().update(common(project=project, base=base))

PROJECT_APPS = [
    'lanretam.main',
]

USE_TZ = True

MIDDLEWARE += [  # noqa
    'wagtail.contrib.legacy.sitemiddleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS += [  # noqa
    'bootstrap4',
    'django_extensions',
    'debug_toolbar',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.styleguide',
    'wagtail.contrib.table_block',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'modelcluster',
    'taggit',
    'wagtailfontawesome',

    'lanretam.main',
]

THUMBNAIL_SUBDIR = "thumbs"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/cms/"

WAGTAIL_SITE_NAME = 'Lanretam'
WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login/'
PASSWORD_REQUIRED_TEMPLATE = 'main/login/password_required.html'  # nosec

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

WIND_AFFIL_HANDLERS = ['lanretam.main.auth.WagtailEditorMapper']

WAGTAILADMIN_STATIC_FILE_VERSION_STRINGS = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(base, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'stagingcontext.staging_processor',
                'ctlsettings.context_processors.env',
                'gacontext.ga_processor',
            ],
        },
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

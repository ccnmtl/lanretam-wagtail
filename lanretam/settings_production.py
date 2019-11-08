# flake8: noqa
from lanretam.settings_shared import *
from ccnmtlsettings.production import common
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

locals().update(
    common(
        project=project,
        base=base,
        STATIC_ROOT=STATIC_ROOT,
        INSTALLED_APPS=INSTALLED_APPS,
# if you use cloudfront:
#        cloudfront="justtheidhere",
# if you don't use S3/cloudfront at all:
#       s3static=False,
    ))

try:
    from lanretam.local_settings import *
except ImportError:
    pass

if hasattr(settings, 'SENTRY_DSN'):
￼   sentry_sdk.init(
￼       dsn=SENTRY_DSN,
￼       integrations=[DjangoIntegration()],
￼   )

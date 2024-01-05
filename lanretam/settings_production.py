import sys
from lanretam.settings_shared import *  # noqa f403
from ctlsettings.production import common
from django.conf import settings
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

locals().update(
    common(
        project=project,  # noqa f405
        base=base,  # noqa f405
        STATIC_ROOT=STATIC_ROOT,  # noqa f405
        INSTALLED_APPS=INSTALLED_APPS,  # noqa f405
        s3prefix="ccnmtl",
    ))

try:
    from lanretam.local_settings import *  # noqa f403
except ImportError:
    pass

if ('collectstatic' not in sys.argv) and hasattr(settings, 'SENTRY_DSN'):
    sentry_sdk.init(
        dsn=SENTRY_DSN,  # noqa: F405
        integrations=[DjangoIntegration()],
    )

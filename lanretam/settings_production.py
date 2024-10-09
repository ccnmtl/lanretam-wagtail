from lanretam.settings_shared import *  # noqa f403
from ctlsettings.production import common, init_sentry
from django.conf import settings

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

if hasattr(settings, 'SENTRY_DSN'):
    init_sentry(SENTRY_DSN)  # noqa F405

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.views.static import serve
import os.path
# from portfolio.main.views import S3DocumentServe

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

site_media_root = os.path.join(os.path.dirname(__file__), "../media")

auth_urls = path('accounts/', include('django.contrib.auth.urls'))

urlpatterns = [
    auth_urls,
    path('admin/', admin.site.urls),
    path('stats/', TemplateView.as_view(template_name="stats.html")),
    path('smoketest/', include('smoketest.urls')),
    path('infranil/', include('infranil.urls')),
    re_path(r'^uploads/(?P<path>.*)$',
            serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'', include(wagtail_urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

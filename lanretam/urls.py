from django.urls import include, path, re_path
from django.contrib import admin
from django.contrib.auth.views import logout
from django.conf import settings
from django.views.generic import TemplateView
from django.views.static import serve
import os.path
# from portfolio.main.views import S3DocumentServe
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

site_media_root = os.path.join(os.path.dirname(__file__), "../media")

redirect_after_logout = getattr(settings, 'LOGOUT_REDIRECT_URL', None)
auth_urls = path('accounts/', include('django.contrib.auth.urls'))
logout_page = path(
    'accounts/logout/',
    logout,
    {'next_page': redirect_after_logout})
if hasattr(settings, 'CAS_BASE'):
    from djangowind.views import logout as windlogout
    auth_urls = path('accounts/', include('djangowind.urls'))
    logout_page = path(
        'accounts/logout/',
        windlogout,
        {'next_page': redirect_after_logout})

urlpatterns = [
    auth_urls,
    logout_page,
    path('admin/', admin.site.urls),
    path('stats/', TemplateView.as_view(template_name="stats.html")),
    path('smoketest/', include('smoketest.urls')),
    path('infranil/', include('infranil.urls')),
    re_path(r'^uploads/(?P<path>.*)$',
            serve, {'document_root': settings.MEDIA_ROOT}),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('', include(wagtail_urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

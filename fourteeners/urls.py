from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'apps.accounts.views.create', name='home'),
    url(r'^accounts/', include('apps.accounts.urls', namespace='accounts')),
    url(r'^mountains/', include('apps.mountains.urls', namespace='mountains')),
    url(r'^login/', RedirectView.as_view(url='/accounts/login', permanent=False)),

    # Plugins
    url(r'^foundation/', include('apps.foundation.urls', namespace='foundation')),
)

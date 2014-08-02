from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
from django.conf import settings

from paintr import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'planetofpaint2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.map_view),
    url(r'^mobile$', views.map_view_mobile),
    url(r'^go$', views.tracker_view),
    url(r'^brush$', views.brush_view),
    url(r'^paintr/api/data/get$', views.get_data),
    url(r'^paintr/api/create$', views.create_canvas),
    url(r'^paintr/api/send$', views.receive_data),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

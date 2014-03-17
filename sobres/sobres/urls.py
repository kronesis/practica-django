from django.conf.urls import patterns, include, url
from isobres.views import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sobres.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', mainpage, name='home'),
	url(r'^user/(\w+)/$', userpage),
	url(r'^login/$','django.contrib.auth.views.login'),

)

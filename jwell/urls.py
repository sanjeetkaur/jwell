from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'front.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'front.views.index', name='index'),
    url(r'^jwell/', include('front.urls')),
    url(r'^bills/', include('bills.urls')), 
    url(r'^$', 'bills.views.bil_index', name='bil_index'),
    url(r'^admin/', include(admin.site.urls)),

)


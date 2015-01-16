from django.conf.urls import patterns, url

from bills import views

urlpatterns = patterns('',
    url(r'^$', views.bil_index, name='bil_index'),
)

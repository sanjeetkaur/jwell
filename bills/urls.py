from django.conf.urls import patterns, url

from bills import views

urlpatterns = patterns('',
    url(r'^bill/', views.bil_index),
    url(r'^bill/', views.bill),
)

from django.conf.urls import patterns, url

from leads import views

urlpatterns = patterns('',
    url(r'^talk-with-us/$', views.talk_with_us, name='talk_with_us'),
    url(r'^register/$', views.register, name='register'),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import HomeView
urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(),
                           name='index'),
                       url(r'^coaches/', include('coaches.urls')),
                       url(r'^courses/', include('courses.urls')),
                       url(r'^students/', include('students.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )

from django.conf.urls import patterns, url
from coaches.views import CoachesList, CoachView, CoachEdit,\
    CoachAdd, CoachDelete

urlpatterns = patterns('',

                       url(r'^$', CoachesList.as_view(), name="coaches-list"),
                       url(r'^add/$', CoachAdd.as_view(), name="coach-add"),
                       url(r'^edit/(?P<pk>\d+)/$', CoachEdit.as_view(),
                           name="coach-edit"),
                       url(r'^delete/(?P<pk>\d+)/$', CoachDelete.as_view(),
                           name="coach-delete"),
                       url(r'^(?P<pk>\d+)/$', CoachView.as_view(),
                           name="coach-item"),
                       )


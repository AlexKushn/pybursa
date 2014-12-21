from django.conf.urls import patterns, include, url
from coaches.views import coaches_list, coaches_item, coach_edit, coach_add, coach_delete

urlpatterns = patterns('',

                       url(r'^$', coaches_list, name="coaches-list"),
                       url(r'^add/$', coach_add, name="coach-add"),
                       url(r'^edit/(?P<coach_id>\d+)/$', coach_edit,
                           name="coach-edit"),
                       url(r'^delete/(?P<coach_id>\d+)/$', coach_delete,
                           name="coach-delete"),
                       url(r'^(?P<coach_id>\d+)/$', coaches_item,
                           name="coach-item"),
                       )


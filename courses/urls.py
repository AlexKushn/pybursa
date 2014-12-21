from django.conf.urls import patterns, include, url
from courses.views import courses_list, courses_item, course_edit, course_add, course_delete

urlpatterns = patterns('',

                       url(r'^$', courses_list, name="courses-list"),
                       url(r'^add/$', course_add, name="course-add"),
                       url(r'^edit/(?P<course_id>\d+)/$', course_edit,
                           name="course-edit"),
                       url(r'^delete/(?P<course_id>\d+)/$', course_delete,
                           name="course-delete"),
                       url(r'^(?P<course_id>\d+)/$', courses_item,
                           name="course-item"),
                       )


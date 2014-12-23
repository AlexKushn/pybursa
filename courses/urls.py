from django.conf.urls import patterns, url
from courses.views import CoursesList, CourseView, CourseEdit,\
    CourseAdd, CourseDelete


urlpatterns = patterns('',

                       url(r'^$', CoursesList.as_view(), name="courses-list"),
                       url(r'^add/$', CourseAdd.as_view(), name="course-add"),
                       url(r'^edit/(?P<pk>\d+)/$', CourseEdit.as_view(),
                           name="course-edit"),
                       url(r'^delete/(?P<pk>\d+)/$', CourseDelete.as_view(),
                           name="course-delete"),
                       url(r'^(?P<pk>\d+)/$', CourseView.as_view(),
                           name="course-item"),
                       )


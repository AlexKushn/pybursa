from django.conf.urls import patterns, include, url
from students.views import students_list, students_item, student_edit, student_add, student_delete

urlpatterns = patterns('',

                       url(r'^$', students_list, name="students-list"),
                       url(r'^add/$', student_add, name="student-add"),
                       url(r'^edit/(?P<student_id>\d+)/$', student_edit,
                           name="student-edit"),
                       url(r'^delete/(?P<student_id>\d+)/$', student_delete,
                           name="student-delete"),
                       url(r'^(?P<student_id>\d+)/$', students_item,
                           name="student-item"),
                       )


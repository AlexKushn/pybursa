from django.shortcuts import render
from students.models import Student


def students_list(request):
    students = Student.objects.all()
    page_title = 'students list'
    return render(request, 'students/list.html', {'students': students,
                                                  'title': page_title})


def students_item(request, student_id):
    student = Student.objects.get(id=student_id)
    page_title = 'student item'
    return render(request, 'students/item.html', {'student': student,
                                                  'title': page_title})
from django.shortcuts import render
from courses.models import Course


def courses_list(request):
    courses = Course.objects.all()
    page_title = 'courses list'
    return render(request, 'courses/list.html', {'courses': courses,
                                                 'title': page_title})


def courses_item(request, course_id):
    course = Course.objects.get(id=course_id)
    page_title = 'course item'
    return render(request, 'courses/item.html', {'course': course,
                                                 'title': page_title})
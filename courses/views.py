from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from courses.models import Course


class CourseModelForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Course
        fields = ['name', 'slug', 'description', 'lecturer', 'assistant', 'date_of_start',
                  'date_of_end', 'technology', "venue"]
        widgets = {
            'technology': forms.RadioSelect
        }


def courses_list(request):
    courses = Course.objects.all()
    page_title = 'courses list'
    return render(request, 'courses/list.html', {'courses': courses,
                                                 'title': page_title})


def courses_item(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    page_title = 'course item'
    return render(request, 'courses/item.html', {'course': course,
                                                 'title': page_title})


def course_edit(request, course_id):
    title = "Course edit item"
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            return redirect('course-edit', course.id)
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html',
                  {'form': form, 'title': title})


def course_add(request):
    title = "Course add item"
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('course-edit', course.id)
    else:
        form = CourseModelForm()
    return render(request, 'courses/edit.html',
                  {'form': form, 'title': title})


def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect('courses-list')
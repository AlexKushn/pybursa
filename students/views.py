# coding=utf-8

from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django import forms
from students.models import Student, Dossier, Course


import logging
logger = logging.getLogger(__name__)


class StudentForm(forms.Form):
    CHOICES = (
              ('S', 'Standard'),
              ('G', 'Gold'),
              ('V', 'Vip'),
    )
    student_name = forms.CharField(max_length=100, label=_('Name'))
    student_surname = forms.CharField(max_length=255, label=_('Surname'))
    student_date_of_birth = forms.DateField(label=_('Date of birth'))
    student_email = forms.EmailField(label=_('Email'))
    student_phone = forms.CharField(max_length=15, label=_('Phone'))
    student_course = forms.ModelMultipleChoiceField(Course.objects.all(),
                                                    label=_('Course'))
    student_package = forms.ChoiceField(widget=forms.RadioSelect,
                                        choices=CHOICES, label=_('Package'))
    student_dossier = forms.ModelChoiceField(Dossier.objects.all(),
                                             required=False, label=_('Dossier'))


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'course',
                  'package', 'dossier']
        widgets = {
            'package': forms.RadioSelect,
            'courses': forms.CheckboxSelectMultiple,
        }


def students_list(request):
    students = Student.objects.all()
    page_title = _('Students list')
    return render(request, 'students/list.html', {'students': students,
                                                  'title': page_title})


def students_item(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    page_title = _('Student item')
    return render(request, 'students/item.html', {'student': student,
                                                  'title': page_title})


def student_edit(request, student_id):
    title = _("Student edit item")
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student.name = form.cleaned_data['student_name']
            student.surname = form.cleaned_data['student_surname']
            student.date_of_birth = form.cleaned_data['student_date_of_birth']
            student.email = form.cleaned_data['student_email']
            student.phone = form.cleaned_data['student_phone']
            student.course = form.cleaned_data['student_course']
            student.package = form.cleaned_data['student_package']
            student.dossier = form.cleaned_data['student_dossier']\
                if form.cleaned_data['student_dossier'] else None

            try:
                student.save()
                messages.success(request, _(student.name + " details updated!"))
            except:
                messages.error(request, _("Update error!"))
        storage = messages.get_messages(request)
        for message in storage:
            logger.debug(message)
        return redirect('student-edit', student.id)
    else:
        form = StudentForm(initial={'student_name': student.name,
                                    'student_surname': student.surname,
                                    'student_date_of_birth': student.date_of_birth,
                                    'student_email': student.email,
                                    'student_phone': student.phone,
                                    'student_course': student.course.all,
                                    'student_package': student.package,
                                    'student_dossier': student.dossier,
                                    })
    return render(request, 'students/edit.html', {'form': form, 'title': title})


def student_add(request):
    title = _("Student add item")
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            try:
                student = form.save()
                messages.success(request, _(student.name + " add successfully!"))
            except:
                messages.error(request, _("Profile add error!"))
        storage = messages.get_messages(request)
        for message in storage:
            logger.debug(message)
        return redirect('student-edit', student.id)
    else:
        form = StudentModelForm()
    return render(request, 'students/edit.html',
                  {'form': form, 'title': title})


def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    try:
        student.delete()
        messages.success(request, _(student.name + " delete successfully!"))
    except:
        messages.error(request, _("Profile delete error!"))
    storage = messages.get_messages(request)
    for message in storage:
        logger.debug(message)
    return redirect('students-list')
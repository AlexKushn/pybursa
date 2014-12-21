from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from students.models import Student, Dossier, Course


class StudentForm(forms.Form):
    CHOICES = (
              ('S', 'Standard'),
              ('G', 'Gold'),
              ('V', 'Vip'),
    )
    student_name = forms.CharField(max_length=100)
    student_surname = forms.CharField(max_length=255)
    student_date_of_birth = forms.DateField()
    student_email = forms.EmailField()
    student_phone = forms.CharField(max_length=15)
    student_course = forms.ModelMultipleChoiceField(Course.objects.all())
    student_package = forms.ChoiceField(widget=forms.RadioSelect,
                                        choices=CHOICES)
    student_dossier = forms.ModelChoiceField(Dossier.objects.all(),
                                             required=False)


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
    page_title = 'students list'
    return render(request, 'students/list.html', {'students': students,
                                                  'title': page_title})


def students_item(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    page_title = 'student item'
    return render(request, 'students/item.html', {'student': student,
                                                  'title': page_title})


def student_edit(request, student_id):
    title = "Student edit item"
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
            student.save()
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
    title = "Student add item"
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student-edit', student.id)
    else:
        form = StudentModelForm()
    return render(request, 'students/edit.html',
                  {'form': form, 'title': title})


def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('students-list')
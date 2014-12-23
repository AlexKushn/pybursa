from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django import forms

from courses.models import Course


class CourseModelForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Course
        fields = ['name', 'slug', 'description', 'lecturer', 'assistant',
                  'date_of_start', 'date_of_end', 'technology', "venue"]
        widgets = {
            'technology': forms.RadioSelect
        }


class CourseView(DetailView):
    template_name = 'courses/item.html'
    model = Course


class CoursesList(ListView):
    template_name = 'courses/list.html'
    model = Course
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super(CoursesList, self).get_context_data(**kwargs)
        context['title'] = 'Courses list'
        return context


class CourseAdd(CreateView):
    template_name = 'courses/edit.html'
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('courses-list')

    def get_context_data(self, **kwargs):
        context = super(CourseAdd, self).get_context_data(**kwargs)
        context['title'] = 'Course add item'
        return context


class CourseEdit(UpdateView):
    template_name = 'courses/edit.html'
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('courses-list')

    def get_context_data(self, **kwargs):
        context = super(CourseEdit, self).get_context_data(**kwargs)
        context['title'] = 'Course update item'
        return context


class CourseDelete(DeleteView):
    template_name = 'courses/delete.html'
    model = Course
    success_url = reverse_lazy('courses-list')

    def get_context_data(self, **kwargs):
        context = super(CourseDelete, self).get_context_data(**kwargs)
        context['title'] = 'Course delete item'
        return context
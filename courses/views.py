# coding=utf-8

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django import forms

from courses.models import Course

import logging
logger = logging.getLogger(__name__)


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
        context['title'] = _('Courses list')
        return context


class CourseAdd(CreateView):
    template_name = 'courses/edit.html'
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('courses-list')

    def form_valid(self, form):
        try:
            course = form.save()
            messages.success(self.request, _(course.name + " added successfully!"))
        except:
            messages.error(self.request, _("Add error."))
        storage = messages.get_messages(self.request)
        for message in storage:
            logger.debug(message)
        return super(CourseAdd, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CourseAdd, self).get_context_data(**kwargs)
        context['title'] = _('Course add item')
        return context


class CourseEdit(UpdateView):
    template_name = 'courses/edit.html'
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('courses-list')

    def form_valid(self, form):
        try:
            course = form.save()
            messages.success(self.request, _(course.name + " updated successfully!"))
        except:
            messages.error(self.request, _("Update error."))
        storage = messages.get_messages(self.request)
        for message in storage:
            logger.debug(message)
        return super(CourseEdit, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CourseEdit, self).get_context_data(**kwargs)
        context['title'] = _('Course update item')
        return context


class CourseDelete(DeleteView):
    template_name = 'courses/delete.html'
    model = Course
    success_url = reverse_lazy('courses-list')

    def delete(self, request, *args, **kwargs):
        try:
            course = self.get_object()
            course.delete()
            messages.success(self.request, _(course.name + " deleted successfully!"))
        except:
            messages.error(self.request, _("Delete error."))
        storage = messages.get_messages(self.request)
        for message in storage:
            logger.debug(message)
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(CourseDelete, self).get_context_data(**kwargs)
        context['title'] = _('Course delete item')
        return context
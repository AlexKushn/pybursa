# coding=utf-8

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django import forms

from coaches.models import Coach

import logging
logger = logging.getLogger(__name__)


class CoachModelForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Coach
        fields = ['name', 'surname', 'date_of_birth', 'email', 'phone',
                  'teacher', 'user', 'dossier']


class CoachView(DetailView):
    template_name = 'coaches/item.html'
    model = Coach


class CoachesList(ListView):
    template_name = 'coaches/list.html'
    model = Coach
    context_object_name = 'coaches'

    def get_context_data(self, **kwargs):
        context = super(CoachesList, self).get_context_data(**kwargs)
        context['title'] = _('Coaches list')
        return context


class CoachAdd(CreateView):
    template_name = 'coaches/edit.html'
    model = Coach
    form_class = CoachModelForm
    success_url = reverse_lazy('coaches-list')

    def form_valid(self, form):
        try:
            coach = form.save()
            messages.success(self.request, _(coach.name + " added successfully!"))
        except:
            messages.error(self.request, _("Add error."))
        storage = messages.get_messages(self.request)
        for message in storage:
            logger.debug(message)
        return super(CoachAdd, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CoachAdd, self).get_context_data(**kwargs)
        context['title'] = _('Coach add item')
        return context


class CoachEdit(UpdateView):
    template_name = 'coaches/edit.html'
    model = Coach
    form_class = CoachModelForm
    success_url = reverse_lazy('coaches-list')

    def form_valid(self, form):
        try:
            coach = form.save()
            messages.success(self.request, _(coach.name + " updated successfully!"))
        except:
            messages.error(self.request, _("Update error."))
        storage = messages.get_messages(self.request)
        for message in storage:
            logger.debug(message)
        return super(CoachEdit, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CoachEdit, self).get_context_data(**kwargs)
        context['title'] = _('Coach update item')
        return context


class CoachDelete(DeleteView):
    template_name = 'coaches/delete.html'
    model = Coach
    success_url = reverse_lazy('coaches-list')

    def delete(self, request, *args, **kwargs):
        try:
            coach = self.get_object()
            coach.delete()
            messages.success(self.request, _(coach.name + " deleted successfully!"))
        except:
            messages.error(self.request, _("Delete error."))
        storage = messages.get_messages(self.request)
        for message in storage:
            logger.debug(message)
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(CoachDelete, self).get_context_data(**kwargs)
        context['title'] = _('Coach delete item')
        return context
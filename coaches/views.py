# coding=utf-8

from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django import forms

from coaches.models import Coach


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

    def get_context_data(self, **kwargs):
        context = super(CoachAdd, self).get_context_data(**kwargs)
        context['title'] = _('Coach add item')
        return context


class CoachEdit(UpdateView):
    template_name = 'coaches/edit.html'
    model = Coach
    form_class = CoachModelForm
    success_url = reverse_lazy('coaches-list')

    def get_context_data(self, **kwargs):
        context = super(CoachEdit, self).get_context_data(**kwargs)
        context['title'] = _('Coach update item')
        return context


class CoachDelete(DeleteView):
    template_name = 'coaches/delete.html'
    model = Coach
    success_url = reverse_lazy('coaches-list')

    def get_context_data(self, **kwargs):
        context = super(CoachDelete, self).get_context_data(**kwargs)
        context['title'] = _('Coach delete item')
        return context
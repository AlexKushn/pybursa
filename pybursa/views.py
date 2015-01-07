# coding=utf-8

from django.shortcuts import redirect
from django import forms
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, FormView


from students.models import Student
from coaches.models import Coach


import logging
logger = logging.getLogger(__name__)


class HomeView(TemplateView):
    template_name = "index.html"


class ContactForm(forms.Form):
    theme = forms.CharField(max_length=255, label=_("Theme"))
    coach = forms.ModelChoiceField(queryset=Coach.objects.filter(teacher="LE"),
                                   widget=forms.Select,
                                   empty_label=None, label=_("Coach"))
    student = forms.ModelChoiceField(queryset=Student.objects.all(),
                                     widget=forms.Select,
                                     empty_label=None, label=_("Student"))
    body = forms.CharField(widget=forms.Textarea, label=_("Body"))
    email = forms.EmailField(label=_("Email"))


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/form.html'

    def form_valid(self, form):
        theme = form.cleaned_data['theme']
        coach = form.cleaned_data['coach']
        student = form.cleaned_data['student']
        body = form.cleaned_data['body']
        email = form.cleaned_data['email']

        mail = render_to_string('contact/sample_form.html', {'coach': coach,
                                                             'student': student,
                                                             'body': body})

        try:
            send_mail(theme, mail, email, [coach.email], fail_silently=False)
            messages.success(self.request, _('Message sent successfully!'))
        except:
            messages.error(self.request, _("Connection error. Try later."))
        storage = messages.get_messages(self.request)
        for message in storage:
            logger.debug(message)
        return redirect('contact-us')

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = _('Contact send email')
        return context
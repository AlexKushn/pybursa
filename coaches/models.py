# coding=utf-8

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

from students.models import Dossier


class Coach(models.Model):
    TEACHERS = (
        ('LE', 'Lecturer'),
        ('AS', 'assistant'),
    )
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    surname = models.CharField(max_length=255,  verbose_name=_('Surname'))
    date_of_birth = models.DateField(verbose_name=_('Date of birth'))
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(max_length=15,  verbose_name=_('Phone'))
    teacher = models.CharField(max_length=2, choices=TEACHERS,
                               verbose_name=_('Teacher'))
    user = models.ForeignKey(User,  verbose_name=_('User'))
    dossier = models.OneToOneField(Dossier, blank=True, null=True,
                                   verbose_name=_('Dossier'))

    def __unicode__(self):
        return "%s %s" % (self.name, self.surname)
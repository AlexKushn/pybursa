# coding=utf-8

from django.utils.translation import ugettext_lazy as _
from django.db import models
from courses.models import Course


class Student(models.Model):
    PACKAGE_FIELDS = (
        ('S', 'Standard'),
        ('G', 'Gold'),
        ('V', 'Vip'),
    )

    name = models.CharField(max_length=255, verbose_name=_('Name'))
    surname = models.CharField(max_length=255, verbose_name=_('Surname'))
    date_of_birth = models.DateField(verbose_name=_('Date of birth'))
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(max_length=15, verbose_name=_('Phone'))
    course = models.ManyToManyField(Course, verbose_name=_('Course'))
    package = models.CharField(max_length=1, choices=PACKAGE_FIELDS,
                               default='S', verbose_name=_('Package'))
    dossier = models.OneToOneField('students.Dossier', blank=True, null=True,
                                   verbose_name=_('Dossier'))

    def __unicode__(self):
        return "%s %s" % (self.name, self.surname)


class Address(models.Model):
    zip = models.CharField(max_length=30, verbose_name=_('Zip'))
    country = models.CharField(max_length=255, verbose_name=_('Country'))
    province = models.CharField(max_length=255, verbose_name=_('Province'))
    region = models.CharField(max_length=255, verbose_name=_('Region'))
    city = models.CharField(max_length=255, verbose_name=_('City'))
    street = models.CharField(max_length=255, verbose_name=_('Street'))
    house = models.CharField(max_length=30, verbose_name=_('House'))

    def __unicode__(self):
        return "%s %s %s %s %s" % (self.zip, self.street, self.house,
                                   self.city, self.country)


class Dossier(models.Model):
    PACKAGE_COLOURS = (
        ('red', 'Red'),
        ('orange', 'Orange'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('indigo', 'Indigo'),
        ('violet', 'Violet'),
    )

    address = models.ForeignKey(Address, verbose_name=_('Address'))
    unloved_courses = models.ManyToManyField(Course, blank=True, null=True,
                                             verbose_name=_('Unloved courses'))
    favorite_colour = models.CharField(max_length=6, choices=PACKAGE_COLOURS,
                                       default='red',
                                       verbose_name=_('Favorite colour'))

    def __unicode__(self):
        return "%s" % self.address

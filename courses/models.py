# coding=utf-8

from django.utils.translation import ugettext_lazy as _
from django.db import models


class Course(models.Model):
    LANGUAGES = (
        ('PY', 'Python'),
        ('RU', 'Ruby'),
        ('JS', 'JavaScript'),
    )

    name = models.CharField(max_length=255, verbose_name=_('Name'))
    slug = models.SlugField(max_length=255, blank=True, default="",
                            verbose_name=_('Slug'))
    description = models.CharField(max_length=255, verbose_name=_('Description'))
    lecturer = models.ForeignKey('coaches.Coach', verbose_name=_('Lecturer'))
    assistant = models.ForeignKey('coaches.Coach',  blank=True, null=True,
                                  related_name="course_assistant",
                                  verbose_name=_('Assistant'))
    date_of_start = models.DateField(verbose_name=_('Date of start'))
    date_of_end = models.DateField(verbose_name=_('Date of end'))
    technology = models.CharField(max_length=2, choices=LANGUAGES,
                                  verbose_name=_('Technology'))
    venue = models.ForeignKey('students.Address', blank=True, null=True,
                              verbose_name=_('Venue'))

    def __unicode__(self):
        return "%s" %  self.name
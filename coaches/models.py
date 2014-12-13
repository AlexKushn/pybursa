from django.db import models
from django.contrib.auth.models import User

from students.models import Dossier


class Coach(models.Model):
    TEACHERS = (
        ('LE', 'Lecturer'),
        ('AS', 'assistant'),
    )
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    teacher = models.CharField(max_length=2, choices=TEACHERS)
    user = models.ForeignKey(User)
    dossier = models.OneToOneField(Dossier, blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.name, self.surname)
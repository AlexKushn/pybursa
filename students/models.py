from django.db import models
from courses.models import Course


class Student(models.Model):
    PACKAGE_FIELDS = (
        ('S', 'Standard'),
        ('G', 'Gold'),
        ('V', 'Vip'),
    )

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.ManyToManyField(Course)
    package = models.CharField(max_length=1, choices=PACKAGE_FIELDS,
                               default='S')
    dossier = models.OneToOneField('students.Dossier', blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.name, self.surname)


class Address(models.Model):
    zip = models.CharField(max_length=30)
    country = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=30)

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

    address = models.ForeignKey(Address)
    unloved_courses = models.ManyToManyField(Course, blank=True, null=True)
    favorite_colour = models.CharField(max_length=6, choices=PACKAGE_COLOURS,
                                       default='red')

    def __unicode__(self):
        return "%s" % self.address

from django.db import models


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
    package = models.CharField(max_length=1, choices=PACKAGE_FIELDS,
                               default='s')
    course = models.ManyToManyField('courses.Course')
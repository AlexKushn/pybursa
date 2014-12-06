from django.db import models


class Course(models.Model):
    LANGUAGES = (
        ('PY', 'Python'),
        ('RU', 'Ruby'),
        ('JS', 'JavaScript'),
    )

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    technology = models.CharField(max_length=2, choices=LANGUAGES)
    lecturer = models.ForeignKey('coaches.Coach')
    assistant = models.ForeignKey('coaches.Coach',  blank=True,
                                  related_name="course_assistant")
    date_of_start = models.DateField()
    date_of_end = models.DateField()

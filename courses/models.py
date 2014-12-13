from django.db import models


class Course(models.Model):
    LANGUAGES = (
        ('PY', 'Python'),
        ('RU', 'Ruby'),
        ('JS', 'JavaScript'),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default="")
    description = models.CharField(max_length=255)
    lecturer = models.ForeignKey('coaches.Coach')
    assistant = models.ForeignKey('coaches.Coach',  blank=True, null=True,
                                  related_name="course_assistant")
    date_of_start = models.DateField()
    date_of_end = models.DateField()
    technology = models.CharField(max_length=2, choices=LANGUAGES)
    venue = models.ForeignKey('students.Address', blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.name, )
from django.contrib import admin
from django.db import models
from django.forms.extras.widgets import SelectDateWidget

from courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'technology', 'date_of_start', 'date_of_end']
    list_filter = ['technology', 'date_of_start']
    search_fields = ['name', 'technology', 'start_date', 'end_date']
    radio_fields = {'technology': admin.VERTICAL}
    list_display_links = ['name', 'technology']
    prepopulated_fields = {'slug': ('name',)}
    formfield_overrides = {
        models.DateField: {'widget': SelectDateWidget},
    }
    fieldsets = (
        ('Course Item Details', {
            'fields': ('name', 'description', 'lecturer', 'technology',
                       'date_of_start', 'date_of_end')
        }),
        ('Advanced options', {
            'fields': [('assistant', 'venue', 'slug')],
            'classes': ['collapse']

        }),
    )
    save_as = True
    save_on_top = True

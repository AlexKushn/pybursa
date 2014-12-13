from django.contrib import admin
from django.db import models
from django.forms import widgets

from coaches.models import Coach
from courses.models import Course


class AssistantInline(admin.StackedInline):
    model = Course
    fk_name = 'assistant'
    fields = 'name', 'technology'
    extra = 0


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'date_of_birth', 'email', 'phone']
    list_filter = ['name', 'surname']
    search_fields = ['name', 'surname']
    radio_fields = {'teacher': admin.HORIZONTAL}
    list_display_links = ['name', 'surname']
    formfield_overrides = {
        models.DateField: {'widget': widgets.DateInput},
    }
    fieldsets = (
        ('Course Item Details', {
            'fields': ('name', 'surname', 'date_of_birth', 'email', 'phone',
                       'teacher', 'user')
        }),
        ('Advanced options', {
            'fields': ['dossier'],
            'classes': ['collapse']

        }),
    )
    save_as = True
    save_on_top = True
    inlines = [AssistantInline]

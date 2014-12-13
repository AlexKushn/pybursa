# coding=utf-8

from django.contrib import admin
from django.db import models
from django.forms import widgets

from students.models import Student, Address, Dossier


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'date_of_birth', 'package']
    list_filter = ['package', ]
    search_fields = ('name', 'surname')
    radio_fields = {'package': admin.HORIZONTAL}
    filter_horizontal = ['course']
    formfield_overrides = {
        models.DateField: {'widget': widgets.DateInput},
    }
    fieldsets = (
        ('Student Item Details', {
            'fields': ('name', 'surname', 'date_of_birth', 'email', 'phone',
                       'course', 'package')
        }),
        ('Advanced options', {
            'fields': ['dossier'],
            'classes': ['collapse']

        }),
    )
    save_as = True
    save_on_top = True


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['zip', 'country', 'province', 'city',
                    'region', 'street', 'house']
    list_display_links = ['country', 'province', 'city']
    list_filter = ['country', 'city']
    search_fields = ['zip', 'country', 'city', 'street']

@admin.register(Dossier)
class DossierAdmin(admin.ModelAdmin):
    list_display = ['address', 'favorite_colour']
    list_display_links = list_display
    filter_horizontal = ['unloved_courses']
    list_filter = ['address__country', 'address__city', 'address__street',
                   'unloved_courses__technology', 'favorite_colour']
    search_fields = ['address__country', 'address__city', 'address__street',
                     'unloved_courses__technology','favorite_colour']
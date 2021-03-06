from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import (Page, Workshop, Presentation, Image, QuestionPaper, Files, PracticeSession,
                     Circular, Poster, Video, WorkshopRegistration, Event, EventRegistration, Charts,Notification,Image_Slider,Medicinal_Trees)


class WorkshopRegistrationAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'email', 'phone', 'workshop')
    search_fields = ('name', 'email')
    list_filter = ('workshop',)


class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')


class EventRegistrationAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'email', 'phone', 'event')
    search_fields = ('name', 'email')
    list_filter = ('event',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')


# Register your models here.
admin.site.register(Page)
# admin.site.register(Workshop, WorkshopAdmin)
# admin.site.register(Presentation)
admin.site.register(Image)
# admin.site.register(QuestionPaper)
admin.site.register(Files)
# admin.site.register(PracticeSession)
# admin.site.register(Circular)
# admin.site.register(Poster)
admin.site.register(Video)
admin.site.register(Charts)
# admin.site.register(WorkshopRegistration, WorkshopRegistrationAdmin)
admin.site.register(Event, EventAdmin)
# admin.site.register(EventRegistration, EventRegistrationAdmin)
admin.site.register(Notification)
admin.site.register(Image_Slider)
admin.site.register(Medicinal_Trees)
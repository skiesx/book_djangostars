from django.contrib.admin.models import LogEntry
from django.contrib import admin
from apps.book_app.models import *

admin.site.register(WebRequest)
admin.site.register(Book)


class LogEntryBookAdmin(admin.ModelAdmin):
    list_display = readonly_fields = [
        'pk', 'action_time', 'object_id', 'object_title', 'action_flag'
    ]

admin.site.register(LogBook, admin_class=LogEntryBookAdmin)

class LogEntryAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'object_repr', 'action_time', 'user', 'content_type', 'object_id', 'action_flag', 'change_message'
    ]
    readonly_fields = [
        'user', 'action_time', 'content_type', 'object_id', 'object_repr', 'change_message', 'action_flag'
    ]

admin.site.register(LogEntry, admin_class=LogEntryAdmin)

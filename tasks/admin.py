from django.contrib import admin

from tasks.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "content", )
    list_filter = ("created_at", "deadline", "is_completed", )
    search_fields = ("name", )


admin.site.register(Tag)

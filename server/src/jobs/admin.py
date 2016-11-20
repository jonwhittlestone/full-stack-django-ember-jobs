from django.contrib import admin
from .models import Job


class JobModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "daily_rate", "timestamp"]
    list_display_links = ["title"]
    list_filter = ["updated", "timestamp"]

    search_fields = ["title", "description", "daily_rate"]

    class Meta:
        model = Job


admin.site.register(Job, JobModelAdmin)

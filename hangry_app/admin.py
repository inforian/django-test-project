from django.contrib import admin

from hangry_app.models import HangryPerson


@admin.register(HangryPerson)
class HangryPersonAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "first_name",
        "last_name",
        "email",
    )
    list_display_links = (
        "pk",
        "first_name",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
    )
    date_hierarchy = "created_at"
    show_full_result_count = False


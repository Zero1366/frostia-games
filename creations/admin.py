from django.contrib import admin

from .models import Creation


@admin.register(Creation)
class CreationAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        "title",
        "alphabet_letter",
        "project_type",
        "status",
        "is_visible",
        "updated_at",
    )

    list_filter = (
        "alphabet_letter",
        "project_type",
        "status",
        "is_visible",
    )

    search_fields = (
        "title",
        "slug",
        "code_name",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

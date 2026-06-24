from django.contrib import admin

from .models import PlayableProject


@admin.register(PlayableProject)
class PlayableProjectAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        "title",
        "status",
        "content_type",
        "is_available",
        "is_visible",
        "updated_at",
    )

    list_filter = (
        "status",
        "content_type",
        "is_available",
        "is_visible",
    )

    search_fields = (
        "title",
        "slug",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

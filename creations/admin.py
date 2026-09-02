from django.contrib import admin

from .models import Category, Creation, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ("name",)


@admin.register(Creation)
class CreationAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        "title",
        "alphabet_letter",
        "category",
        "project_type",
        "status",
        "is_visible",
        "updated_at",
    )

    list_filter = (
        "alphabet_letter",
        "category",
        "project_type",
        "status",
        "is_visible",
    )

    filter_horizontal = ("tags",)

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

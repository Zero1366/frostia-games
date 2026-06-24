from django.db import models


class Creation(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name="Titre",
    )

    slug = models.SlugField(
        max_length=140,
        unique=True,
        verbose_name="Identifiant URL",
    )

    alphabet_letter = models.CharField(
        max_length=1,
        verbose_name="Lettre alphabétique",
    )

    code_name = models.CharField(
        max_length=120,
        blank=True,
        verbose_name="Nom de code",
    )

    project_type = models.CharField(
        max_length=100,
        verbose_name="Type de projet",
    )

    status = models.CharField(
        max_length=100,
        verbose_name="Statut",
    )

    short_description = models.TextField(
        verbose_name="Description courte",
    )

    is_visible = models.BooleanField(
        default=True,
        verbose_name="Visible sur le site",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Dernière modification",
    )

    class Meta:
        verbose_name = "Création"
        verbose_name_plural = "Créations"
        ordering = ["alphabet_letter", "title"]

    def __str__(self) -> str:
        return self.title

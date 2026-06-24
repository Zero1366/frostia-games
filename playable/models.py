from django.db import models


class PlayableProject(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name="Titre",
    )

    slug = models.SlugField(
        max_length=140,
        unique=True,
        verbose_name="Identifiant URL",
    )

    status = models.CharField(
        max_length=100,
        verbose_name="Statut",
    )

    content_type = models.CharField(
        max_length=100,
        verbose_name="Type de contenu prévu",
    )

    short_description = models.TextField(
        verbose_name="Description courte",
    )

    availability_message = models.TextField(
        verbose_name="Message de disponibilité",
    )

    is_available = models.BooleanField(
        default=False,
        verbose_name="Disponible",
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
        verbose_name = "Projet jouable"
        verbose_name_plural = "Projets jouables"
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title

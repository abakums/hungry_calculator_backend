import uuid
from django.db import models


class Group(models.Model):
    title = models.CharField("Название", max_length=200)
    organizer = models.ForeignKey(
        "users.Participant",
        on_delete=models.CASCADE,
        verbose_name="Организатор",
        related_name="organizer_groups"
    )
    group_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    requisites = models.CharField("Реквизиты", max_length=100)

    class Meta:
        verbose_name = "группу"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.title


class Participant(models.Model):
    name = models.CharField("Имя", max_length=200)
    groups = models.ManyToManyField(
        "users.Group",
        blank=True,
        related_name="participants",
        verbose_name="Группы",
        through="ParticipantGroup",
        through_fields=("participant", "group", "is_organizer")
    )

    class Meta:
        verbose_name = "участника"
        verbose_name_plural = "Участники"

    def __str__(self):
        return self.name


class ParticipantGroup(models.Model):
    participant = models.ForeignKey(
        "users.Participant",
        on_delete=models.CASCADE,
        verbose_name="Участник",
        related_name="participant_groups"
    )
    group = models.ForeignKey(
        "users.Group",
        on_delete=models.CASCADE,
        verbose_name="Группа",
        related_name="participant_groups"
    )
    is_organizer = models.BooleanField("Является организатором", default=False)

    class Meta:
        verbose_name = "участника группы"
        verbose_name_plural = "Участники групп"

    def __str__(self):
        return f"{self.participant} - {self.group}"

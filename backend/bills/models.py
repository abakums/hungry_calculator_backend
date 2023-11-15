from django.db import models


class ParticipantBillPosition(models.Model):
    bill_position = models.ForeignKey(
        "bills.BillPosition",
        on_delete=models.CASCADE,
        verbose_name="Позиция в чеке",
        related_name="participant_bill_positions"
    )
    participant = models.ForeignKey(
        "users.Participant",
        on_delete=models.CASCADE,
        verbose_name="Участник",
        related_name="participant_bill_positions"
    )
    participant_price = models.IntegerField("Стоимость")

    class Meta:
        verbose_name = "позицию участника"
        verbose_name_plural = "Позиции участников"

    def __str__(self):
        return f"{self.bill_position} - {self.participant}"


class BillPosition(models.Model):
    title = models.CharField("Название", max_length=200)
    price = models.IntegerField("Цена")
    group = models.ForeignKey(
        "users.Group",
        on_delete=models.CASCADE,
        verbose_name="Группа",
        related_name="bill_positions"
    )
    participants = models.ManyToManyField(
        "users.Participant",
        blank=True,
        related_name="bill_positions",
        verbose_name="Участники",
        through="ParticipantBillPosition",
        through_fields=("bill_position", "participant", "participant_price")
    )

    class Meta:
        verbose_name = "позицию в чеке"
        verbose_name_plural = "Поизии в чеке"

    def __str__(self):
        return f"{self.title} ({self.group})"

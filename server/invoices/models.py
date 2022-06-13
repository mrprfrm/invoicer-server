from django.db import models
from django.utils import timezone


class Contract(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    client = models.ForeignKey("participants.Client", on_delete=models.PROTECT)
    contractor = models.ForeignKey("participants.Contractor", on_delete=models.PROTECT)

    class Meta:
        unique_together = ["name", "date", "client"]

    def __str__(self):
        return f"{self.client} {self.name} {self.date}"


class Invoice(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    contract = models.ForeignKey("invoices.Contract", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Service(models.Model):
    description = models.TextField()
    quantity = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    amount = models.IntegerField()

    invoice = models.ForeignKey(
        "invoices.Invoice", related_name="services", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.description

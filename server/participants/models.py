from django.db import models


class Contractor(models.Model):
    name = models.CharField(max_length=255)
    inn = models.CharField(max_length=12)
    registration_address = models.TextField()
    beneficiary_bank = models.CharField(max_length=255)
    bank_address = models.TextField()
    swift = models.CharField(max_length=11)
    account = models.CharField(max_length=20)

    class Meta:
        unique_together = ["name", "inn"]

    def __str__(self):
        return f"{self.name} {self.inn}"


class Client(models.Model):
    name = models.CharField(max_length=255, unique=True)
    alias = models.CharField(max_length=255, null=True)
    registration_address = models.TextField()
    bank_details = models.TextField()
    swift = models.CharField(max_length=11)
    account = models.CharField(max_length=12)

    def __str__(self):
        return self.alias or self.name

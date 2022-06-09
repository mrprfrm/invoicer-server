from django.contrib import admin

from .models import Client, Contractor


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    pass

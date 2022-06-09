from django.contrib import admin

from .models import Contract, Invoice, Service


class ServiceInline(admin.TabularInline):
    model = Service


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass

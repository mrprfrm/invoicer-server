from django.urls import path

from .views import invoice_view

app_name = "invoices"

urlpatterns = [
    path("<int:id>", invoice_view, name="invoice")
]

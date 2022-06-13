from django.db.models import F, Sum
from django.shortcuts import get_object_or_404, render

from .models import Invoice


def invoice_view(request, id):
    invoices = Invoice.objects.select_related("contract").prefetch_related("services")
    total_query = Invoice.objects.aggregate(
        total=Sum(F("services__price") * F("services__amount"))
    )
    invoice = get_object_or_404(invoices, id=id)
    return render(
        request,
        "invoices/invoice.html",
        {"invoice": invoice, "total": "%.2f" % total_query["total"]},
    )

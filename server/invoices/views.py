from tempfile import TemporaryFile

from django.db.models import F, Sum
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from weasyprint import HTML

from .models import Invoice


def invoice_view(request, id):
    invoices = Invoice.objects.select_related("contract").prefetch_related("services")
    total_query = Invoice.objects.aggregate(
        total=Sum(F("services__price") * F("services__amount"))
    )
    invoice = get_object_or_404(invoices, id=id)
    template_name = "invoices/invoice.html"
    context = {"invoice": invoice, "total": "%.2f" % total_query["total"]}

    with TemporaryFile() as temp:
        html = HTML(string=render_to_string(template_name, context))
        html.write_pdf(temp)
        temp.seek(0)
        response = HttpResponse(temp.read(), content_type="application/pdf")
        response[
            "Content-Disposition"
        ] = f'attachment; filename="{invoice.name}_{invoice.date}.pdf"'
        return response

    return render(request, template_name, context)

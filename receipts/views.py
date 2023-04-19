from django.shortcuts import render
from receipts.models import Receipt, ExpenseCategory, Account

# Create your views here.


def receipt_lists(request):
    receipt_list = Receipt.objects.all()
    context = {
        "receipt_lists": receipt_list,
    }
    return render(request, "receipts/list.html", context)

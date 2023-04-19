from django.shortcuts import render
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def receipt_lists(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_lists": receipt_list,
    }
    return render(request, "receipts/list.html", context)

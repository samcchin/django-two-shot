from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from receipts.forms import ReceiptForm, ExpenseCategoryForm, AccountForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def receipt_lists(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_lists": receipt_list,
    }
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()
        form.fields['category'].queryset = ExpenseCategory.objects.filter(owner=request.user)
        form.fields['account'].queryset = Account.objects.filter(owner=request.user)
    context = {
        "form": form,
    }
    return render(request, "receipts/create.html", context)


@login_required
def category_list(request):
    expense_category = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "expense_categories": expense_category,
    }
    return render(request, "receipts/category_list.html", context)


@login_required
def account_list(request):
    accounts_list = Account.objects.filter(owner=request.user)
    context = {
        "accounts": accounts_list,
    }
    return render(request, "receipts/account_list.html", context)


@login_required
def create_category(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect("category_list")
    else:
        form = ExpenseCategoryForm()
    context = {
        "form": form,
    }
    return render(request, "categories/create.html", context)


@login_required
def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(False)
            account.owner = request.user
            account.save()
            return redirect("account_list")
    else:
        form = AccountForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/create.html", context)

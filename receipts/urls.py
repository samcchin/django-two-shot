from django.urls import path
from receipts.views import receipt_lists, create_receipt, category_list, account_list, create_category


urlpatterns = [
    path("", receipt_lists, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", category_list, name="category_list"),
    path("accounts/", account_list, name="account_list"),
    path("categories/create/", create_category, name="create_category"),
]

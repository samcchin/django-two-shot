from django.urls import path
from receipts.views import receipt_lists, create_receipt


urlpatterns = [
    path("", receipt_lists, name="home"),
    path("create/", create_receipt, name="create_receipt")
]

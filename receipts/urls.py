from django.urls import path
from receipts.views import receipt_lists


urlpatterns = [
    path("", receipt_lists, name="home")
]

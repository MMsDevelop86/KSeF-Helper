from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_view, name='invoice_view'),
    ]
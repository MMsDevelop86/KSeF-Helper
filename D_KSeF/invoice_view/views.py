from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def invoice_view(request):
    return render(request, 'inv_view.html')
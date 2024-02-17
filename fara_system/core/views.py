from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    product_data = ProductModel.objects.all()
    company_data = CompanyModel.objects.all()
    context = {'product_data': product_data, 'company_data':company_data}
    return render(request, "core/home.html", context)
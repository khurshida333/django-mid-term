from django.shortcuts import render,redirect
from .import forms

# Create your views here.

def add_brands(request):
    if request.method == 'POST':
        brand_form = forms.BrandForm(request.POST)
        if brand_form.is_valid():
            brand_form.save()
            return redirect(add_brands)
    else:
        brand_form = forms.BrandForm()
        return render(request, 'add_brands.html',{'form': brand_form})
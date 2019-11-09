from django.shortcuts import render, redirect
from .models import *

def category_a(request):
    cat_a_obj = CategoryA.objects.all()
    return render(request,'dashboard/livestock/livestock_cat_a.html',{'data': cat_a_obj})

def category_b(request):
    if request.method == 'POST':
        cat_b_obj = CategoryB.objects.filter(category__name = request.POST.get('category_a'))

        cat_a_images = CategoryAImage.objects.filter(category__name = request.POST.get('category_a'))
        return render(request,'dashboard/livestock/livestock_cat_b.html',{'data': cat_b_obj, 'images': cat_a_images})
    else:
        return redirect('/livestock')

def category_result(request):
    if request.method == 'POST':
        cat_b = CategoryB.objects.get(name = request.POST.get('category_b'))
        cat_b_images = CategoryBImage.objects.filter(category = cat_b)
        disease = LiveStockDisease.objects.get(name = cat_b.disease_name)
        return render(request,'dashboard/livestock/livestock_result.html',{'data': cat_b, 'disease': disease, 'images': cat_b_images})
    else:
        return redirect('/livestock')

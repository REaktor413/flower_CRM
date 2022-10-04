from django.shortcuts import render
from categories.models import Category


def home(request, pk=None):
    qs = Category.objects.all()
    context = {'objects_list': qs, }
    return render(request, "categories/home.html", context)

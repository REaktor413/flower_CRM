from django.urls import path

from categories.views import *

urlpatterns = [
    path('', home, name="categories"),
]

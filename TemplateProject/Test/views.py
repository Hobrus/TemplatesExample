from django.shortcuts import render
from django.views.generic import ListView

from .models import TestModel


# Create your views here.

def main(request):
    return render(request, 'main.html')


def second_page(request):
    return render(request, 'second_page.html')


class MyTestModelView(ListView):
    model = TestModel
    template_name = 'test_model.html'

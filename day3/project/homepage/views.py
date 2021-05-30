from django.shortcuts import render, HttpResponse

from .forms import CoffeeForm
from .models import Coffee
# Create your views here.


def index(request):
    nums = [1, 2, 3, 4, 5]
    name = 'Lukas'
    context = {
        "name": name,
        "nums": nums
    }
    return render(request, 'index.html', context=context)


def coffee_view(request):
    if request.method == 'POST':
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()

    coffee_list = Coffee.objects.all()
    form = CoffeeForm()
    context = {
        "item_list": coffee_list,
        "item_form": form
    }
    return render(request, 'coffee.html', context=context)
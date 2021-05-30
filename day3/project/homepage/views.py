from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    nums = [1, 2, 3, 4, 5]
    name = 'Lukas'
    context = {
        "name": name,
        "nums": nums
    }
    return render(request, 'index.html', context=context)

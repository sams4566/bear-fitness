from django.shortcuts import render


def current_basket(request):
    return render(request, 'basket.html')


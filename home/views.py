from django.shortcuts import render

def index(request):
    """
    Displays the home screen
    """
    return render(request, 'home/index.html')

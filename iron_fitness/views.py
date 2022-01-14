from django.shortcuts import render


def my_custom_page_not_found_view(request, exception):
    """
    Display 404 error page
    """
    return render(request, 'iron_fitness/404.html', {})

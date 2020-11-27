from django.shortcuts import render


def landing(request):
    """Render the landing page of the site."""
    return render(request, "index.html")

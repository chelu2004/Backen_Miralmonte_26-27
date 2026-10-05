from django.shortcuts import render


def homepage(request):
    """Render the homepage."""
    return render(request, "home.html")
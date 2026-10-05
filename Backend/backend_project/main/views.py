from django.shortcuts import render


def main(request):
    """Render the main application page."""
    return render(request, "main/main.html")
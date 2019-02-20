from django.shortcuts import render

# Create your views here.
def HomeView(request):
    """View function for home page of site."""
    return render(request, 'index.html')

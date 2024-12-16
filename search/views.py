from django.shortcuts import render
from .models import DjangleDb


def perform_search(query):
    return DjangleDb.objects.filter(
        title__icontains=query
    ) | DjangleDb.objects.filter(
        content__icontains=query
    )
def search_page(request):
    query = request.GET.get('q')
    results = []

    if query:
        # Perform your search logic here
        results = perform_search(query)  # Replace with your actual search function

    return render(request, 'search/base.html', {'results': results})

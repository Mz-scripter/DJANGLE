from django.shortcuts import render
from .models import SearchResult
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


def perform_search(query):
    search_query = SearchQuery(query)
    vector = (
        SearchVector('title', weight='A') +
        SearchVector('content', weight='B') +
        SearchVector('keywords', weight='C')
    )
    results = SearchResult.objects.annotate(
        rank=SearchRank(vector, search_query)
    ).filter(search_vector=search_query).order_by('-rank')

    return results

def search_page(request):
    query = request.GET.get('q')
    results = []

    if query:
        # Perform your search logic here
        results = perform_search(query)  # Replace with your actual search function

    return render(request, 'search/base.html', {'results': results, 'query': query})

from django.shortcuts import render
from .models import SearchResult
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

def perform_search(query, result_type=None):
    search_query = SearchQuery(query)
    vector = (
        SearchVector('title', weight='A') +
        SearchVector('content', weight='B') +
        SearchVector('keywords', weight='C')
    )
    results = SearchResult.objects.annotate(
        rank=SearchRank(vector, search_query)
    ).filter(search_vector=search_query).order_by('-rank')

    if result_type:
        results = results.filter(type=result_type)

    return results

def search_page(request):
    query = request.GET.get('q')
    result_type = request.GET.get('type')
    results = []

    if query:
        # Perform your search logic here
        results = perform_search(query, result_type)  # Replace with your actual search function

    # Pagination Setup
    paginator = Paginator(results, 10)
    page = request.GET.get('page', 1)
    try:
        paginated_results = paginator.page(page)
    except PageNotAnInteger:
        paginated_results = paginator.page(1)
    except EmptyPage:
        paginated_results = paginator.page(paginator.num_pages)

    return render(request, 'search/base.html', {'results': paginated_results, 'query': query, 'paginator': paginator})

from django.shortcuts import render
from .models import SearchResult
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
import time
from django.http import JsonResponse
from django.db.models import Q
from datetime import datetime

def autocomplete(request):
    query = request.GET.get('q', '').strip()
    suggestions = []

    if query:
        suggestions = SearchResult.objects.filter(
            Q(title__icontains=query)
        ).values_list('title', flat=True)[:8]
    
    return JsonResponse({'suggestions': list(suggestions)})

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
    total_results = 0
    search_time = 0

    if query:
        # Perform your search logic here
        start_time = time.time()
        results = perform_search(query, result_type)  # Replace with your actual search function
        total_results = results.count()
        search_time = time.time() - start_time

    # Pagination Setup
    paginator = Paginator(results, 10)
    page = request.GET.get('page', 1)
    try:
        paginated_results = paginator.page(page)
    except PageNotAnInteger:
        paginated_results = paginator.page(1)
    except EmptyPage:
        paginated_results = paginator.page(paginator.num_pages)
    
    context = {
        'results': paginated_results,
        'query': query,
        'paginator': paginator,
        'total_results': total_results,
        'search_time': search_time,
        'current_year': datetime.now().year,
    }

    return render(request, 'search/base.html', context)

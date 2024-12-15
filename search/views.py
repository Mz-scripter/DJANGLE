from django.shortcuts import render

def search_page(request):
    return render(request, 'search/base.html')

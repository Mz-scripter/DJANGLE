from django.contrib import admin
from .models import DjangleDb, SearchResult

admin.site.register(DjangleDb)
# admin.site.register(SearchResult)

@admin.register(SearchResult)
class SearchResultAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'url')
    search_fields = ('title', 'keywords', 'type')
from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year', 'duration_min', 'rating')
    list_filter = ('genre', 'release_year')
    search_fields = ('title', 'genre')
    list_editable = ('rating',)
    ordering = ('title',)

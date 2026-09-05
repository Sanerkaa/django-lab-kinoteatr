from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import MovieForm
from .models import Movie


def home(request):
    """Первое представление из п. 5.2 методички."""
    return HttpResponse(
        '<h1>Hello, Django!</h1>'
        '<p><a href="/movies/">Перейти к афише кинотеатра</a></p>'
    )


class MovieListView(ListView):
    model = Movie
    template_name = 'core/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '').strip()
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'core/movie_detail.html'
    context_object_name = 'movie'


class MovieCreateView(CreateView):
    """Дополнительное задание (п. 7.4): создание объекта через форму на сайте."""

    model = Movie
    form_class = MovieForm
    template_name = 'core/movie_form.html'
    success_url = reverse_lazy('movie_list')

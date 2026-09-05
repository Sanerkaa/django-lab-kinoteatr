from django import forms

from .models import Movie


class MovieForm(forms.ModelForm):
    """Форма добавления фильма с сайта (п. 7.4 — дополнительное задание)."""

    class Meta:
        model = Movie
        fields = ['title', 'genre', 'duration_min', 'rating', 'release_year']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Интерстеллар'}),
            'genre': forms.TextInput(attrs={'placeholder': 'Фантастика'}),
            'duration_min': forms.NumberInput(attrs={'min': 1, 'max': 600}),
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 10, 'step': '0.1'}),
            'release_year': forms.NumberInput(attrs={'min': 1895, 'max': 2100}),
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if not 0 <= rating <= 10:
            raise forms.ValidationError('Рейтинг задаётся по десятибалльной шкале: от 0 до 10.')
        return rating

    def clean_release_year(self):
        year = self.cleaned_data['release_year']
        if year < 1895:
            raise forms.ValidationError('Первый киносеанс состоялся в 1895 году.')
        return year

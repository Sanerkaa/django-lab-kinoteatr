from django.db import models
from django.urls import reverse


class Movie(models.Model):
    """Вариант 6 — «Кинотеатр». Карточка фильма в афише."""

    title = models.CharField('Название', max_length=200)
    genre = models.CharField('Жанр', max_length=100, blank=True)
    duration_min = models.PositiveIntegerField('Длительность, мин')
    rating = models.DecimalField('Рейтинг', max_digits=3, decimal_places=1, default=0)
    release_year = models.PositiveIntegerField('Год выхода')

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', args=[self.pk])

    @property
    def duration_pretty(self):
        """Длительность в формате «2 ч 28 мин» — для шаблонов."""
        hours, minutes = divmod(self.duration_min, 60)
        if hours:
            return f'{hours} ч {minutes} мин'
        return f'{minutes} мин'

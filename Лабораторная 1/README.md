# Лабораторная работа № 1 — «Знакомство с Django»

**Вариант 6 — «Кинотеатр»** (модель `Movie`: `title`, `genre`, `duration_min`, `rating`, `release_year`)
НГУЭУ «НИНХ», дисциплина «Интернет-программирование».

## Что реализовано

| Этап | Что сделано | Где смотреть |
|---|---|---|
| Пара 1 | Проект `mysite`, приложение `core`, view `home` → «Hello, Django!», маршрутизация через `include()` | `core/views.py`, `core/urls.py`, `mysite/urls.py` |
| Пара 1 | `ALLOWED_HOSTS` и `CSRF_TRUSTED_ORIGINS` для домена Replit | `mysite/settings.py` |
| Пара 2 | Модель `Movie`, миграция, админ-панель, 8 записей в фикстуре | `core/models.py`, `core/admin.py`, `core/fixtures/movies.json` |
| Пара 3 | `base.html` + наследование шаблонов, `ListView`, `DetailView`, статический CSS | `core/templates/core/`, `static/css/style.css` |
| Доп. задание | `ModelForm` + `CreateView` — добавление фильма с сайта | `core/forms.py`, `core/templates/core/movie_form.html` |

## Маршруты

| URL | View | Назначение |
|---|---|---|
| `/` | `home` | Страница «Hello, Django!» из п. 5.2 |
| `/movies/` | `MovieListView` | Афиша + поиск по названию |
| `/movies/<pk>/` | `MovieDetailView` | Карточка фильма |
| `/movies/add/` | `MovieCreateView` | Форма добавления фильма (доп. задание) |
| `/admin/` | `admin.site.urls` | Административная панель |

## Запуск в Replit

1. Импортировать репозиторий в Replit (**Import → GitHub**) или создать Repl по шаблону **Python** и загрузить файлы.
2. В Shell выполнить:

```bash
cd "Лабораторная 1"
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata movies
DJANGO_SUPERUSER_USERNAME=admin \
DJANGO_SUPERUSER_PASSWORD=admin12345 \
DJANGO_SUPERUSER_EMAIL=admin@example.com \
python manage.py createsuperuser --noinput
```

3. Нажать **Run** (команда запуска берётся из корневого `.replit`) и открыть вкладку **Preview**.

Главная страница — «Hello, Django!», афиша — `/movies/`, админка — `/admin/` (логин `admin`, пароль `admin12345`).

## Запуск локально

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate && python manage.py loaddata movies
python manage.py runserver
```

## Учебные упрощения

* `ALLOWED_HOSTS = ["*"]` — только для лабораторной работы; в реальном проекте список хостов задаётся явно.
* `DEBUG = True` и `SECRET_KEY` в открытом виде — так генерирует `django-admin startproject`; для продакшена выносятся в переменные окружения.
* `db.sqlite3` не хранится в репозитории (см. `.gitignore`) — база восстанавливается командами `migrate` + `loaddata movies`.

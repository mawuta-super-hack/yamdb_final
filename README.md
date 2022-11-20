### Проект API Yamdb - api для сайта с отзывами на кино, книги и музыку.

***Здесь вы можете создавать оставлять отзывы и рейтинг на произведения, а также комментировать отзывы.***

Этот репозиторий содержит урезанную версию проекта: в составе готовое API для взаимодействия с проектом.
<br>

![workflow](https://github.com/mawuta-super-hack/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?)

### Возможности API:
- Регистрация и токена авторизации (Simple JWT).
- Получение, создание, обновление, удаление учетных записей.
- Получение, создание, обновление, удаление произведений.
- Получение, создание, удаление категорий произведений и их жанров.
- Получение, создание, обновление, удаление отзывов и комментариев.

Подробней [по ссылке](http://127.0.0.1:8000/api/v1/redoc/)<br>
<sub>Ссылка откроется после развертывания проекта.</sub>
<br>
### Описание команд для запуска приложения в контейнерах:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/mawuta-super-hack/infra_sp2.git
```

```
cd ./api_yamdb/infra
```

Запуск docker-compose:
```
docker-compose up -d --build
```

Выполение миграций:
```
docker-compose exec web python manage.py migrate
```

Создание суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```

Cбор статики:
```
docker-compose exec web python manage.py collectstatic --no-input 
```

Создание резервной копии БД:
```
docker-compose exec web python manage.py dumpdata > fixtures.json
```

### Пример наполения .env-файла:

DB_ENGINE=django.db.backends.postgresql <br>
DB_NAME=(им базы данных)<br>
POSTGRES_USER=(логин для подключения к БД)<br>
POSTGRES_PASSWORD=(пароль для подключения к БД)<br>
DB_HOST=(название сервиса/контейнера)<br>
DB_PORT=(порт для подключения к БД)<br>
SECRET_KEY=(автоматически сгенерированное значение переменной при создании проекта django)<br>

### Импорт данных из csv для наполнения базы:

После развертывания проекта перейдите:

```
cd api_yamdb
```

Запустите команду импорта:

```
python manage.py load_csv_data
```

В терминале отобразится результат импорта.<br>
Если какой-либо из файлов отсутствует, то он не будет импортирован.

Примеры файлов csv для наполнения базы находятся в папке /static/data/*.csv:
- users.csv - файл для заполнения таблицы пользователей
- titles.csv - файл для заполнения таблицы произведений.
- category.csv - файл для заполнения таблицы категорий произведений.
- genre.csv - файл для заполнения таблицы жанров произведений.
- genre_title.csv - файл для заполнения таблицы Many-to-Many: одно произведение может иметь несколько жанров.
- review.csv - файл для заполнения таблицы отзывов к произведениям.
- comments.csv - файл для заполнения таблицы комментариев к отзывам.
<br>

### Примеры запросов к API:

- Получение списка всех категорий: <br>
GET http://localhost/api/v1/categories/

```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```

- Создание категории (только для администратора): <br>
POST http://localhost/api/v1/categories/
```
{
  "name": "string",
  "slug": "string"
}
```
- Удаление категории (только для администратора): <br>
DELETE http://localhost/api/v1/categories/{slug}/


Полный список запросов и эндпоинтов описан в документации ReDoc. Документация доступна после запуска проекта по адресу:

```
http://84.201.163.132/redoc/
```

Авторы проекта:
<br>
Auth/Users: Петухов Артем [Github](https://github.com/mityasun)<br>
Titles/Category/Genre: Клименкова Мария [Github](https://github.com/mawuta-super-hack)<br>
Reviews/Comments: Хужина Лилия [Github](https://github.com/iamliliya)<br>

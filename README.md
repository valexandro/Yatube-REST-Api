# YaTube REST API (Учебный проект)
## Описание проекта
Проект создан в рамках курса "Python-разработчик".

Yatube - платформа для блогов, с возможностью регистрации пользователей, группами, подписками и комментариями, использующая возможности Django ORM и DRF.

### Использованные технологии
- Python 3.7
- Django 2.2.16 + DRF 3.12.4 - **REST API**
- Djoser 2.05 - **аутентификация по JWT**

## Установка (Linux)
1. Склонировать репозиторий:
```
git clone git@github.com:valexandro/api_final_yatube.git
```
2. Создать и активировать виртуальное окружение в папке проекта:
```
python3.7 -m venv venv
source venv/bin/activate
```
3. Обновить pip и установить зависимости:
```
pip install --upgrade pip
pip install -r requirements.txt
```
4. Выполнить миграции:
```
python manage.py makemigrations
python manage.py migrate
```
5. Запустить локальный веб сервер для разработки:
```
cd yatube_api/
python manage.py runserver
```
## Примеры запросов к апи
Получение списка всех постов. Аутентификация не требуется

При указании URL параметров limit и offset выдача работает с пагинацией.
```
GET http://127.0.0.1:8000/api/v1/posts/
```
Пример ответа
```
[
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2019-08-24T14:15:22Z",
        "image": "string",
        "group": 0
    },
]
```
Создание поста. Требуется аутентификация по JWT-токену.

При успешном создании будет возвращен экземпляр созданного поста.
```
POST http://127.0.0.1:8000/api/v1/posts/
```
Тело запроса
```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
Пример ответа
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
Полная документация по апи по умолчанию доступна по адресу http://127.0.0.1:8000/redoc/ после запуска сервера разработки.

## Автор
Вячеслав Александров
- [LinkedIn](https://www.linkedin.com/in/valexandro/)
- [Github](https://github.com/valexandro/)

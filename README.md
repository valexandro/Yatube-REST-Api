# YaTube REST API (Яндекс.Практикум)
## Описание проекта
Проект создан в рамках курса "Python-разработчик".

Yatube - платформа для блогов, с возможностью регистрации пользователей, группами, подписками и комментариями, использующая возможности Django ORM и DRF. В данном проекте реализовано REST API, аутентификация по JWT (Djoser).
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
Полная документация по апи по умолчанию доступна по адресу http://127.0.0.1:8000/redoc/ после запуска сервера разработки.
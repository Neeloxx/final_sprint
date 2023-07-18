# REST API for FSTR pereval.online website

## Описание:

Приложение для любителей походов и покорителей вершин. Позволяет делиться своими подъемами, описанием местности, добавление фотографий и координат объектов.

### Этап 1

* Создание базы данных.
* Создание класса по работе с данными, с помощью которого можно добавить в БД новый перевал и всю информацию о нем.
* Написание REST API, который вызывает метод из класса по работе с данными.

### Этап 2

Добавлено ещё три метода:
        
GET /submitData/ — получить одну запись (перевал) по её id. 

PATCH /submitData/{id}/ — редактирование существующей записи, если она в статусе new. Редактировать можно все поля, кроме тех, что содержат в себе ФИО, адрес email и номер телефона. Метод принимает тот же самый json, который принимал уже реализованный метод submit-data. Возвращаются 2 значения: status и message.

 GET /submitData/?user__email=<email> — список данных обо всех объектах, которые пользователь с почтой отправил на сервер.

### Этап 3

* Добавление в Readme.md документации к REST API
        
* Документация с помощью Swagger
        
* Покрыть код тестами

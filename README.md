# Тестовое задание для "Фаблайт Электроникс" - приложение для управления пользователями

# Требования:
* Разработать простое серверное приложение на выбранном вами языке программирования Python.
* Реализовать базу данных PostgreSQL.
* Реализовать функции регистрации и аутентификации пользователей.
* Реализовать обработку следующих типов запросов:
* Получение списка пользователей.
* Добавление нового пользователя.
* Обновление информации о пользователе.
* Удаление пользователя.
* Обеспечить минимальную защиту приложения (например, защита от SQL-инъекций).

# Технологии
* Сервис реализован на DjangoRestFramework
* Python версии 3.11
* База данных - PostgreSQL
* ORM - DjangoORM
* Проект разворачивается с помощью docker compose
* Релизован pre-commit - при коммите код проверяется линтером и автоматически исправляются ошибки 
* Использована автосхема документации Swagger

## Установка и запуск:

# Предварительные условия
 
Предполагается, что пользователь установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине или на удаленном сервере, где проект будет запускаться в контейнерах. Проверить наличие можно выполнив команды:

```bash
docker --version && docker-compose --version
```
<h1></h1>
  
# Локальный запуск: Docker Compose

1. Клонируйте репозиторий с GitHub переменные окружения уже находятся в корневой папке проекта для удобства:

```bash
git clone git@github.com:LoG1s7/test-task-fablite.git && \
cd test-task-fablite&& \
```
2. Создайте файл ".env" в папке "test-task-fablite". Пример наполнения в файле ".env.example"
```bash
cd test-task-fablite && touch .env
```  
3. Из корневой директории проекта выполните команду:
```bash
sudo docker compose -f infra/docker-compose.yml up -d --build
```
  Проект будет развернут в трех docker-контейнерах (db, web, nginx) по адресу http://localhost/api/.

4. Чтобы выполнить миграции выполните команду:
```bash
sudo docker compose -f infra/docker-compose.yaml exec web python manage.py migrate
```
5. Чтобы собрать статические файлы выполните команду:
```bash
sudo docker compose -f infra/docker-compose.yaml exec web python manage.py collectstatic --no-input
```
6. Чтобы создать суперюзера выполните команду и следуйте инструкции:
```bash
sudo docker compose -f infra/docker-compose.yaml exec web python manage.py createsuperuser
```
7. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```bash
sudo docker compose -f infra/docker-compose.yml down
```
  Если также необходимо удалить том базы данных:
```bash
docker compose -f infra/docker-compose.yml down -v
```
#### Админ-панель Django
```bash
http://localhost/admin
```
#### Документация API
```bash
http://localhost/api/docs
```
<h1></h1>

## Автор
[Aleksandr Kolesnikov](https://github.com/log1s7)

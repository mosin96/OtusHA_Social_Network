# Учебный сервер для социальной сети курса Otus HA

## Обзор проекта

Этот проект использует [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Подготовка к запуску

### Изменение файла с переменными окружения

При необходимости замените дефолтные значения переменных окружения для работы с БД в файле **docker/.env-postgresql**
```
DATABASE_PORT=5432
DATABASE_DIALECT=postgresql
POSTGRES_DB=HA_SN_db
POSTGRES_USER=HA_SN_user
POSTGRES_PASSWORD=HA_SN_password
POSTGRES_HOST=postgres
```
## Запуск через Docker

### Соберите и запустите через Docker compose

```commandline
docker compose up
```
## Использование

### Postman collection

Коллекция расположена тут:

**postman_collection/OTUS HA Social Network.postman_collection.json**

### pgAdmin

Зайдите на http://localhost:5050/browser/ для работы с БД через pgAdmin

Для подключения к БД используйте данные из файла с переменными окружения **docker/.env-postgresql**

### SwaggerUI

Зайдите на http://localhost:8280/ui/ для просмотра спеки и отправки тестовых запросов

### Jmeter data for tests

Скачайте файл [Тестовая выборка](https://raw.githubusercontent.com/OtusTeam/highload/master/homework/people.v2.csv) в 
директорию extra_files. И запустите скрипт extra_files/prepare_data.py для генерации подготовленных тестовых данных.
Результат появится там же с именем people.v3.csv

Примеры скриптов Jmeter для регистрации пользователей и поиска на разных потоках лежат там же в extra_files.
Перед запуском замените путь до файла people.v3.csv на актуальный для вашей машины  и обновите адрес сервера, если
запуск не на одной машине. Также обновите токен для запросов на полученный в методе /login
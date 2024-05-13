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

### pgAdmin

Зайдите на http://localhost:5050/browser/ для работы с БД через pgAdmin

Для подключения к БД используйте данные из файла с переменными окружения **docker/.env-postgresql**

### SwaggerUI

Зайдлите на http://localhost:8280/ui/ для просмотра спеки и отправки тестовых запросов
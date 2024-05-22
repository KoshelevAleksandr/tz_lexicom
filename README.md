# tz_lexicom

1. Небходимо разработать сервис с использование FastAPI и Redis.

##### Команда для запуска сервиса:

``docker compose -f docker-compose-local.yaml up -d --build``
или
``Make up``

2. Даны 2 таблица PostgreSQL. Необходимо перенести данные о статусе из таблицы short_name в таблицу full_name.

``UPDATE full_names fn
SET status = sn.status
FROM short_names sn
WHERE sn.name = LEFT(fn.name, POSITION('.' in fn.name) - 1) or sn.name = fn.name
``
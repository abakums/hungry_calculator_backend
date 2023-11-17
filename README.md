# Hungry calculator backend

Backend для проекта Hungry calculator, содержащий API и базу данных на Django + PostgreSQL. 

## Запуск проекта

Для запуска проекта необходимо создать файл .env такой же структуры, как и .env.example, заполнить настройки базы данных.\
POSTGRES_HOST указать значением database (название контейнера) при запуске через docker-compose.yml файла.

После этого необходимо выполнить команду из главной директории, где находится файл docker-compose.yml:

`docker-compose up -d --build`

После завершения работы с проектом нужно выполнить команду из той же директории:

`docker-compose down`

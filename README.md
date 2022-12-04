
## Запуск проекта
        docker-compose up -d --build
    
        docker-compose exec servicedb alembic init -t async migrations
    
        docker-compose exec servicedb alembic revision --autogenerate -m "init"

        docker-compose exec servicedb alembic upgrade head

____
## Ссылка для запуска страницы обращения
        http://localhost:8000/
____
## PGAdmin
    http://localhost:5050/
    
    user:pgadmin4@pgadmin.org
    password=admin

    Подключение сервера:
        Host:db
        Maintenance database:postgres
        Username:postgres
        Password:postgres
____
## RabbitMQ
    http://localhost:15672/
    
    user:guest
    password:guest
____
## Удаление проекта
        docker-compose down -v
____
## WARNING!
    Иногда, впервые запуская проект, контейнер "servicedb" или "db" надо перезагрузить, перед использованием docker-compose exec 
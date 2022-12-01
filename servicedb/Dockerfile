FROM python:3.10
EXPOSE 4369 5671 5672 8000 25672
WORKDIR /servicedb
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY *.py /servicedb/
COPY ./sql_app /servicedb/sql_app/
COPY ./alembic /servicedb/alembic/
COPY alembic.ini /servicedb/
COPY .env /servicedb/

FROM python:3.10
EXPOSE 8888 8000

WORKDIR /backend
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py /backend/
CMD ["python", "main.py"]

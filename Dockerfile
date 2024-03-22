FROM python:3.11-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt && python manage.py migrate
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
EXPOSE 8000
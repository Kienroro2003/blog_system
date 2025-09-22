# services/news-service/Dockerfile

FROM python:3.11-slim

WORKDIR /code

# Cài đặt gunicorn
RUN pip install gunicorn

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 8000

# Chạy ứng dụng bằng gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.main:app"]

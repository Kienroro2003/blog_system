# services/user-service/Dockerfile (và 2 services còn lại)

# Sử dụng image Python chính thức
FROM python:3.11-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /code

# Sao chép file requirements và cài đặt thư viện
# Làm bước này riêng để tận dụng cache của Docker
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Sao chép toàn bộ code của ứng dụng vào container
COPY ./app /code/app

# Mở port 8000 để uvicorn chạy
EXPOSE 8000

# Lệnh để chạy ứng dụng khi container khởi động
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

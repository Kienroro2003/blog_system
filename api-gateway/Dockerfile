# api-gateway/Dockerfile

# Sử dụng image Nginx chính thức
FROM nginx:1.25-alpine

# Xóa file config mặc định
RUN rm /etc/nginx/conf.d/default.conf

# Sao chép file config của chúng ta vào đúng vị trí
COPY ./config/nginx.conf /etc/nginx/conf.d/

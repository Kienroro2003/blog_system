# Hệ thống Blog Microservices

Đây là một hệ thống blog được xây dựng theo kiến trúc Microservices, bao gồm các dịch vụ chính: **User Service**, **News Service**, và **Search Service**. Hệ thống sử dụng Docker để đóng gói và quản lý các services một cách dễ dàng.

## Kiến trúc hệ thống

Hệ thống bao gồm các thành phần sau:

- **API Gateway (Nginx):** Là điểm vào duy nhất cho tất cả các request từ client, có nhiệm vụ điều hướng request đến các service tương ứng.
- **User Service (Flask):** Quản lý tất cả các nghiệp vụ liên quan đến người dùng, bao gồm đăng ký, đăng nhập và xác thực.
- **News Service (Flask):** Quản lý các nghiệp vụ liên quan đến bài viết như tạo, đọc, cập nhật, và xóa bài viết.
- **Search Service (FastAPI):** Cung cấp khả năng tìm kiếm bài viết (sẽ được phát triển trong tương lai).
- **MySQL Databases:** Mỗi service (User và News) có một database riêng để đảm bảo tính độc lập.
- **Redis:** Được sử dụng làm cache cho News Service để tăng tốc độ truy vấn dữ liệu.

## Yêu cầu cài đặt

Trước khi bắt đầu, hãy đảm bảo bạn đã cài đặt các công cụ sau trên máy của mình:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/) (thường được cài đặt sẵn cùng với Docker Desktop)

## Hướng dẫn cài đặt và khởi chạy

Thực hiện theo các bước sau để khởi chạy toàn bộ hệ thống trên máy cục bộ của bạn.

### 1\. Sao chép (Clone) mã nguồn

Sao chép mã nguồn của dự án từ repository về máy của bạn:

```bash
git clone <URL_CỦA_REPOSITORY>
cd <TÊN_THƯ_MỤC_DỰ_ÁN>
```

### 2\. Khởi chạy hệ thống bằng Docker Compose

Lệnh duy nhất bạn cần để khởi động toàn bộ các services (bao gồm cả databases và Redis) là:

```bash
docker-compose up --build
```

**Giải thích các tham số:**

- `up`: Khởi động và chạy các container.
- `--build`: Yêu cầu Docker Compose xây dựng lại các images từ Dockerfile trước khi khởi động. Bạn nên dùng tham số này trong lần chạy đầu tiên hoặc khi có thay đổi trong mã nguồn hoặc `requirements.txt`.

Sau khi chạy lệnh trên, Docker Compose sẽ:

1.  Tải về các images cần thiết (Python, MySQL, Redis, Nginx).
2.  Xây dựng images cho từng service của bạn.
3.  Khởi tạo các container cho tất cả các service được định nghĩa trong `docker-compose.yml`.
4.  Kết nối chúng vào cùng một mạng ảo để chúng có thể giao tiếp với nhau.

Quá trình này có thể mất vài phút trong lần chạy đầu tiên.

### 3\. Kiểm tra trạng thái các services

Để kiểm tra xem tất cả các container đã khởi động và đang chạy ổn định hay chưa, bạn có thể mở một cửa sổ terminal mới và chạy lệnh:

```bash
docker-compose ps
```

Bạn sẽ thấy danh sách các container và trạng thái (State) của chúng. Tất cả nên ở trạng thái `Up` hoặc `running`.

### 4\. Truy cập hệ thống

Sau khi tất cả các services đã khởi động thành công, bạn có thể bắt đầu tương tác với hệ thống thông qua API Gateway:

- **API Gateway:** `http://localhost:8080`
- **User Service:** Các request đến `http://localhost:8080/api/users/...` sẽ được chuyển đến User Service.
- **News Service:** Các request đến `http://localhost:8080/api/news/...` sẽ được chuyển đến News Service.

Bạn có thể sử dụng các công cụ như [Postman](https://www.postman.com/) hoặc `curl` để gửi request đến các endpoints này.

## Dừng hệ thống

Để dừng tất cả các container đang chạy, hãy quay lại cửa sổ terminal nơi bạn đã chạy lệnh `docker-compose up` và nhấn `Ctrl + C`.

Nếu bạn muốn dừng và xóa các container, hãy chạy lệnh:

```bash
docker-compose down
```

Để xóa cả các volumes (dữ liệu trong database), thêm cờ `--volumes`:

```bash
docker-compose down --volumes
```

**Lưu ý:** Lệnh này sẽ **xóa toàn bộ dữ liệu** người dùng và bài viết.

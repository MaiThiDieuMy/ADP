# Ứng dụng Web Quản lý Điểm Sinh viên

## Tổng quan

Ứng dụng web được thiết kế để quản lý điểm sinh viên với hai vai trò chính:

- **Admin**:

  - Quản lý tài khoản giáo viên
  - Phân quyền môn học và lớp học

- **Giáo viên**:
  - Quản lý điểm sinh viên
  - Xem phân công và thông tin cá nhân

## Cấu trúc giao diện và tính năng

### 1. Trang chủ (Home)

#### Nội dung hiển thị:

- Thông điệp chào mừng: _"Chào mừng đến với Hệ thống Quản lý Điểm Sinh viên! Vui lòng đăng nhập để bắt đầu."_
- Nút đăng nhập dẫn đến trang đăng nhập duy nhất

#### Mục đích:

- Giao diện đơn giản, thân thiện
- Cung cấp điểm truy cập chính vào hệ thống

## 2. Đăng nhập và Phân quyền

### Đăng nhập

- Trang đăng nhập duy nhất cho mọi vai trò
- Người dùng nhập tên đăng nhập và mật khẩu
- Hệ thống tự động phân quyền dựa trên vai trò:
  - Admin: Chuyển đến trang quản trị
  - Giáo viên: Chuyển đến trang phân công và quản lý điểm
- Có chức năng Quên mật khẩu (gửi email hoặc thông báo cho admin)

### Vai trò Admin

#### Quản lý giáo viên

- **Danh sách giáo viên**
  - Hiển thị: Tên, trạng thái (hoạt động/khóa), nút Xóa, nút Khóa/Mở khóa
  - Xác nhận trước khi thực hiện các thao tác quan trọng
  - Thêm giáo viên mới qua form nhập thông tin
  - Xem chi tiết giáo viên: thông tin cá nhân, reset mật khẩu

#### Phân quyền môn học và lớp học

- **Quản lý môn học**
  - Xem danh sách môn học hiện có
  - Thêm môn học mới
- **Quản lý lớp học**
  - Liên kết lớp học với môn học
  - Thêm lớp học mới (mã lớp, tên lớp)
  - Có thể thêm nhiều lớp cho một môn học

### Vai trò Giáo viên

#### Trang chính

- **Phân công giảng dạy**
  - Danh sách môn học được phân công
  - Lọc theo học kỳ
  - Tìm kiếm môn học theo tên
  - Xem danh sách lớp học cho từng môn

#### Quản lý điểm

- **Bảng điểm sinh viên**
  - Hiển thị: Mã số SV, Tên SV, các cột điểm (miệng, 15p, thi)
- **Nhập điểm**
  - Nhập điểm từng ô
  - Nhập điểm hàng loạt
  - Import từ file Excel (có template mẫu)
- **Chỉnh sửa điểm**
  - Sửa/xóa điểm
  - Lưu lịch sử chỉnh sửa (người sửa, thời gian)

#### Thông tin cá nhân

- Xem và chỉnh sửa thông tin
- Đổi mật khẩu
- Đăng xuất

### Tính năng bổ sung

#### Thông báo và xác nhận

- Xác nhận các thao tác quan trọng
- Thông báo kết quả thao tác

#### Tìm kiếm và lọc

- Tìm kiếm theo tên môn học
- Lọc theo học kỳ
- Hiển thị môn học kèm học kỳ

### Quy trình hoạt động mẫu

#### Admin

1. Đăng nhập
2. Thêm giáo viên mới
3. Phân công môn học
4. Liên kết lớp học
5. Quản lý trạng thái tài khoản giáo viên

#### Giáo viên

1. Đăng nhập
2. Xem phân công giảng dạy
3. Chọn lớp và môn học
4. Nhập/sửa điểm
5. Theo dõi lịch sử chỉnh sửa

### Đánh giá tổng quan

- Giao diện đơn giản, thân thiện
- Hệ thống đăng nhập thông minh với phân quyền tự động
- Quản lý môn học/lớp học linh hoạt
- Đa dạng phương thức nhập điểm
- Tính năng tìm kiếm và lọc hiệu quả

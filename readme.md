Mô tả dự án: Ứng dụng web quản lý điểm sinh viên
Tổng quan:  
Ứng dụng web này được thiết kế để quản lý điểm sinh viên với hai vai trò chính:

Admin: Quản lý tài khoản giáo viên, phân quyền môn học và lớp học.
Giáo viên: Quản lý điểm sinh viên, xem phân công và thông tin cá nhân.

Cấu trúc giao diện và tính năng chi tiết:
1. Trang đầu tiên (Home):
Nội dung hiển thị:
Một thông điệp chào mừng, ví dụ:
"Chào mừng đến với Hệ thống Quản lý Điểm Sinh viên! Vui lòng đăng nhập để bắt đầu."
Logo của trường hoặc hệ thống (nếu có).
Nút Đăng nhập dẫn đến trang đăng nhập duy nhất.
Mục đích: Đơn giản, thân thiện, cung cấp điểm truy cập chính vào hệ thống.
**2. Đăng nhập:**
Trang đăng nhập duy nhất:
Không tách riêng "Đăng nhập với admin" và "Đăng nhập thông thường".
Người dùng nhập tên đăng nhập và mật khẩu.
Hệ thống tự động phân quyền dựa trên vai trò:
Nếu là admin: Chuyển đến trang quản trị.
Nếu là giáo viên: Chuyển đến trang phân công và quản lý điểm.
Có nút Quên mật khẩu để yêu cầu reset (gửi email hoặc thông báo cho admin).
Vai trò Admin:
Trang quản trị:
Quản lý giáo viên:
Danh sách giáo viên:
Hiển thị: Tên, trạng thái (hoạt động/khóa), nút Xóa, nút Khóa/Mở khóa.
Khi nhấn Xóa hoặc Khóa/Mở khóa: Hiện thông báo xác nhận (VD: "Bạn có chắc muốn xóa giáo viên này?").
Nút Thêm giáo viên:
Mở form nhập thông tin (tên, email, số điện thoại, v.v.) và tạo tài khoản với mật khẩu mặc định.
Click vào tên giáo viên: Chuyển đến trang chi tiết:
Thông tin cá nhân: Xem và chỉnh sửa (tên, email, số điện thoại, v.v.).
Reset mật khẩu: Tạo mật khẩu mới và gửi thông báo cho giáo viên (VD: qua email).
Phân quyền môn học và lớp học:
Chọn môn học:
Hiển thị danh sách môn học có sẵn (VD: Toán, Lý, Hóa).
Nút Thêm môn học mới để nhập tên môn nếu cần.
Liên kết lớp học:
Mỗi môn học có nút Chọn lớp học.
Hiển thị danh sách lớp học có sẵn (VD: Lớp 10A1, 10A2).
Nút Thêm lớp học mới để nhập thông tin lớp (mã lớp, tên lớp).
Admin có thể thêm nhiều lớp cho một môn học.
Vai trò Giáo viên:
Trang chính:
Phân công của tôi:
Danh sách môn học:
Hiển thị các môn học được phân công (VD: "Toán - HK1 2022-2023").
Nút chọn học kỳ: Lọc môn học theo học kỳ (VD: HK1 2022-2023, HK2 2022-2023).
Thanh tìm kiếm: Tìm môn học theo tên (VD: nhập "Toán" để lọc).
Click vào môn học:
Hiển thị danh sách lớp học (VD: Lớp 10A1, 10A2).
Click vào lớp học:
Hiển thị bảng điểm sinh viên:
Cột: Mã số sinh viên, Tên sinh viên, các cột điểm (VD: Điểm miệng, Điểm 15p, Điểm thi).
Quản lý điểm:
Nhập từng ô: Giáo viên nhập điểm trực tiếp vào ô tương ứng.
Nhập hàng loạt: Chọn nhiều sinh viên và nhập điểm cùng lúc (VD: nhập 8.0 cho cả cột Điểm thi).
Tải file Excel: Tải file chứa danh sách sinh viên và điểm lên hệ thống (có template mẫu).
Xóa/Sửa điểm:
Giáo viên có thể chỉnh sửa hoặc xóa điểm.
Lịch sử chỉnh sửa: Lưu thông tin ai sửa (tên giáo viên), sửa khi nào (ngày giờ).
Thông tin cá nhân:
Xem và chỉnh sửa: Tên, email, số điện thoại, v.v.
Đổi mật khẩu:
Nhập mật khẩu cũ và mật khẩu mới để thay đổi.
Đăng xuất:
Thoát khỏi hệ thống và quay về trang Home.
Các tính năng bổ sung:
Thông báo và xác nhận:
Các hành động quan trọng như Xóa tài khoản giáo viên, Khóa/Mở khóa, Reset mật khẩu đều hiện thông báo xác nhận (VD: "Bạn có chắc chắn muốn thực hiện hành động này?").
Quản lý điểm:
Hỗ trợ 3 cách nhập điểm: Nhập từng ô, nhập hàng loạt, tải file Excel.
Lưu trữ lịch sử chỉnh sửa điểm (giáo viên nào, thời gian nào).
Tìm kiếm và lọc:
Thanh tìm kiếm trong "Phân công của tôi" tìm theo tên môn học.
Nút chọn học kỳ để lọc môn học trong học kỳ đó.
Tên môn học hiển thị kèm học kỳ (VD: "Toán - HK1 2022-2023").
Quy trình hoạt động mẫu:
Admin:
Đăng nhập → Thêm giáo viên A → Phân môn "Toán" → Liên kết lớp "10A1" và "10A2".
Khóa tài khoản giáo viên B → Xác nhận → Thông báo thành công.
Giáo viên:
Đăng nhập → Vào "Phân công của tôi" → Chọn HK1 2022-2023 → Tìm "Toán" → Chọn lớp "10A1".
Nhập điểm: Nhập 8.0 cho sinh viên X (từng ô) → Tải file Excel cho toàn lớp → Sửa điểm sinh viên Y từ 7.0 thành 8.5 (lịch sử lưu: "Giáo viên A sửa ngày 20/03/2025").
Đánh giá tổng quan:
Dự án của bạn giờ đây đã rõ ràng hơn với:

Trang Home đơn giản, tập trung vào chào mừng và đăng nhập.
Hệ thống đăng nhập thông minh, tự phân quyền.
Quy trình phân quyền môn học/lớp học linh hoạt (chọn sẵn hoặc thêm mới).
Quản lý điểm đa dạng (3 cách nhập) và có lịch sử chỉnh sửa.
Tính năng tìm kiếm và lọc hiệu quả với học kỳ

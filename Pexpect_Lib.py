# Pexpect: Thư viện Python 
# Cho phép tự động hóa tương tác với các ứng dụng dựa trên văn bản. 
# Thư viện này mô phỏng hành vi của người dùng bằng cách gửi và nhận dữ liệu qua giao diện dòng lệnh:
# Tự động hóa các tác vụ: Pexpect có thể tự động hóa các thao tác lặp đi lặp lại trong các ứng dụng như:
# ------------------------------------------------------------------
# Đăng nhập
# Thực thi lệnh
# Truy xuất dữ liệu
# Chuyển đổi tập tin
# ------------------------------------------------------------------
# Pexpect có thể tương tác với nhiều loại ứng dụng khác nhau, bao gồm:
# Telnet
# SSH
# FTP
# Expect
# Ứng dụng Python
# -------------------------------------------------------------------
# Pexpect cung cấp API đơn giản và dễ sử dụng, giúp bạn dễ dàng viết script tự động hóa.

# Dòng code này import thư viện pexpect vào chương trình.
# Ví dụ sau mô tả tập lệnh python sử dụng để đăng nhập từ xa qua giao thức SSH.
import pexpect

# Tạo kết nối SSH
# Dòng code này sử dụng hàm pexpect.spawn() để tạo kết nối SSH với máy chủ có địa chỉ 'host' và tên người dùng 'user'.
child = pexpect.spawn('ssh user@host')

# Đăng nhập
# Sử dụng phương thức expect() để chờ đợi prompt "Password:" xuất hiện. 
# Khi prompt xuất hiện, dòng code tiếp theo sử dụng phương thức sendline() để gửi mật khẩu "password" cho máy chủ.
child.expect('Password:')
child.sendline('password')

# Thực thi lệnh
# Phương thức expect() để chờ đợi prompt "$" xuất hiện, cho biết lệnh đã được thực thi thành công.
child.expect('$')
child.sendline('ls -l')

# Lấy kết quả
# Dòng code này sử dụng phương thức read() để lấy kết quả của lệnh 'ls -l' và lưu trữ vào biến 'result'.
result = child.read()

# Đóng kết nối.
child.close()

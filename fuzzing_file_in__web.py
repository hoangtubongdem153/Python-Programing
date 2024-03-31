# Nhập module request để thực hiện các request http và nhận phản hồi
import requests
# Thực hiện lấy domain người dùng nhập vào từ bàn phím
domain = input("Nhap domain to de kiem tra: ").strip()
# Tạo mảng list[] để lưu các tên miền trong file Logins.txt
logins = []
# Xử dụng with để thao tác đóng mở file đúng cách , thực hiện mở file Logins.txt ở chế độ chỉ đọc "r"
# file Logins.txt là file chứa các đường dẫn trang đăng nhập phổ biến
with open('Logins.txt', 'r') as file_list:
    # Duyệt qua từng dòng trong file , sử dụng [:-1] để loại bỏ ký tự xuống dòng trên mỗi dòng
    for line in file_list:
        line = line[:-1]
        # Thêm vào mảng logins
        logins.append(line)
# Lặp qua từng giá trị trong danh sách logins vừa tạo 
for login in logins:
    # Tạo yêu cầu và biến 'res' để lưu phản hồi
    print("Dang kiem tra..." + domain + login)
    res = requests.get(domain+login)
    # Kiểm tra nếu phản hồi thành công (có mã trạng thái là 200) , in ra thông báo 'Da tim thay'
    if res.status_code == 200: 
        print("Da tim thay : " + login)

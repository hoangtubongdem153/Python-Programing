# Nhập module shodan để sử dụng , ( cài đặt với cú pháp: pip3 install shodan)
import shodan

# Nhập địa chỉ IP từ bàn phím
ip_address = input("Nhập địa chỉ IP: ")

# Tạo API key Shodan, sử dụng API key từ account.shodan.io với đăng nhập tài khoản đã đăng ký
SHODAN_API_KEY = "QLENmb3lHhc4vb9hpi4EBExdIHAmpi6z"

# Khởi tạo đối tượng API Shodan từ class Shodan()
api = shodan.Shodan(SHODAN_API_KEY)

# Truy vấn thông tin IP, sử dụng try-except để bắt lỗi khi có lỗi xảy ra 
try:
    # Tìm kiếm thông tin IP
    host = api.search(ip_address)

    # In thông tin cơ bản
    print("IP:", host['ip_str'])
    print("Hệ điều hành:", host['os'])
    print("Hostname:", host['hostname'])
    print("Cổng mở:", host['ports'])

    # In thông tin chi tiết
    for data in host['data']:
        print(data)
# Xử lý nếu có exception , error , in ra lỗi
except shodan.APIError as e:
    print("Lỗi API Shodan:", e)

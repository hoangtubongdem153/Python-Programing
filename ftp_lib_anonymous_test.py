# Sử dụng thư viện ftplib trong Python để build một tập
# lệnh nhỏ nhằm xác định xem máy chủ FTP có cung cấp 
# đăng nhập ẩn danh (anonymous) hay không.

# Import thư viện ftplib, có các chức năng tương tác với máy chủ FTP.
import ftplib
# Tạo hàm kiểm tra kết nối anonymous(ẩn danh) tới FTP server.
# hostname param chỉ định địa chỉ của máy chủ
def test_Login_Anonymous(hostname):
    try: 
        # Tạo đối tượng FTP client để kết nối
        ftp = ftplib.FTP(hostname)
        # Thực hiện login() để kết nối, tham số user='anonymous' và passwd tùy ý!
        ftp.login('anonymous','any_thing')
        # Nếu thực thi k có except , in ra Succeeded và đóng kết nối
        print('\n[*] '+ str(hostname) + ' FTP Anonymous Login Succeeded!')
        ftp.quit()
        return True
    except Exception:
        print('\n[*] '+ str(hostname) + ' FTP Anonymous Login Failed!')
        return False
# Thực hiện test với host bất kỳ.
host = '10.10.10.10'
test_Login_Anonymous(host)

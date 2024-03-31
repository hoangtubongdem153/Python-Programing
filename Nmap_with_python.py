# Nhập mô đun nmap để thực hiện sử dụng công cụ này trên python
# Nếu chưa có , có thể cài đặt theo cú pháp : "pip3 install python-nmap"
import nmap
# Tạo một đối tượng PortScanner()
scanPort = nmap.PortScanner()
# Nhập địa chỉ IP cần scan
host_scan = input("Nhap IP cua Host to scan: ")
# chỉ định phạm vi của port thực hiện quét
port_range = input("Nhap pham vi scan <min-max>: ")
# Thực hiện scan, đối tượng scanPort lưu kết quả scanning 
# Sử dụng tùy chọn -n ( disable phân giải tên miền) giúp việc scanning nhanh hơn , -p để chỉ định phạm vi cổng cần quét
scanPort.scan(hosts=host_scan, arguments='-n -p'+port_range)
# In ra chính xác câu lệnh nmap được chạy 
print(scanPort.command_line())
# Tạo danh sách hosts_list lưu giữ các cặp (tuple) địa chỉ IP và trạng thái (state) của địa chỉ IP đó
hosts_list = [(x, scanPort[x]['status']['state']) for x in scanPort.all_hosts()]
# duyệt qua mảng hosts_list trên 
for host, status in hosts_list:
    # In ra host và trạng thái của nó ( mở, đóng)
    print(host, status)
    # Sử dụng vòng lặp for để duyệt qua tất cả các protocol của host 
    for protocol in scanPort[host].all_protocols():
        # In ra phương thức protocol 
        print('Protocol: ',protocol)
        # Sử dụng keys() để lấy danh sách các key trong dictionary 'scanPort[host][protocol]' 
        # có dạng như: ' {23: {'state': 'filtered', 'reason': 'no-response', 'name': 'telnet'}'
        # ta được port list là listport bên dưới
        listport = scanPort[host][protocol].keys()
        # Sử dụng vòng lặp for lặp qua từng port trong listport 
        # Sau đó in kết quả 
        print(scanPort[host])
        for port in listport:
            print('Port:{} State:{} '.format(port, scanPort[host][protocol][port]['state']))

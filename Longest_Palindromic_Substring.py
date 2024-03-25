# Given a string s, return the longest palindromic substring in s
# Palindromic :A string is palindromic if it reads the same forward and backward
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

#   Example 2:
# Input: s = "cbbd"
# Output: "bb"
# Ý tưởng thực hiện: 
# viết hàm kiểm tra từ một vị trí  , kiểm tra phía trái (left) và phía phải (right) của vị trí đó , nếu khớp tiếp tục so sánh các 
# ký tự  tiếp theo ở 2 bên left , right .
# điều kiện cho vòng lặp thực hiện kiểm tra là left >=0 , right < n = len(string_input)
# Triển khai: 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_str = s[0]
        # hàm thực hiện kiểm tra substring palindrome từ một ví trí trung tâm
        # sử dụng 2 biến left và right để lưu giá trị vị trí của phần tử đang được kiểm tra ở 2 phía : left and right 
        def expand_center(left, right):
            # điều kiện lặp dừng khi hàm kiểm tra đến các giá trị ngoài cùng trái hoặc phải , hoặc 2 ký tự 2 phía đang được so sánh không giống nhau.
            while left >=0 and right < n and s[left]==s[right]:
                # thỏa mãn điều kiện , tiếp tục tăng right lên 1 và giảm left đi 1 để tiếp tục so sánh
                left -= 1
                right +=1
            # trả về substring palindrome sau khi kiểm tra từ các vị trí cho trước (left, right)
            return s[left+1:right]
        # sử dụng vòng lặp để kiểm tra từng vị trí
        for i in range(0,n-1):
            # Có 2 trường hợp về độ dài chuỗi 
            # 1. nếu độ dài chuỗi substring cần tìm lẻ , ta gán left và right của hàm kiểm tra substring 'expand_center' cùng một giá trị ( do khi mở rộng 2 bên từ 1 vị trí
            # độ dài của chuỗi sẽ là lẻ
            odd = expand_center(i,i)
            # 2. nếu rơi vào trường hợp substring cần tìm là chẵn , ta sử dụng 2 biến left và right có giá trị liên tiếp nhau, kiểm tra 2
            # vị trí liên tiếp với hàm 'expand_center' , kết quả trả về substring palindrome là chuỗi chẵn
            even = expand_center(i, i+1)
            # thực hiện so sánh sau mỗi lần kiểm tra , cả odd và even vì mục tiêu tìm substring palindrome có độ dài lớn nhất.
            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even
        return max_str 

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1.Open brackets must be closed by the same type of brackets.
# 2.Open brackets must be closed in the correct order.
# 3.Every close bracket has a corresponding open bracket of the same type.
# Ý tưởng là sẽ ứng dụng stack để lưu các ngoặc mở , sau đó kiểm tra các ngoặc đóng xem có khớp với ngoặc mở hay không
# sử dụng dict để lưu các cặp ngoặc đóng và mở dạng 'key':'value' để ta có thể so khớp.
  
class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {'{':'}', '[':']', '(':')'}
        # Tạo danh sách để lưu các cặp ngoặc mở
        stack = []
        # Nếu giá trị của chuỗi đầu vào lẻ , return False
        if len(s) % 2 != 0: 
            return False 
        for char in s:
            if char in bracket: 
                stack.append(char)
            # Kiểm tra stack có rỗng hay không và ngoặc đóng có phù hợp không, nếu thỏa mãn điều kiện return False
            elif not stack or bracket[stack.pop()] != char: 
                return False
        # Sau khi so sánh khớp , nếu stack rỗng , return True , else return False
        if not stack : 
            return True
        return False
print(Solution().isValid("(("))

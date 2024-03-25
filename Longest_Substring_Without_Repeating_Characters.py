# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Ý tưởng 1: 
# tạo một set để chứa các ký tự duy nhất (kiểu queue) , lặp qua từng ký tự trong string input rồi thêm vào set
# nếu ký tự được thêm vào đã có thì thực hiện xóa nó đi khỏi set rồi thêm ký tự đó vào 
# sử dụng biến a để đếm vị trí ký tự đầu ở string input còn trong queue
 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = set()
        # Sử dụng a để lưu chỉ số ký tự (đầu tiên còn trong queue) trong input string 's'
        # Sử dụng b để lưu giá trị max của chuỗi tìm được trong quá trình kiểm tra
        a,b = 0,0 
        for i in range(len(s)):
            # Nếu phần tử s[i] đang kiểm tra hiện có trong queue , loại bỏ phần tử đầu tiên của queue :s[a] ( tham chiếu tới phần tử thứ a trong 's' do set queue không có chỉ mục index cho phần tử)
            while s[i] in stack: 
                stack.remove(s[a])
                a += 1
            # Thực hiện thêm phần tử s[i] vào queue 
            stack.add(s[i])
            b = max(b,i-a +1)
        # Trả về độ dài chuỗi lớn nhất tìm được 
        return b
# Ý tưởng 2: tương tự , nhưng sử dụng stack kiểu list[]
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         stack = []
#         b = 0 
#         for i in range(len(s)):
#             while s[i] in stack: 
#                 stack.pop(0)       
#             stack.append(s[i])
#             b = max(b,len(stack))
#         return b
# Ý tưởng 3: 
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         substr = ""
#         list_len = []
#         i=0
#         while i < len(s): 
#             if s[i] not in substr:
#                 substr += s[i]
#                 i+=1
#                 if i == len(s):
#                     list_len.append(len(substr))
#                     break
#             else: 
#                 list_len.append(len(substr))
#                 i = i - len(substr) + 1
#                 substr ="" 
                 
#         return max(list_len) if list_len else 0

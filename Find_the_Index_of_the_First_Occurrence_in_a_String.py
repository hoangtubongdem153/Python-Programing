#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#Sử dụng hàm find tích hợp sẵn trong python để giải quyết bài toán :))
class Solution:
    def first_Index(self, haystack: str, needle: str) -> int:
        n2 = len(haystack)
        i = haystack.find(needle,0,n2)
        return i if i != -1 else -1
print(Solution().first_Index("hello","ll"))
# class Solution(object):
#     def first_Index(self, haystack, needle):
#         # makes sure we don't iterate through a substring that is shorter than needle
#         for i in range(len(haystack) - len(needle) + 1):
#             # check if any substring of haystack with the same length as needle is equal to needle
#             if haystack[i : i+len(needle)] == needle:
#                 # if yes, we return the first index of that substring
#                 return i
#         # if we exit the loop, return -1        
#         return -1

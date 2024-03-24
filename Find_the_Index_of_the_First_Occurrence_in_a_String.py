#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#Sử dụng hàm find tích hợp sẵn trong python để giải quyết bài toán :))
class Solution:
    def first_Index(self, haystack: str, needle: str) -> int:
        n2 = len(haystack)
        i = haystack.find(needle,0,n2)
        return i if i != -1 else -1
print(Solution().first_Index("hello","ll"))

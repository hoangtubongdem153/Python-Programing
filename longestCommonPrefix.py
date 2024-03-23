//Đoạn code tìm độ dài tiền tố chung dài nhất của các từ trong mảng từ input
class Solution:
    // Hàm tìm tiền tố chung của 2 string
    def lcpa(self, s1: str, s2: str):
        i=0 
        while i < len(s1) and i< len(s2) and s1[i] == s2[i]:
            i=i+1 
        return s1[:i] 
    // Hàm tìm tiền tố chung mảng
    def longestCommonPrefix(self, strs: list[str]):
        s=''
        if not strs:
            return ""
        prefix = strs[0]
        for char in strs[1:]:
            prefix = self.lcpa(prefix , char)
        return prefix 
        
       

# Given an integer x, return true if x is a palindrome (An integer is a palindrome when it reads the same forward and backward), and false otherwise.
class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     str_num_ = str(x)
    #     list_digit_ = list(str_num_)
    #     n = len(list_digit_)
    #     for i in range(int(n/2)):
    #         if list_digit_[i] != list_digit_[n-1-i]:
    #             return False
    #     return True
    def isPalindrome(self, x: int) -> bool: 
        if x < 0:
            return False
        reverse = 0
        num_divided = x
        while num_divided > 0: 
            digit = num_divided % 10 
            reverse = reverse*10 + digit
            num_divided = int(num_divided/10) 
        if reverse == x: 
            return True
        return False

print(Solution().isPalindrome(121))

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Ví dụ: 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

#Ý tưởng: 
#1.Tạo các list[] từ Link-list , chuyển thành số sau khi đảo ngược, cộng tổng rồi chuyển lại thành dãy list và tạo listnode từ dãy đó -> output listnode 
#2.Cộng ngược từng phần tử trong dãy có nhớ từ trái qua phải listnode rồi thêm vào listnode mới 

# Note: các cách đảo ngược chuỗi (string) trong python: 
# String_ = "Tung"
# 1. Slicing: String_ = String_[::-1]    [start:end:step]
# 2. John() and reversed() function: String_ = "".join(reversed(string))

# định nghĩa một listnode
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# xử lý
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Tạo node tail ( lưu giá trị cuối ) , head (lưu giá trị đầu)
        tail = head = ListNode()
        # mảng để lưu các giá trị trích xuất từ linklist
        list_l1 = []
        list_l2 = []
        # Thực hiện lặp while để lấy value mỗi node
        while l1: 
            list_l1.append(l1.val)
            l1 = l1.next
        while l2: 
            list_l2.append(l2.val)
            l2 = l2.next
        # Sử dụng hàm reverse() để đảo ngược list[]
        list_l1.reverse()
        list_l2.reverse()
        for digit in list_l1:
            num1 += str(digit)
        for digit in list_l2:
            num2 += str(digit)
        # Tính tổng từ 2 số được trích xuất
        sum = int(num1) + int(num2)
        # Tạo list từ các digit trong sum
        list_result = [int(digit) for digit in sum]
        # Thực hiện đảo ngược list[] với .reverse()
        list_result.reverse()
        # Tạo linklist từ list các phần tử vừa được tạo 
        for digit in list_result:
          tail.next = ListNode(digit)
          tail = tail.next
        tail.next = None
        # Trả về linklist head.next
        return head.next
        
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         tail = head = ListNode()
#         carry = 0
        
#         while l1 is not None or l2 is not None or carry != 0: 
#             if l1 is not None: 
#                 num1 = l1.val
#                 l1 = l1.next
#             else: 
#                 num1 = 0
#                 l1 = None
#             if l2 is not None: 
#                 num2 = l2.val
#                 l2 = l2.next
#             else: 
#                 num2 = 0
#                 l2 = None
#             digit = (num1 + num2 + carry) % 10 
#             carry = (num1 + num2 + carry) // 10 

#             tail.next= ListNode(digit)  
#             tail = tail.next

#         tail.next = None
#         return head.next


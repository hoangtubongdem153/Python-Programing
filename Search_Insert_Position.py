# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Ý tưởng:
# Bài toán yêu cầu viết thuật toán có độ phức tạp về mặt thời gian là O(logN),
# nên ta nghĩ ngay tới bài toán tìm kiếm nhị phân
# Thuật toán tìm kiếm nhị phân là một thuật toán hiệu quả để tìm kiếm một phần tử cụ thể 
# trong một danh sách đã được sắp xếp. Thuật toán này hoạt động bằng cách liên tục chia đôi 
# danh sách và loại bỏ một nửa không thể chứa phần tử đang tìm kiếm.
# Thực hiện : 
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Tạo left và right để lưu vị trí đầu và cuối dãy đang tìm kiếm
        left, right = 0 , len(nums)-1
        while left < right:  
            # biến n được sử dụng để lưu giá trị vị trí giữa trong tìm kiếm nhị phân
            n = (right+left) // 2      
            if (nums[n] == target):
                return n
            # Thực hiện thay đổi vị trí left , right nếu không thỏa mãn điều kiện 
            elif nums[n] > target:
                right = n 
            else: 
                left = n+1
        # Trả về left+1 hoặc left tùy theo điều kiện ( đây là vị trí có thể chèn vào được nếu không tìm thấy 'target' trong mảng
        return left+1 if nums[left] < target else left 
print(Solution().searchInsert([1,3,5,6], 5))    # output: 2

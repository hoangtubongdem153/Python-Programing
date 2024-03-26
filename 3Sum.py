# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
----------------------------------
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Ý tưởng: 
Ta sử dụng list kiểu set để lưu giá trị các bộ 3 duy nhất
Để dễ dàng tính toán tìm kiếm với độ phức tạp O(1) , ta tạo 2 bộ set() cho các dãy số âm và dương (chứa các giá trị không trùng lặp)
Trước tiên kiểm tra các bộ 3 có số 0
Sau đó sử dụng vòng lặp lặp qua 2 giá trị 1 trong 2 dãy âm hoặc dương, sau đó lấy -1*(sum) so sánh với giá trị trong dãy còn lại
Sau khi tìm được kết quả , vì để set chỉ lưu các bộ 3 duy nhất không theo thứ tự 
Ta cần sắp xếp chúng thành các dãy tăng dần sử dụng hàm sorted(list[])
Sau đó cho vào tuple(tương tự như list, nếu dùng list sẽ trả về lỗi khi thêm vào set ( unhashable type 'list') rồi mới có thể add vào set được 
# Thực hiện :
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        set_result = set()
        n, p , z = [], [], []
        for i in nums: 
            if i> 0: 
                p.append(i)
            if i < 0: 
                n.append(i)
            if i == 0:
                z.append(i)
        N, P = set(n), set(p)
        if z: 
            for i in N:
                if -1*i in P:
                    set_result.add((i,0,-1*i))
        if len(z) >=3:
            set_result.add((0,0,0))
        for i in range(len(n)-1):
            for j in range(i+1,len(n)):
                tar = -1*(n[i]+n[j])
                if tar in P:
                    set_result.add(tuple(sorted([n[i],n[j],tar])))
        for i in range(len(p)-1):
            for j in range(i+1,len(p)):
                tar = -1*(p[i] + p[j])
                if tar in N:
                    set_result.add(tuple(sorted([p[i], p[j], tar])))
        return set_result
        # Lap qua day so am truoc:
        
            

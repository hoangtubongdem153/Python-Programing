# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# ý tưởng đơn giản là cho chạy 2 vòng for.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        for i in range(n-1):
            # if nums[i] > target: 
            #     continue
            for j in range(i+1,n):
                # if nums[j] > target:
                #     continue
                sum_ = nums[i] + nums[j]
                if sum_ == target: 
                    return [i,j]
                if sum_ != target: 
                    continue
        return ()
    
print(Solution().twoSum([-3,4,3,90],0))


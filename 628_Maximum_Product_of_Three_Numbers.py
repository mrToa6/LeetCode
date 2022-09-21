class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        print(nums)
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
             
nums_list = [4,5,-1,-2,-3,-4]

a = Solution()
print(a.maximumProduct(nums_list))

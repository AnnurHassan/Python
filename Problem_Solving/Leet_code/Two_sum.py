class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        j = i + 1
        while (i <= len(nums)):
            if target == nums[i] + nums[j]:
                return [i, j]
            
            if j == len(nums) - 1:
                i += 1
                j = i + 1
            
            else:
                j += 1

# Alternative Solution
"""class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                return i,d[num]
            else:
                d[target-num] = i
        
        return None
"""

test_case = Solution()
print(test_case.twoSum([2, 7, 11, 15], 9))
print(test_case.twoSum([3, 2, 4], 6))
print(test_case.twoSum([3, 3], 6))




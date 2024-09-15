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

test_case = Solution()
print(test_case.twoSum([2, 7, 11, 15], 9))
print(test_case.twoSum([3, 2, 4], 6))
print(test_case.twoSum([3, 3], 6))




from collections import defaultdict
from typing import List

class Solution:
    # ignore case sensitivity and non character
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        left, right = 0, len(cleaned) - 1
        while left <= right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True
    
    # must be O(1) space, dict is not allowed!
    # numbers is sorted!
    # one solution is guaranteed!
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left <= right:
            current = numbers[left] + numbers[right]
            # combination too big, need to decrease result
            if current > target:
                right -= 1
            elif current < target:
                left += 1
            else:
                return [left + 1, right + 1]
    
    # return a list of triplet possibilities whose sum == 0
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # sort the array first
        # then loop through element, when one item is chosen, do twoSumII to solve and find combination
        for i, item in enumerate(nums):
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                three = nums[i] + nums[left] + nums[right]
                if three > 0:
                    right -= 1
                elif three < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
        return res
        
        
                

run = Solution()
# 1
print(run.isPalindrome("Was it a car or a cat I saw?"))
# 2
print(run.twoSum([1,2,3,4,5,6,7], 6))
# 3
print(run.threeSum([-1,0,1,2,-1,-4]))
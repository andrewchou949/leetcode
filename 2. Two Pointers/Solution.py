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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pass

run = Solution()
# 1
print(run.isPalindrome("Was it a car or a cat I saw?"))
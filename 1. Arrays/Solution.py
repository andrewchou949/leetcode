from collections import defaultdict

class Solution:
    
    # return true if any value exist more than once
    def hasDuplicate(self, nums: list[int]) -> bool:
        my_set = list(set(nums))
        if len(nums) == len(my_set):
            return False
        return True
    
    # return True if it's anagram
    def isAnagram(self, s: str, t: str) -> bool:
        # # return false immediately when len is no equivalent
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)
        
        # another solution
        if len(s) != len(t):
            return False
        my_s, my_t = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            my_s[s[i]] += 1
            my_t[t[i]] += 1
        for item in my_s.keys():
            if my_s[item] != my_t[item]:
                return False
        return True
        
    
    
run = Solution()
print(run.hasDuplicate([1, 2, 3]))
print(run.isAnagram("jar", "jam"))

from collections import defaultdict
from typing import List

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
    
    # return the index of item that make up the two sum  
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # keep track of current : missing pair to make the target
        my_dict = {}
        for i in range(len(nums)):
            missing = target - nums[i]
            if missing in my_dict:
                return [my_dict[missing], i]
            my_dict[nums[i]] = i
        return [] # default not found
    
    # group all anagram together
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # brute force approach
        # store ascii total to [] 
        # might be unreliable due to false positive situation.
        # my_dict = {}
        # for item in strs:
        #     current = sum(ord(x) for x in item)
        #     if current in my_dict:
        #         my_dict[current].append(item)
        #     else:
        #         my_dict[current] = [item]
        # result = []
        # for k, v in my_dict.items():
        #     result.append(v)
        # return result
        
        # another approach
        # sorting it first, less error prone!
        my_dict = {}
        for item in strs:
            # using tuple is better than string, since tuple is immutable
            current = tuple(sorted(item))
            if current in my_dict:
                my_dict[current].append(item)
            else:
                my_dict[current] = [item]
        result = list(sorted(my_dict.values(), key=lambda x: len(x)))
        return result
    
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # need to create an array to track the most frequently showned val
        # the index is the count
        # the value is the array that store the element
        dummy = [[] for i in range(len(nums) + 1)]
        my_dict = defaultdict(int) # store the count of each element
        for item in nums:
            my_dict[item] += 1
        # loop through each pair of k and v
        for n, v in my_dict.items():
            # v is the count, n is the item
            dummy[v].append(n)
        result = []
        # loop from the back for the biggest count and moving down
        for i in range(len(dummy) - 1, 0, -1):
            for n in dummy[i]:
                result.append(n)
                if len(result) == k:
                    return result
    
    # encode decode (facebook question)
    # for encoding, convert the given list into str with hashed output
    def encode(self, strs: List[str]) -> str:
        res = ""
        # picking len(item) + "#" as delimiter!
        for item in strs:
            res += str(len(item)) + "#" + item
        return res
    
    # for decoding, revert the string back to original list
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            # looping to find actual length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
    
    # return the product of array excluding self 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        postfix = [1 for _ in range(len(nums))]
        # going from front to back
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]
        # going from back to front
        postfix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i] * postfix[i + 1]
        output = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                output[i] = 1 * postfix[i + 1]
            elif i == len(nums) - 1:
                output[i] = 1 * prefix[i - 1]
            else:
                output[i] = prefix[i - 1] * postfix[i + 1]
        return output
        
            
    
run = Solution()
# 1
print(run.hasDuplicate([1, 2, 3]))
# 2
print(run.isAnagram("jar", "jam"))
# 3
print(run.twoSum([3, 4, 5, 6], 11))
# 4
print(run.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
# 5
print(run.topKFrequent([1, 2, 2, 3, 3, 3, 4], 2))
# 6
temp = run.encode(["I", "love", "neet", "code"])
print(temp) # to see encode result
print(run.decode(temp))
# 7
print(run.productExceptSelf([1,2,3,4]))
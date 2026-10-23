class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        nums = [0] * 26

        for i in range(len(s)):
            nums[ord(s[i]) - ord('a')] += 1
            nums[ord(t[i]) - ord('a')] -= 1

        return all(value == 0 for value in nums)
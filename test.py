class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        
        unique = set()
        ans = 0
        
        while right<len(s):
            while s[right] in unique:
                unique.remove(s[left])
                left+=1
            ans = max(ans, right-left+1) 
            unique.add(s[right])
            right+=1
        
        return ans
            

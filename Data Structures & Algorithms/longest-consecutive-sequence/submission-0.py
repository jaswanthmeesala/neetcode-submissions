class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s=set(nums)
        ans=0
        for i in s:
            if i-1 not in s:
                c=1
                while i+c in s:
                    c+=1
                ans=max(ans,c)
        return ans

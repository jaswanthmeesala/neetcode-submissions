class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def fun(ind,n,l,nums):
            if ind>=n:
                ans.append(list(l))
                return
            l.append(nums[ind])
            fun(ind+1,n,l,nums)
            l.pop()
            fun(ind+1,n,l,nums)

        fun(0,len(nums),[],nums)
        return ans
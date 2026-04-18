class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]
        def fun(ds, taken):
            if len(ds)==len(nums):
                ans.append(ds.copy())
                return
            

            for i in range(len(nums)):
                if(taken[i]==False):
                    taken[i]=True
                    ds.append(nums[i])
                    fun(ds,taken)
                    taken[i]=False
                    ds.pop()


        ds=[]
        n=len(nums)
        taken=[False]*n
        fun(ds,taken)
        return ans
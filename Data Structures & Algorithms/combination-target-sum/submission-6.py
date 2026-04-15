class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def fun(ind,n,l,nums,t):
            if ind==n:
                print(l,t)
                if t==0:
                    ans.append(l.copy())
                return
            else:
                if t>=nums[ind]:
                    l.append(nums[ind])
                    fun(ind,n,l,nums,t-nums[ind])
                    l.pop()
                fun(ind+1,n,l,nums,t)

        fun(0,len(nums),[],nums,target)
        return ans
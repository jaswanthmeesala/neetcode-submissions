class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()

        def fun(idx,ds):
            if idx==len(nums):
                ans.add(tuple(ds))
                return
            
            ds.append(nums[idx])
            fun(idx+1,ds)
            ds.pop()
            fun(idx+1,ds)
        
        fun(0,[])
        ans=[list(i) for i in ans]
        return ans
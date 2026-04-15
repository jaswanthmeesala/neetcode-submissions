class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()
        
        for i in range(len(nums)):
            t=-nums[i]
            j=i+1
            k=len(nums)-1

            while j<k:
                if nums[j]+nums[k]==t:
                    ans.add(tuple([nums[i],nums[j],nums[k]]))
                    k-=1
                elif nums[j]+nums[k]>t:
                    k-=1
                else:
                    j+=1
        ans=[list(i) for i in ans]
        return ans
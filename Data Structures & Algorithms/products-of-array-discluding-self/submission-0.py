class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[nums[0]]*len(nums)
        suf=[nums[len(nums)-1]]*len(nums)

        for i in range(1,len(nums)):
            pre[i]=pre[i-1]*nums[i]
            suf[len(nums)-i-1]=suf[len(nums)-i]*nums[len(nums)-i-1]
        ans=[]
        for i in range(len(nums)):
            if i==0:
                ans.append(suf[i+1])
            elif i==len(nums)-1:
                ans.append(pre[i-1])
            else:
                ans.append(pre[i-1]*suf[i+1])
        return ans



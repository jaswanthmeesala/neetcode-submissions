class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        pre=[height[0]]*len(height)
        suf=[height[n-1]]*len(height)
        for i in range(1,n):
            pre[i]=max(pre[i-1],height[i])
            suf[n-i-1]=max(suf[n-i],height[n-i-1])
        
        ans=0
        for i in range(1,n-1):
            if pre[i-1]<height[i] or suf[i+1]<height[i]:
                continue
            ans+=min(pre[i-1],suf[i+1])-height[i]
        return ans
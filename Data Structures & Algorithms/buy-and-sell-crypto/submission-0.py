class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        m=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<m:
                m=prices[i]
                continue
            else:
                ans=max(ans,prices[i]-m)
        return ans
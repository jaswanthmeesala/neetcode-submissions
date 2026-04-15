import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d={}
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
        l=[]
        for i,j in d.items():
            l.append([j,i])
        l.sort()
        ans=[]
        for i in range(k):
            ans.append(l.pop()[1])
        return ans
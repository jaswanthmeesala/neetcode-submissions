class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=set()
        def fun(ind,l,ds,t):
            if t<0:
                return
            if ind==len(l):
                if t==0:
                    ans.add(tuple(ds))
                return
            ds.append(l[ind])
            fun(ind+1,l,ds,t-l[ind])
            ds.pop()
            while ind+1<len(l):
                if l[ind]==l[ind+1]:
                    ind+=1
                else:
                    break
            fun(ind+1,l,ds,t)
        candidates.sort()
        fun(0,candidates,[],target)
        ans=[list(i) for i in ans]
        return ans
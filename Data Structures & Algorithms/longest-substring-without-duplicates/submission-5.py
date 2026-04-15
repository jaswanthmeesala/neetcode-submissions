class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        ans=0
        l=set()
        i=0
        j=0
        while j<n:
            if s[j] not in l:
                l.add(s[j])
            else:
                print(l)
                ans=max(ans,j-i)
                while True:
                    if s[i]==s[j]:
                        i+=1
                        break
                    else:
                        l.remove(s[i])
                        i+=1
            j+=1
        ans=max(ans,j-i)
        return ans
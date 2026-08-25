class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        n=len(s)
        freq1={}
        freq2={}
        for i in range(n):
            if s[i] not in freq1:
                freq1[s[i]] = 1
            else:
                freq1[s[i]]+=1
        for i in range(n):
            if t[i] not in freq2:
                freq2[t[i]] = 1
            else:
                freq2[t[i]]+=1
        return freq1==freq2
        
        
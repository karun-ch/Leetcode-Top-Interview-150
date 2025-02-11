class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn=[]
        m=[]
        for i in ransomNote :
            rn.append(i)
        for j in magazine:
            m.append(j)  
        l1=len(rn)
        while l1>0:
            for k in rn:
                l1-=1
                if k in m:
                    rn.pop(rn.index(k))
                    m.pop(m.index(k))
                elif k not in m:
                    return False
        return True
        
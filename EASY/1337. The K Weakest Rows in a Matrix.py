class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        import numpy as np
        li=[]
        for i in range(len(mat)):
            li.append(sum(mat[i]))
        res=sorted(range(len(li)), key=li.__getitem__)
        res=res[0:k]
        return(res)

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        if n==1:
            return 0
        q=[]
        for i in range(n):
            q.append(i)
        while len(q)>=2:
            cand=q.pop(0)
            other=q.pop(0)
            if knows(cand,other) is True or knows(other,cand) is False:
                q.insert(0,other)
            else:
                q.insert(0, cand)
            # now we only have one candidates
        cand= q.pop(0)
        for other in range(n):
            if other==cand:
                continue
            if  knows(other,cand) is False  or knows(cand,other) is True:
                return -1
        return cand

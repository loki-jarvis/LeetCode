class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = list(map(int, str(format(num, "b"))))
        return(res.count(1)*2+res.count(0)-1)

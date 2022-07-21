class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ma=0
        for i in range(len(accounts)):
            if(ma<sum(accounts[i])):
                ma=sum(accounts[i])
        return(ma)

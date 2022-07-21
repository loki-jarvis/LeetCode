class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans1=[]
        ans2=[]
        if(n==1):
            return([nums[0]*nums[0]])
        ind=0
        for i in range(n):
            ans1.append(nums[i]*nums[i])
            if(ans1[i]<ans1[i-1]):
                ind=i
        le=ind-1
        ri=ind
        for k in range(n-1):
            if(ans1[le]>ans1[ri]):
                ans2.append(ans1[ri])
                ri=ri+1
            elif(ans1[le]<ans1[ri]):
                ans2.append(ans1[le])
                le=le-1
            else:
                ans2.append(ans1[ri])
                ans2.append(ans1[le])
                ri=ri+1
                le=le-1
                i=i+1
            if(le==-1):
                for k in range(ri,n):
                    ans2.append(ans1[k])
                break
            if(ri==n):
                for k in range(le,-1,-1):
                    ans2.append(ans1[k])
                break
        return(ans2)

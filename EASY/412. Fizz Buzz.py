class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lis=[]
        for i in range(1,n+1):
            lis.append(str(i))
        for i in range(2,n,3):
            lis[i]="Fizz"
        for i in range(4,n,5):
            lis[i]="Buzz"
        for i in range(14,n,15):
            lis[i]="FizzBuzz"
        return(lis)

#copy of my leet code solution.
class Solution:
    def mySqrt(self, x: int) -> int:
        #lets create a possible range and search like binary tree.
        l=0
        r=x
        if x==0 or x==1:
            return x
        mid=(l+r)//2
        while(True):
            t=mid
            if mid*mid>x:
                r=mid+1
            else:
                l=mid
            mid=(l+r)//2
            if t==mid:
                break
        return l
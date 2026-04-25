class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        la = [1]*n
        ra = [1]*n
        output = [1]*n
        for i in range(1,n):
            la[i] = la[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            ra[i] = ra[i+1]*nums[i+1]
        for i in range(n):
            output[i] = la[i]*ra[i]
        return output
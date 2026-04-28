class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        i = 0
        j = n-1
        maxi = 0
        while(i<j):
            nums = min(height[i],height[j])*(j-i)
            maxi = max(nums,maxi)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return (maxi)
                
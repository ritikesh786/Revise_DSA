class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:

        

        n = len(nums)
        if n < 2:
            return nums
        lst = [nums[0]]

        for i in range(1,n-1):
            if max(nums[:i])<nums[i] or max(nums[i+1:])<nums[i]:
                lst.append(nums[i])
        lst.append(nums[-1])
        return lst


        
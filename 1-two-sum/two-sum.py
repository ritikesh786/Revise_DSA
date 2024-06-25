class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}

        for i , num in enumerate(nums):
            goal = target - num

            if goal in dict:
                return [dict[goal],i]
            dict[num] = i

        return []
        
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        seen = set()
        duplicate = set()

        for item in nums:
            if item in seen:
                duplicate.add(item)
            else:
                seen.add(item)

        ans = list(duplicate)
        return ans

        
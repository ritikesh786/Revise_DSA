class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_arr = sorted(heights)
        cnt = 0
        num = len(heights)
        for i in range(num):
            if heights[i] != sorted_arr[i]:
                cnt += 1
        return cnt
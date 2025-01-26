class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        l = 0
        curr_max = 0
        curr_sum = 0

        bucket = set()

        n = len(nums)

        if len(set(nums))<k:
            return 0

        for r in range(n):

            while nums[r] in bucket:
                bucket.remove(nums[l])

                curr_sum -= nums[l]
                l+=1

            bucket.add(nums[r])
            curr_sum += nums[r]


            if len(bucket) == k:
                curr_max = max(curr_sum,curr_max)

                bucket.remove(nums[l])
                curr_sum -= nums[l]
                l+=1
        return curr_max
        
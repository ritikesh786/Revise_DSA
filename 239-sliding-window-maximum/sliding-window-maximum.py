from collections import deque
class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        if not arr or k <= 0:
            return []
        
        n = len(arr)
        if k > n:
            return []

        max_values = []
        deq = deque()  # Will store indices of array elements

        for i in range(n):
            # Remove elements not within the window
            if deq and deq[0] < i - k + 1:
                deq.popleft()

            # Remove elements from the deque that are smaller than the current element
            while deq and arr[deq[-1]] < arr[i]:
                deq.pop()
            
            # Add current element's index at the end of the deque
            deq.append(i)

            # The front of the deque is the index of the largest element for the current window
            if i >= k - 1:
                max_values.append(arr[deq[0]])

        return max_values





        
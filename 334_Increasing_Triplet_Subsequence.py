class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:  # Early exit if the list is too short
            return False
        
        # Calculate the left min array
        leftmin = [0] * n
        minv = float('inf')
        for i in range(n):
            minv = min(minv, nums[i])
            leftmin[i] = minv
        
        # Calculate the right max array
        rightmax = [0] * n
        maxv = float('-inf')
        for i in range(n - 1, -1, -1):  # Corrected the range here
            maxv = max(maxv, nums[i])
            rightmax[i] = maxv

        # Check the condition
        for i in range(n):
            if leftmin[i] < nums[i] < rightmax[i]:  # Fixed the comparison
                return True

        return False

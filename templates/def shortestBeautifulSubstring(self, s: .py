class Solution:
    def findIndices(self, nums, indexDifference: int, valueDifference: int):
        min_indices = []
        max_indices = []

        # Iterate through nums and maintain lists of min and max indices
        for i, num in enumerate(nums):
            while min_indices and nums[min_indices[-1]] >= num:
                min_indices.pop()
            while max_indices and nums[max_indices[-1]] <= num:
                max_indices.pop()
            min_indices.append(i)
            max_indices.append(i)

            # Check for valid pairs
            if min_indices[0] <= i - indexDifference:
                min_indices.pop(0)
            if max_indices[0] <= i - indexDifference:
                max_indices.pop(0)

            if min_indices and max_indices and nums[max_indices[0]] - nums[min_indices[0]] >= valueDifference:
                return [min_indices[0], max_indices[0]]

        return [-1, -1]


solution = Solution()
print(solution.findIndices([5, 1, 4, 1], 2, 4))  # Expected output: [0, 3]
# Expected output: [0, 0] or [0, 1] or [1, 0] or [1, 1]
print(solution.findIndices([2, 1], 0, 0))
print(solution.findIndices([1, 2, 3], 2, 4))   # Expected output: [-1, -1]

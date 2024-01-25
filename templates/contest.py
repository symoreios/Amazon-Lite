import heapq


def smallestArray(nums, limit):
    n = len(nums)
    arr = []

    for i in range(n):
        heapq.heappush(arr, (nums[i], i))

    for i in range(n):
        tmp = []

        while arr:
            val, idx = heapq.heappop(arr)

            if idx <= i:
                continue

            if abs(nums[i] - val) <= limit and nums[i] > val:
                nums[i], nums[idx] = nums[idx], nums[i]
                break
            else:
                tmp.append((val, idx))

        for item in tmp:
            heapq.heappush(arr, item)

    return nums


# Provided test cases
test_cases = [
    ([1, 5, 3, 9, 8], 2),
    ([1, 7, 6, 18, 2, 1], 3),
    ([1, 7, 28, 19, 10], 3)
]

# Running the test cases
outputs = [smallestArray(nums, limit) for nums, limit in test_cases]
print(outputs)

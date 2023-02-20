from functools import reduce


def zero_sum_subarray(nums: list) -> bool:
    if 0 in nums:
        return True

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums) + 1):
            if reduce(lambda a, b: a + b, nums[i:j]) == 0:
                return True
    return False

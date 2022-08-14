from typing import List


def contains_duplicate_impl_1(nums: List[int]) -> bool:
    if not nums or len(nums) == 1:
        return False

    nums.sort()
    for i, n in enumerate(nums[1:]):
        if nums[i] == n:
            return True
    return False


def contains_duplicate_impl_2(nums: List[int]) -> bool:
    if not nums or len(nums) == 1:
        return False

    # return len(nums) != len(set(nums))  # too costly
    n_set = set()
    for n in nums:
        if n in n_set:
            return True
        else:
            n_set.add(n)
    return False


if __name__ == '__main__':
    res = contains_duplicate_impl_2([1, 2, 3, 1])
    print(res)
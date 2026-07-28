"""
AI-LeetCode-Mentor
Example: Binary Search Problem
"""


def binary_search(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


if __name__ == "__main__":

    nums = [1, 3, 5, 7, 9, 11]
    target = 7

    result = binary_search(nums, target)

    print("Array:", nums)
    print("Target:", target)
    print("Index:", result)

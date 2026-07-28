"""
AI-LeetCode-Mentor
Example: Two Sum Problem

This example demonstrates how the AI mentor
can explain a common LeetCode problem.
"""


def two_sum(nums, target):
    """
    Finds two numbers whose sum equals the target.

    Approach:
    - Use a hash map to store previously seen numbers.
    - Check if the required complement exists.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    seen = {}

    for index, number in enumerate(nums):

        complement = target - number

        if complement in seen:
            return [seen[complement], index]

        seen[number] = index

    return []


if __name__ == "__main__":

    nums = [2, 7, 11, 15]
    target = 9

    result = two_sum(nums, target)

    print("Input:", nums)
    print("Target:", target)
    print("Answer:", result)

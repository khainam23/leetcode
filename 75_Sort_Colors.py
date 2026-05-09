'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

 

Constraints:

    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.

'''
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums: List[int], l: int, r: int) -> None:
        if l >= r:
            return

        mid = (l + r) // 2

        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)

        self.mergeParts(nums, l, mid, r)

    def mergeParts(self, nums: List[int], l: int, mid: int, r: int) -> None:
        temp = []

        i, j = l, mid + 1

        while i <= mid and j <= r:
            if nums[i] < nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= r:
            temp.append(nums[j])
            j += 1

        for idx in range(len(temp)):
            nums[l + idx] = temp[idx]

from TestCase import TestCase  

def wrapper(matrix):
    Solution().sortColors(matrix)
    return matrix

data = [
    ([[2,0,2,1,1,0]], [[0,0,1,1,2,2]]),
    ([[2,0,1]], [[0,1,2]])
]

testcasse = TestCase()
testcasse.test_case([
    (lambda m=inp: (Solution().sortColors(m), m)[1], exp) 
    for inp, exp in data
])
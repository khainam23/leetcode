'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0

 

Constraints:

    0 <= num <= 231 - 1

'''
class Solution:
    def addDigits(self, num: int) -> int:
        def sum(number: int) -> int:
            if number < 10:
                return number

            left_number = int(number // 10)
            right_number = int(number % 10)
            return sum(left_number + right_number)

        return sum(num)
            
'''
Super best solution
class Solution(object): 
    def addDigits(self, num): 
        if num == 0: return 0
        if num % 9 == 0: return 9
        return num % 9
'''
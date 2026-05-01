from typing import List

# v2 - Optimize mem but time is worse than v1
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         len_row = len(matrix)
#         len_col = len(matrix[0])
        
#         first_row_zero = False
#         first_col_zero = False

#         # Bước 1: Kiểm tra hàng đầu và cột đầu
#         for c in range(len_col):
#             if matrix[0][c] == 0:
#                 first_row_zero = True
#                 break
        
#         for r in range(len_row):
#             if matrix[r][0] == 0:
#                 first_col_zero = True
#                 break

#         # Bước 2: Dùng hàng/cột đầu làm nơi đánh dấu (marker) cho phần còn lại
#         for r in range(1, len_row):
#             for c in range(1, len_col):
#                 if matrix[r][c] == 0:
#                     matrix[r][0] = 0
#                     matrix[0][c] = 0

#         # Bước 3: Cập nhật ma trận dựa trên các marker
#         for r in range(1, len_row):
#             for c in range(1, len_col):
#                 if matrix[r][0] == 0 or matrix[0][c] == 0:
#                     matrix[r][c] = 0
        
#         # Bước 4: Xử lý nốt hàng đầu và cột đầu
#         if first_row_zero:
#             for c in range(len_col):
#                 matrix[0][c] = 0
        
#         if first_col_zero:
#             for r in range(len_row):
#                 matrix[r][0] = 0

# v1
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_row = len(matrix)
        len_col = len(matrix[0])
        
        # Đánh dấu các hàng và cột cần xóa
        rows_to_zero = set()
        cols_to_zero = set()

        for r in range(len_row):
            for c in range(len_col):
                if matrix[r][c] == 0:
                    rows_to_zero.add(r)
                    cols_to_zero.add(c)

        # Cập nhật mảng tại chỗ
        for r in rows_to_zero:
            for c in range(len_col):
                matrix[r][c] = 0
        
        for c in cols_to_zero:
            for r in range(len_row):
                matrix[r][c] = 0

from TestCase import TestCase  

def wrapper(matrix):
    Solution().setZeroes(matrix)
    return matrix

data = [
    ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]),
    ([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]])
]

testcasse = TestCase()
testcasse.test_case([
    (lambda m=inp: (Solution().setZeroes(m), m)[1], exp) 
    for inp, exp in data
])

'''
STT   | Status     | Time (ms)    | Mem (KB)     | Actual               | Expected            
----------------------------------------------------------------------------------------------
1     | PASS       | 0.0152       | 0.88         | [[1, 0, 1], [0, 0... | [[1, 0, 1], [0, 0...
2     | PASS       | 0.0127       | 0.89         | [[0, 0, 0, 0], [0... | [[0, 0, 0, 0], [0...
''' 
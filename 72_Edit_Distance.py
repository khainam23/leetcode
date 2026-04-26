class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Initialize the DP table
        # dp[i][j] represents the distance between word1[:i] and word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases: transforming a string to an empty string
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
            
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Characters match, no new operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Choose the minimum of:
                    # 1. dp[i-1][j] + 1 (Deletion)
                    # 2. dp[i][j-1] + 1 (Insertion)
                    # 3. dp[i-1][j-1] + 1 (Substitution)
                    dp[i][j] = 1 + min(dp[i - 1][j],      # Delete
                                       dp[i][j - 1],      # Insert
                                       dp[i - 1][j - 1])  # Replace
                                       
        return dp[m][n]
    
from TestCase import TestCase
test_case = TestCase()
test_case.test_case([
    [Solution().minDistance("horse", "ros"), 3],
    [Solution().minDistance("intention", "execution"), 5],
    [Solution().minDistance("a", "aa"), 1],
    [Solution().minDistance("a", "ab"), 1],
    [Solution().minDistance("zoologicoarchaeologist", "zoogeologist"), 10],
])

'''
STT   | Status     | Actual                    | Expected                 
--------------------------------------------------------------------------
1     | PASS       | 3                         | 3                        
2     | PASS       | 5                         | 5                        
3     | PASS       | 1                         | 1                        
4     | PASS       | 1                         | 1                        
5     | PASS       | 10                        | 10  
'''
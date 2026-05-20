# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def recursive(root: Optional[TreeNode], content: str):
            if root.left == None and root.right == None:
                result.append(content + str(root.val))
                return

            if root.left != None:
                recursive(root.left, content + str(root.val) + "->")

            if root.right != None:
                recursive(root.right, content + str(root.val) + "->")

        recursive(root, "")
        return result
    
from TestCase import TestCase
test_case = TestCase()
test_case.test_case([
    [Solution().binaryTreePaths(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))), ["1->2->5", "1->3"]],
    [Solution().binaryTreePaths(TreeNode(1)), ["1"]],
])
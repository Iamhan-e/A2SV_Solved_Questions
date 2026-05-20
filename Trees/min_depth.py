# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(root):
            if not root:
                return 0
            
            if not root.left:
                return 1+ depth(root.right)
            if not root.right:
                return 1+ depth(root.left)

            return min(1+depth(root.left), 1+depth(root.right))

        return depth(root)

#https://leetcode.com/problems/minimum-depth-of-binary-tree/
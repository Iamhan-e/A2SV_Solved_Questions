# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        moves= 0
        def dfs(root):
            nonlocal moves
            if root is None:
                return 0

            left_balance= dfs(root.left)
            right_balance= dfs(root.right)
            moves+= abs(left_balance) + abs(right_balance)

            return root.val - 1 + left_balance + right_balance
        

        dfs(root)
        return moves
#https://leetcode.com/problems/distribute-coins-in-binary-tree/description/
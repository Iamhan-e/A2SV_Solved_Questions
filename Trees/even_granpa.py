# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def find_granparents(root, parent, granpa):

            res=0
            if not root :
                return 0
            
            if granpa and granpa.val%2 == 0:
                res+= root.val
            res+= find_granparents(root.left, root, parent)
            res+= find_granparents(root.right, root, parent)
            
            return res
        return find_granparents(root, None, None)


#https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
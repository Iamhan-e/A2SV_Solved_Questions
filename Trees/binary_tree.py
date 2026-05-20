# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
       
        in_map= {}
        pre_que= collections.deque(preorder)

        for i in range(len(inorder)):
            in_map[inorder[i]]= i

        def build(start, end):
            if start > end: return None
        
            root= TreeNode(pre_que.popleft())
            indx= in_map[root.val]

            root.left= build(start, indx-1)
            root.right= build(indx+1, end)

            return root
        
        return build(0, len(preorder)-1)

#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/


        


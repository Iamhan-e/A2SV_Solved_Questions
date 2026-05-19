# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        prefix_sum= {0:1}

        def dfs(root, curr_sum):
            cnt=0
            if root is None:
                return 0
            curr_sum+= root.val
            
            if curr_sum - targetSum in prefix_sum:
                cnt += prefix_sum.get(curr_sum - targetSum, 0)

            prefix_sum[curr_sum]= prefix_sum.get(curr_sum,0) +1

            l_path= dfs(root.left, curr_sum)
            r_path= dfs(root.right, curr_sum)
            prefix_sum[curr_sum]-=1
            cnt= cnt+ l_path + r_path

            return cnt


        return dfs(root, 0)
#https://leetcode.com/problems/path-sum-iii/


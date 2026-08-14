# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            if not root:
                return 0
            leftmaxx = max(dfs(root.left),0)
            rightmaxx = max(dfs(root.right),0)
            res[0] = max(res[0], leftmaxx + root.val + rightmaxx)
            return root.val + max(leftmaxx,rightmaxx)
        dfs(root)
        return res[0]
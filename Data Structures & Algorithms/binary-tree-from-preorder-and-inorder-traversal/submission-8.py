# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
         pos = {v: i for i, v in enumerate(inorder)}

         def build(pl, pr, il, ir):
            if pl > pr:
                return None

            root = TreeNode(preorder[pl])
            mid = pos[preorder[pl]]

            left = mid - il

            root.left = build(pl + 1, pl + left, il, mid - 1)
            root.right = build(pl + left + 1, pr, mid + 1, ir)

            return root

         return build(0, len(preorder) - 1, 0, len(inorder) - 1)
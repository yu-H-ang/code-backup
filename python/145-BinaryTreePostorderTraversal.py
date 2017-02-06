# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        out = []
        while stack:
            p = stack.pop()
            if p:
                out.insert(0, p.val)
                stack.append(p.left)
                stack.append(p.right)
        
        return out

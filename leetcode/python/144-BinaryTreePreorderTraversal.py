# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        if root == None:
            return []
        stack = []
        p = root
        out = []
        while stack or p != None:
            while p != None:
                out.append(p.val)
                if p.right != None:
                    stack.append(p.right)
                p = p.left
            if stack:
                p = stack.pop()
        '''
        stack = [root]
        out = []
        while stack:
            p = stack.pop()
            if p:
                out.append(p.val)
                stack.append(p.right)
                stack.append(p.left)
        
        return out

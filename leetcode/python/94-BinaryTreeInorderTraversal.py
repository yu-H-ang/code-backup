# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None:
            return []
        
        stack = []
        p = root
        out = []
        
        while len(stack) > 0 or p != None:
            # if p is not None, go to the left end
            while p != None:
                stack.append(p)
                p = p.left
            # set p to the frist element in stack,
            # print, then go to the right child
            if stack:
                p = stack.pop()
                out.append(p.val)
                p = p.right
        
        return out

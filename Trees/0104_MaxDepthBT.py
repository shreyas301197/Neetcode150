class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root :
            return 0
        # ans from left
        left =  self.maxDepth(root.left)
        # ans from right
        right = self.maxDepth(root.right)
        return 1 + max(left,right)
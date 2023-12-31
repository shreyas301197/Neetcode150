class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root :
            return None
        # search left
        if p.val < root.val and q.val < root.val :
            return self.lowestCommonAncestor( root.left, p, q)
        # search right
        if p.val > root.val and q.val > root.val :
            return self.lowestCommonAncestor( root.right, p, q)
        else: return root
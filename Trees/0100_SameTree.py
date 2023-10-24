class Solution(object):
    def isSameTree(self, node1, node2):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (node2 != None) &( node1 == None):
            return False
        if (node2 == None) & (node1 != None):
            return False
        if (node2 == None) & (node1 == None):
            return True
        if (node2.val != node1.val) :
            return False
        left = self.isSameTree( node1.left, node2.left)
        right = self.isSameTree( node1.right, node2.right)
        return left & right
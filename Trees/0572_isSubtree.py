# recursive solution : TC - O(MN)
class Solution(object):
    def sameTree(self,node1,node2) :
        # BC - two null roots can be identical
        if (not node1) and (not node2) :
            return True
        
        if node1 and node2 and node1.val == node2.val :
            return self.sameTree(node1.left,node2.left) & self.sameTree(node1.right,node2.right)
        return False
    def isSubtree(self, root, subroot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        # BC - null subtree is always a subtree of any tree
        if not subroot :
            return True
        # BC - if subtree is not null, and main tree is null -> return False
        if ( not root)  :
            return False
        # check if they are same trees
        if self.sameTree(root,subroot):
            return True
        # now check in the left and right children of the main tree to find the subtree
        if self.isSubtree(root.left,subroot) | self.isSubtree(root.right,subroot):
            return True
        return False


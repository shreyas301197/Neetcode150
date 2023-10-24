# inorder of a BST is sorted in increasing order
import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ans = []
        def inorder(root,ans) :
            if not root :
                return
            inorder(root.left,ans)
            ans.append(root.val)
            inorder(root.right,ans)
        inorder(root,ans)
        for i in range(len(ans)-1) :
            if ans[i] >= ans[i+1] :
                return False
        return True

# DFS - Recursive - Valid range
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def solve(root) :
            if not root : # flag,min,max
                return True,sys.maxint,-sys.maxint
            # call for left
            left = solve(root.left)
            # call for right
            right = solve(root.right)
            lb,rb = left[0],right[0]
            left_max,right_max = left[2],right[2]
            left_min,right_min = left[1],right[1]
            cond1 = left_max < root.val
            cond2 = right_min > root.val
            if lb & rb & cond1 & cond2 :
                return True,min(root.val,left_min),max(root.val,right_max)
            return False,min(root.val,left_min),max(root.val,right_max)
            
        return solve(root)[0]

# Recursive - Valid range
class Solution(object):
    def solve(self,root,min,max) :
        if root == None :
            return True
        if (root.val > min) & (root.val < max) :
            left = self.solve(root.left,min,root.val)
            right = self.solve(root.right,root.val,max)
            return left & right
        return False
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.solve(root,-sys.maxint,sys.maxint)
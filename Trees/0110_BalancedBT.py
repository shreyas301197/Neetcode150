class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if not root :
                return True,0
            left = check(root.left)
            right = check(root.right)
            lb,rb = left[0],right[0]
            lh,rh = left[1],right[1]
            cond = abs(lh-rh) <= 1
            if lb & rb &  cond :
                return True,max(lh,rh)+1
            return False,max(lh,rh)+1
        return check(root)[0]
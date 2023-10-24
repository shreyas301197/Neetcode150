# You understand that DFS is the way to go here - You also know that we need to somehow propagate the current max to the lower nodes - the way to go about this is PREORDER traversal where you first process the current node (update max_till_now) and then go left/right
import sys
class Solution(object):
    def preorder(self,root,max,ans) :
        if not root :
            return
        # process N
        if max <= root.val :
            max = root.val
            ans[0] += 1
        # go L
        self.preorder(root.left, max, ans)
        # go R
        self.preorder(root.right, max, ans)

        
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0]
        self.preorder(root,-sys.maxint,ans)
        return ans[0]
    

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: # type: ignore  # noqa: F821
        if not root:
            return 0
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))        
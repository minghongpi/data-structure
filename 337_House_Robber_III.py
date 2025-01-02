class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # return self.__dfs_rec(root)
        dp = {}
        return self.__dfs_topdown(root, dp)

    def __dfs_rec(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        m1 = self.__dfs_rec(root.left) + self.__dfs_rec(root.right)

        m2 = root.val;
        if root.left:
            m2 = m2 + self.__dfs_rec(root.left.left) + self.__dfs_rec(root.left.right)
        if root.right:
            m2 = m2 + self.__dfs_rec(root.right.left) + self.__dfs_rec(root.right.right)
        
        return max(m1, m2)

    
    def __dfs_topdown(self, root: Optional[TreeNode], dp : dict ) -> int:
        if root is None:
            return 0
        
        if root in dp:
            return dp[root]

        m1 = self.__dfs_topdown(root.left, dp) + self.__dfs_topdown(root.right, dp)

        m2 = root.val;
        if root.left:
            m2 = m2 + self.__dfs_topdown(root.left.left, dp) + self.__dfs_topdown(root.left.right, dp)
        if root.right:
            m2 = m2 + self.__dfs_topdown(root.right.left, dp) + self.__dfs_topdown(root.right.right, dp)
        
        dp[root] = max(m1, m2)
        return dp[root]

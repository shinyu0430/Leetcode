def DFS(self, node, count):
    if not node:
        return 0
    self.DFS(node.left, count+1)
    self.DFS(node.right, count+1)

    if self.max_c < count:
        self.max_c = count
    return self.max_c


def maxDepth(self, root: Optional[TreeNode]) -> int:
    return self.DFS(root, 1)

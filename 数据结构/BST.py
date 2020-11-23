# 二叉树节点的定义
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 二叉查找树的搜索
def searchBST(self, root: TreeNode, x: int) -> TreeNode:
    # 如果树为空，则肯定不存在值为x的节点，返回空
    if root is None:
        return None
    p = root
    # 当p不空，说明没有查找结束
    while p is not None:
        # 如果p的值等于x，则p就是我们要找的节点，返回p
        if p.val == x:
            return p
        # 节点p的值大于x，说明x在p的左子树
        if p.val > x:
            p = p.left
        # 节点p的值小于x，说明x在p右左子树
        elif p.val < x:
            p = p.right
    # 若一直查找到空节点，说明整个树中没有值为x的节点，返回空
    return None


# 二叉查找树插入，将x插入根节点为root的二叉查找树
def insertIntoBST(self, root: TreeNode, x: int) -> TreeNode:
    # 树为空，则直接插入到根节点
    if root is None:
        root = TreeNode(x)
        return root
    # parent指向当前节点的父节点
    p = root
    parent = p
    while p is not None:
        if p.val == x:
            print("插入失败，二叉搜索树中已经存在值为x的节点")
            return None
        if p.val > x:
            parent = p
            p = p.left
        elif p.val < x:
            parent = p
            p = p.right
    # 循环完成，parent指向p的父节点，值将被插入到parent的左孩子或者右孩子
    if parent.val > x:
        parent.left = TreeNode(x)
    else:
        parent.right = TreeNode(x)
    return root
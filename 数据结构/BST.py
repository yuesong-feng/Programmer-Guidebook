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

# 二叉树删除节点
def deleteNode(self, root: TreeNode, key: int) ->TreeNode:
    # 首先要找到值为key的节点p，用parent记录p的父节点
    p = root
    parent = p
    while p is not None:
        if p.val == key:
            break
        elif p.val > key:
            parent = p
            p = p.left
        elif p.val < key:
            parent = p
            p = p.right
    if p is None:
        print("树中没有值为key的节点，无法删除！")
        return root
    # 到这里，p是值为key的节点，parent是p的父节点
    # 1. 如果p是叶子节点
    if p.left is None and p.right is None:
        # 判断p是parent的左孩子还是右孩子
        if parent.left is p:
            parent.left = None
        elif parent.right is p:
            parent.right = None
        # p是根节点
        elif parent is p:
            return None
        return root
    # 2.1 如果p只有左孩子
    elif p.left is not None and p.right is None:
        if parent.left is p:
            parent.left = p.left
        elif parent.right is p:
            parent.right = p.left
        elif parent is p:
            return p.left
        return root
    # 2.2 如果p只有右孩子
    elif p.left is None and p.right is not None:
        if parent.left is p:
            parent.left = p.right
        elif parent.right is p:
            parent.right = p.right
        elif parent is p:
            return p.right
        return root
    # 3. 如果p有两个孩子
    elif p.left is not None and p.right is not None:
        # 3.1. 将p的直接后继node的值拷贝到p
        # 3.1.1 先找到p的直接后继node，node_parent是nod的父节点
        node_parent = p
        node = p.right
        while node.left is not None:
            node_parent = node
            node = node.left
        # 此时node是待删除节点p的直接后继,node_parentnode的父节点。
        # 3.1.2 将node的值拷贝到p
        p.val = node.val
        # 3.2. 删除p的直接后继node。由于node是p的右子树的左节点，那么node肯定没有左孩子，可能有右孩子。
        # 3.2.1 如果node没有右孩子
        if node.right is None:
            if node_parent.left is node:
                node_parent.left = None
            elif node_parent.right is node:
                node_parent.right = None
        # 3.2.2 如果node有右孩子
        elif node.right is not None:
            if node_parent.left is node:
                node_parent.left = node.right
            elif node_parent.right is node:
                node_parent.right = node.right
        return root

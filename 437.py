# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    # 树类
    def __init__(self, root=None):
        self.root = root

    def add(self, val):
        node = TreeNode(val)
        if self.root is None:
            self.root = node
        else:
            queue = [self.root]
            while queue:
                cur_node = queue.pop(0)
                if cur_node.left is None:
                    cur_node.left = node
                    return
                elif cur_node.right is None:
                    cur_node.right = node
                    return
                else:
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)

    def BFS(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def find_path(root, targetsum):
            path_num = 0
            if root is None or root.val is None:
                return 0
            if root.val == targetsum:
                path_num += 1

            path_num += find_path(root.left, targetsum - root.val)
            path_num += find_path(root.right, targetsum - root.val)
            return path_num

        if root is None:
            return 0
        else:
            path_num = find_path(root, targetSum)
            path_num += self.pathSum(root.left, targetSum)
            path_num += self.pathSum(root.right, targetSum)

        return path_num


if __name__ == '__main__':
    # 主函数
    inputs = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    tar = 8
    tree = Tree()  # 新建一个树对象
    for val in inputs:
        tree.add(val)  # 逐个加入树的节点

    result = Solution().pathSum(root=tree.root, targetSum=tar)
    print(result)



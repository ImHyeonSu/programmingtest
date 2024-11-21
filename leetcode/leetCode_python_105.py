from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def setTree(self, nums: list[int]):
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.setTree(nums[:mid])
        root.right = self.setTree(nums[mid + 1 :])
        return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root

    def print_tree(self, node, level=0):
        if node:
            print("  " * level + str(node.val))
            self.print_tree(node.left, level + 1)
            self.print_tree(node.right, level + 1)


a = Solution()
result = a.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
a.print_tree(result)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])
        return root

    def print_tree(self, node, level=0):
        if node:
            print("  " * level + str(node.val))
            self.print_tree(node.left, level + 1)
            self.print_tree(node.right, level + 1)


a = Solution()
result = a.sortedArrayToBST([-10, -3, 0, 5, 9])
a.print_tree(result)

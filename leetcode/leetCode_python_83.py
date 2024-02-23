from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1_head = ListNode()
        current = list1_head
        for val in head:
            current.next = ListNode(val)
            current = current.next
            print(current.val, end=" -> ")
            

a = Solution()
result = a.deleteDuplicates([1,1,2])

# while result:
#     print(result.val, end=" -> ")
#     result = result.next
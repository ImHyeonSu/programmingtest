from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next


# tail.next = l1 또는 tail.next = l2에서 tail.next에 대입하는 것은 현재 tail이 가리키는 노드의 next를 새로운 노드로 설정하는 것을 의미합니다. 이로써 현재까지 병합된 리스트의 끝에 새로운 노드가 추가된다고 이해하면 됩니다.

# 각 루프에서 tail.next에 값을 대입함으로써 새로운 노드가 현재까지 병합된 리스트의 끝에 추가되는 것이며, 이때 tail은 이 새로운 노드를 가리키게 됩니다. 이 과정을 반복하면서 두 리스트를 병합하게 되고, 최종적으로 dummy.next가 전체 병합된 리스트의 시작을 가리키게 됩니다.

# 다음은 각 루프에서 tail.next에 대입되는 노드들이 현재까지 어떻게 변하는지를 나타낸 예시입니다:

# 첫 번째 루프: tail.next = l1 → [1]이 추가됨 → tail은 [1]을 가리킴
# 두 번째 루프: tail.next = l2 → [1, 1]이 추가됨 → tail은 [1, 1]을 가리킴
# 세 번째 루프: tail.next = l1 → [1, 1, 2]가 추가됨 → tail은 [1, 1, 2]를 가리킴
# 네 번째 루프: tail.next = l2 → [1, 1, 2, 3]이 추가됨 → tail은 [1, 1, 2, 3]을 가리킴
# 다섯 번째 루프: tail.next = l1 → [1, 1, 2, 3, 4]가 추가됨 → tail은 [1, 1, 2, 3, 4]를 가리킴
# 여섯 번째 루프: tail.next = l2 → [1, 1, 2, 3, 4, 4]가 추가됨 → tail은 [1, 1, 2, 3, 4, 4]를 가리킴
# 이러한 방식으로 tail은 항상 현재까지 병합된 리스트의 마지막 노드를 가리키게 되고, tail.next에 대입되는 노드들이 현재까지 병합된 리스트에 추가되어 전체 리스트가 생성됩니다.

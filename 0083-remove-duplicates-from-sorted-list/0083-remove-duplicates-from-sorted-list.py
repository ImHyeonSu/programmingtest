# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode list = head;

        while(list != null){
            if(list.next == null){
                break;
            }
            if(list.val == list.next.val){
                list.next = list.next.next
            }else{
                list = list.next
            }
            
        }
        return head;
    }
}
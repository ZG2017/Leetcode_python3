# mine:
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        sorted_list = []
        output = ListNode(0)
        tmp = output
        for i in range(len(lists)):
            if lists[i] != None:
                sorted_list.append(lists[i].val)
        while True:
            if sorted_list == []:
                return output.next
            sorted_list = sorted(sorted_list)
            mini = sorted_list.pop(0)
            tmp.next = ListNode(mini)
            tmp = tmp.next
            for i in range(len(lists)):
                if lists[i] == None:
                    continue
                elif lists[i].val == mini:
                    lists[i] = lists[i].next
                    if lists[i] != None:
                        sorted_list.append(lists[i].val)
                    break


# update:
class Solution:
    def mergeKLists(self, lists):
        from operator import attrgetter
        
        sorted_list = []
        for lst in lists:
            while lst is not None:
                sorted_list.append(lst)
                lst = lst.next
        sorted_list = sorted(sorted_list, key = attrgetter('val'))
        dummy  = curr = ListNode(0)
        for node in sorted_list:
            curr.next = curr = node
        return dummy.next



# updated again:
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        sorted_list = []
        output = tmp = ListNode(0)
        tmp = output
        for i in range(len(lists)):
            while lists[i] != None:
                sorted_list.append(lists[i])
                lists[i] = lists[i].next
        sorted_list = sorted(sorted_list, key = lambda x:x.val)
        for i in range(len(sorted_list)):
            tmp.next = ListNode(sorted_list[i].val)
            tmp = tmp.next
        return output.next



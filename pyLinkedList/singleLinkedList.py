class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    # Traversing the Single Linked List
    # Time: O(n) 
    # Space: O(1)
    def listTraverse(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next


    # Count the length of Single Linked List
    # Time: O(n) 
    # Space: O(1)
    def listLength(self):
        current = self.head
        count = 0
    
        while current is not None:
            count += 1
            current = current.next

        return count         


class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
  
class DoublyLinkedList: 
    def __init__(self): 
        self.head = None
    def merge(self, first, second): 
        if first is None: 
            return second  
        if second is None: 
            return first 
        if first.data < second.data: 
            first.next = self.merge(first.next, second) 
            first.next.prev = first 
            first.prev = None   
            return first 
        else: 
            second.next = self.merge(first, second.next) 
            second.next.prev = second 
            second.prev = None
            return second 
    def mergeSort(self, tempHead): 
        if tempHead is None:  
            return tempHead 
        if tempHead.next is None: 
            return tempHead 
        
        tempHead = self.mergeSort(tempHead) 
        second = self.mergeSort(second) 

        return self.merge(tempHead, second) 

    def split(self, tempHead): 
        fast = slow =  tempHead 
        while(True): 
            if fast.next is None: 
                break
            if fast.next.next is None: 
                break
            fast = fast.next.next 
            slow = slow.next
              
        temp = slow.next
        slow.next = None
        return temp 

    def push(self, new_data): 

        new_node = Node(new_data) 
 
        new_node.next = self.head 

        if self.head is not None: 
            self.head.prev = new_node 

        self.head = new_node 
  
  
    def printList(self, node): 
        temp = node 
        print "Forward Traversal using next poitner"
        while(node is not None): 
            print node.data, 
            temp = node 
            node = node.next
        print "\nBackward Traversal using prev pointer"
        while(temp): 
            print temp.data, 
            temp = temp.prev 

dll = DoublyLinkedList() 
dll.push(5) 
dll.push(20); 
dll.push(4); 
dll.push(3); 
dll.push(30) 
dll.push(10); 
dll.head = dll.mergeSort(dll.head)    
print "Linked List after sorting"
dll.printList(dll.head) 

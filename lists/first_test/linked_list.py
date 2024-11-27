class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None
    
    def append(self, data):
        """Add a node at the end of the list"""
        new_node = Node(data)
        self.size += 1
        
        if self.head is None:
            self.head = new_node
            return
            
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        """Add a node at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete(self, data):
        """Delete the first occurrence of data in the linked list"""
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
            
        if current.next:
            current.next = current.next.next
            self.size -= 1
    
    def search(self, data):
        """Search for a node with the given data"""
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1
    
    def get(self, index):
        """Get data at the given index"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
            
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    
    def insert_at(self, index, data):
        """Insert a node at the given index"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
            
        if index == 0:
            self.prepend(data)
            return
            
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def __len__(self):
        """Return the length of the linked list"""
        return self.size
    
    def __str__(self):
        """String representation of the linked list"""
        if self.head is None:
            return "[]"
            
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return "[" + " -> ".join(result) + "]"

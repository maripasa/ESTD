# nth by tail
# if is circular
# remove all equal
# printinreverse
class Node:
    def __init__(self, data: int, next: "Node | None" = None):
        self.data: int = data
        self.next: Node | None = next

class LinkedList:
    def nth_by_tail(self, index):
        pass

    def is_circular(self):
        pass 

    def remove_similar(self, item_to_remove):
        pass

    def print_in_reverse(self):
        pass

    def __init__(self, values: list = []):
        self.head: Node | None = None
        for value in values:
            self.append(value)

    def insert_at_beginning(self, data) -> None:
        newNode = Node(data)
        if self.head is not None:
            newNode.next = self.head
        self.head = newNode

    def length(self) -> int:
        length: int = 0

        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            length += 1

        return length
    
    def append(self, data) -> None:
        if self.head is None:
            return self.insert_at_beginning(data)
         
        current_node: Node = self.head
        next_node: Node | None = self.head.next

        while next_node is not None:
            current_node = next_node
            next_node = next_node.next

        newNode = Node(data)
        current_node.next = newNode

    def remove_first_node(self) -> int:
        if self.head is None:
            raise IndexError("can't remove an item from an empty list.")
        removed_value = self.head.data
        self.head = self.head.next
        return removed_value
    
    def pop(self) -> int:
        if self.head is None:
            raise IndexError("can't remove an item from an empty list.")
        if self.head.next is None:
            return self.remove_first_node()
        
        current_node: Node = self.head
        next_node: Node = self.head.next

        while next_node.next is not None:
            current_node = next_node
            next_node = next_node.next

        removed_value = next_node.data
        current_node.next = None
       
        return removed_value
    
    def remove_item(self, index: int) -> int:
        if index == 0:
            return self.remove_first_node()

        if index > self.length():
            raise IndexError("index bigger than list.")
        
        current_node: Node = self.head
        next_node: Node = self.head.next
        
        for _ in range(index - 1):
            current_node = next_node
            next_node = next_node.next
        
        current_node.next = next_node.next
        return next_node.data

    def insert(self, index, value) -> None:
        if index == 0:
            return self.insert_at_beginning(value)

        current_node: Node = self.head
        next_node: Node = self.head.next

        for _ in range(index - 1):
            current_node = next_node
            next_node = next_node.next
        
        new_node = Node(value)
        current_node.next = new_node
        new_node.next = next_node

    def __str__(self) -> str:
        output = "["

        current_node = self.head

        while current_node is not None:
            output += f"{current_node.data}"
            if current_node.next is not None:
                output += ", "
            current_node = current_node.next
        output += "]"
        return output

    def __getitem__(self, index: int) -> int:
        if index - 1 > self.length:
            raise IndexError("index biggen than list")
        
        current_node = self.head
        for i in range(index):
            current_node = current_node.next

        return current_node.data


    def __setitem__(self, index: int, value: int):
        if index - 1 > self.length:
            raise IndexError("index biggen than list")
        
        current_node = self.head
        for i in range(index):
            current_node = current_node.next

        current_node.data = value

lista = LinkedList()
lista.append(5)
print(lista.head.data)
lista.append(6)
print(lista.head.data)
lista.append(15)
print(lista.head.data)
print(lista.length())
print(lista)

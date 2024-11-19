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

    def __init__(self):
        self.head: Node | None = None
        
    def insert_at_beginning(self, data) -> None:
        newNode = Node(data)
        if self.head is not None:
            newNode.next = self.head
        self.head = newNode
    
    # Looks really ugly
    def insert_at_end(self, data) -> None:
        if self.head is None:
            return self.insert_at_beginning(data)
         
        current_node: Node = self.head

        if isinstance(self.head.next, Node):
            next_node: Node = self.head.next

            while next_node.next is not None:
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
    
    def remove_last_node(self) -> int:
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
    
    def remove(self, position) -> None:
        #pode alterar a forma que o index funciona?
        pass
    
    def insert(self, position, value) -> None:
        pass
           
    def __str__(self) -> str:
        output = "["

        current_node = self.head

        while current_node is not None:
            output += f"{current_node.data}"
            if current_node.next is None:
                output += ", "
            current_node = current_node.next
        output += "]"
        return output


lista = LinkedList()
lista.insert_at_beginning(5)
print(lista)

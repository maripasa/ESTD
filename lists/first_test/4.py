from .linked_list import LinkedList

def invert_linked_list(linked_list: LinkedList):
    current_node = linked_list.head
    next_node = linked_list.head.next
    current_node.next = None
    while next_node.next is not None:
        future_node = next_node.next
        next_node.next = current_node
        next_node = future_node
        current_node = next_node
    next_node.next = current_node 
    linked_list.head = next_node

    return linked_list

""" def  """

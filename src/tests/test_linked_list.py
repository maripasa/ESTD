import pytest
from ..linked_list import LinkedList, Node

def test_insert_at_beginning():
    lista = LinkedList()
    lista.insert_at_beginning(5)
    assert str(lista) == "[5]"
    
    lista.insert_at_beginning(10)
    assert str(lista) == "[10, 5]"

def test_length():
    lista = LinkedList()
    assert lista.length() == 0
    
    lista.insert_at_beginning(5)
    assert lista.length() == 1
    
    lista.append(10)
    assert lista.length() == 2

def test_append():
    lista = LinkedList()
    lista.append(5)
    assert str(lista) == "[5]"
    
    lista.append(10)
    assert str(lista) == "[5, 10]"

def test_remove_first_node():
    lista = LinkedList()
    lista.insert_at_beginning(5)
    removed = lista.remove_first_node()
    assert removed == 5
    assert lista.length() == 0

    with pytest.raises(IndexError):
        lista.remove_first_node()

def test_pop():
    lista = LinkedList()
    lista.append(5)
    lista.append(10)
    lista.append(15)
    
    removed = lista.pop()
    assert removed == 15
    assert str(lista) == "[5, 10]"

    empty_list = LinkedList()
    with pytest.raises(IndexError):
        empty_list.pop()

def test_remove_item():
    lista = LinkedList()
    lista.append(5)
    lista.append(10)
    lista.append(15)
    
    lista.remove_item(1)
    assert str(lista) == "[5, 15]"
    
    with pytest.raises(IndexError):
        lista.remove_item(5)

def test_insert():
    lista = LinkedList()
    lista.append(5)
    lista.append(15)
    lista.insert(1, 10)
    assert str(lista) == "[5, 10, 15]"

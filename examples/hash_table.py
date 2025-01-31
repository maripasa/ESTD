from collections import Counter
from typing import  List, Callable

def count_max_words(s: str) -> List:
    return Counter(s.lower().split()).most_common(3)

def sum_hash(key: object) -> int: ...
def polinomial_hash(key: object) -> int: ...
def critical_hash(key: object) -> int: ...

def division_compress(num: int) -> int: ...
def fold_compress(num: int) -> int: ...
def mad_compress(num: int) -> int: ...

class HashNode:
    def __init__(self, key, value, next=None):
        if key is None:
            raise ValueError("Can't be None")
        self.key = key
        self.value = value
        self.next = next

class HashTable:
    def __init__(self, hashing_method: Callable[[object], int], compression_method: Callable[[int], int], size: int = 32):
        self.table: List[None | HashNode] = [None] * size
        self.hashing_method: Callable[[object], int] = hashing_method
        self.compression_method: Callable[[int], int] = compression_method
        self.existing_keys = set()

    def __setitem__(self, key: object, value: object) -> None:
        index: int = self.compression_method(self.hashing_method(key))
        current_node = self.table[index]

        if current_node is None:
            current_node = HashNode(key, value) 
            return
        
        next_node = current_node

        while next_node is not None:
            if next_node.key == key:
                next_node.value = value
                return

            current_node = next_node
            next_node = next_node.next

        current_node.next = HashNode(key, value)

    def __getitem__(self, key: object) -> object:
        index: int = self.compression_method(self.hashing_method(key))
        current_node = self.table[index]

        if current_node is None:
            raise KeyError()

        while current_node.key != key:
            next_node = current_node.next
            if next_node is None:
                raise KeyError()
        
        return current_node.value


        
            

    """ def copy(self) -> dict[_KT, _VT]: ...
    
    static methods:
    def fromkeys(cls, iterable: Iterable[_T], value: None = None, /) -> dict[_T, Any | None]: ...
    def fromkeys(cls, iterable: Iterable[_T], value: _S, /) -> dict[_T, _S]: ...

    def get(self, key: _KT, /) -> _VT | None: ...
    def pop(self, key: _KT, /) -> _VT: ...

    def __len__(self) -> int: ...
    def __getitem__(self, key: _KT, /) -> _VT: ...
    def __setitem__(self, key: _KT, value: _VT, /) -> None: ...
    def __delitem__(self, key: _KT, /) -> None: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def __eq__(self, value: object, /) -> bool: ...
    def __reversed__(self) -> Iterator[_KT]: ...

    def keys(self) -> dict_keys[_KT, _VT]: ...
    def values(self) -> dict_values[_KT, _VT]: ...
k in M
M.get(k, d=None)
M.setdefault(k,d)
se k existir, devolve o valor. senao, setta e retorna d
M.pop(k, d=None)
remove k e retorna o valor
M.popitem() valor aleatorio
.clear
.keys()
.values()
.items()
.update(M2)
== !=
"""

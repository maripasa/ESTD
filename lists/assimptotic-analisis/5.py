def biggest_10(lista: list):
    # Handle edge cases
    if len(lista) <= 10:
        return sorted(lista, reverse=True)
    
    # Initialize with first 10 elements
    comparator = lista[:10]
    comparator.sort()
    
    # Check remaining elements
    for i in range(10, len(lista)):
        if lista[i] > comparator[0]: 
            comparator[0] = lista[i]
            comparator.sort()      
            
    return sorted(comparator, reverse=True)


test_list = [1, 5, 2, 8, 12, 3, 7, 9, 15, 4, 6, 11]
print(biggest_10(test_list))

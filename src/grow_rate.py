

# O(n)
def find_element(array: list, key: int):
    for i in array:
        if i == key:
            return True
    return False

# O(n^2)
def bubble_sort(array):
    n = len(array)


print(find_element([3,4,5,6,7,2,4,6,7,4,5], 3))

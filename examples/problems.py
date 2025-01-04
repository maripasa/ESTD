""" def reverse_queue(queue: Queue):
    queue_stack: list = []
    for item in queue:
        queue_stack.append(item)
    for item in queue_stack:
        queue.enQueue(item) """


def reverse_list(lista: list):
    for i in range(len(lista) // 2):
        lista[i], lista[-1 * (i + 1)] = lista[-1 * (i + 1)], lista[i] 
    return lista

print(reverse_list([1,2,3,4,5,6,7]))
print(reverse_list([1,2,3,4,5,6]))

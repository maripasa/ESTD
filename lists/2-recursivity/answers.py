""" Projete um algoritmo recursivo para determinar o maior elemento em uma sequência de inteiros S com n elementos.
Qual é a complexidade do seu algoritmo? Desenhe a árvore de recursão. """

def biggest_element(numbers: list) -> int:
    return numbers[0] if len(numbers) == 1 else biggest_element(numbers[1:]) if biggest_element(numbers[1:]) > numbers[0] else numbers[0]
"""
Infelizmente fiz eu uma linha pq ia ser engraçado, então a complexidade é O(n^2)
biggest_element([a, b, c, d])
├── biggest_element([b, c, d])
│     ├── biggest_element([c, d])
│     │     ├── biggest_element([d])
│     │     └── Compare: biggest_element([d]) > c ? biggest_element([d]) : c
│     └── Compare: biggest_element([c, d]) > b ? biggest_element([c, d]) : b
└── Compare: biggest_element([b, c, d]) > a ? biggest_element([b, c, d]) : a

os biggest_element das comparações trazem... mais recursões.
"""
print(biggest_element([2,5,7,3,2,6,1,23,5,4,76]))

""" Faça um diagrama das chamadas recursivas de uma função que resolve o problema das torres de hanoi. """
def hanoi(n: int, start: int, end: int) -> None:
    if start < 1 or start > 3:
        raise ValueError("Invalid start")
    if end < 1 or end > 3:
        raise ValueError("Invalid end")
    if start == end:
        raise ValueError("start can't be equal to end")
    if n < 1:
        raise ValueError("n cannot be less then 1")
    if n == 1:
        print(start, "->", end)
        return
    hanoi(n-1, start, 6 - (start + end))
    hanoi(1, start, end)
    hanoi(n-1, 6 - (start + end), end)

print(hanoi(9, 1, 3))

"""
Move 3 disks from A to C using B:
  ├── Move 2 disks from A to B using C:
  │   ├── Move 1 disk from A to C using B:
  │   │   └── Move disk 1 from A to C
  │   └── Move disk 2 from A to B
  │   └── Move 1 disk from C to B using A:
  │       └── Move disk 1 from C to B
  ├── Move disk 3 from A to C
  └── Move 2 disks from B to C using A:
      ├── Move 1 disk from B to A using C:
      │   └── Move disk 1 from B to A
      └── Move disk 2 from B to C
      └── Move 1 disk from A to C using B:
          └── Move disk 1 from A to C
"""

""" Escreva um algoritmo recursivo que organize uma sequência de inteiros de tal forma que os valores pares apareçam
antes do que os ímpares. """

def even_numbers_in_front(numbers: list) -> list:
    return numbers if len(numbers) == 1 else numbers[:1] + even_numbers_in_front(numbers[1:]) if numbers[0] % 2 == 0 else even_numbers_in_front(numbers[1:]) + numbers[:1]

print(even_numbers_in_front([2,5,7,3,2,6,1,23,5,4,76]))

"""
maiorDigito
    retorna o maior dígito de um inteiro

menorDigito
    retorna o menor dígito de um inteiro

contaDigito
    retorna a quantidade de dígitos de um inteiro

somaDigito
    retorna a soma dos dígitos de um inteiro

zeraPares
    retorna um inteiro com os dígitos pares em zero

zeraImpares
    retorna um inteiro com os dígitos ímpares em zero

removePares
    remove os dígitos pares de um inteiro """

def maiorDigito(number: int) -> int:
    return number if number < 10 else maiorDigito(number//10) if maiorDigito(number//10) > number%10 else number%10

print(maiorDigito(28347289684012))

def menorDigito(number: int) -> int:
    return number if number < 10 else menorDigito(number//10) if menorDigito(number//10) < number%10 else number%10

print(menorDigito(28347289684012))

def contaDigito(number: int) -> int:
    return 1 if number < 10 else contaDigito(number//10) + 1

print(contaDigito(28347289684012))

def somaDigito(number: int) -> int:
    return number if number < 10 else somaDigito(number//10) + number%10

print(somaDigito(28347289684012))

def zeraPares(number: int) -> int:
    return number*(number%2) if number<10 else zeraPares(number//10)*10 + (number%10) * (number%2)

print(zeraPares(28347289684012))
# 307009000010

def zeraImpares(number: int) -> int:
    return number*((number-1)%2) if number<10 else zeraImpares(number//10)*10 + (number%10) * ((number+1)%2)

print(zeraImpares(28347289684012))
# 28040280684002

def removePares(number: int) -> int:
    return number*(number%2) if number<10 else removePares(number//10)*(10 - (9 * ((number+1)%2))) + (number%10) * (number%2)

print(removePares(28347289684012))
print(removePares(13579315973))
print(removePares(13579316973))
# 3791

""" Crie uma função recursiva para verificar se uma string tem mais vogais do que consoantes. """
def has_more_vowels(input: str) -> bool:
    def count_vowels(input: str) -> int:
        return 0 if not input else (1 if input[0].lower() in "aeiou" else 0) + count_vowels(input[1:])
    def count_consonants(input: str) -> int:
        return 0 if not input else (1 if input[0].lower() not in "aeiou" else 0) + count_consonants(input[1:])
    return count_vowels(input) > count_consonants(input)

print(has_more_vowels("string"))

"""Implemente o algoritmo de busca binária em um vetor de inteiros ordenado."""
def binary_search(key: int, input: list[int]) -> int | None:
    if len(input) == 0:
        return None
    
    mid = len(input) // 2
    if input[mid] == key:
        return mid
    elif input[mid] > key:
        result = binary_search(key, input[:mid])
        if result is None:
            return None
        return result
    else:
        result = binary_search(key, input[mid+1:])
        if result is None:
            return None
        return mid + 1 + result

"""Dados um vetor de inteiros distintos e ordenados de maneira crescente e um inteiro target, crie um algoritmo recursivo que determine se existem dois inteiros no vetor que a soma seja igual a target."""
def find_inner_sum(target: int, input: list[int]) -> bool:
    def helper(start: int, end: int) -> bool:
        if start >= end:
            return False
        total = input[start] + input[end]
        if total == target:
            return True
        elif total < target:
            return helper(start + 1, end)
        else:
            return helper(start, end - 1)

    if len(input) < 2:
        raise ValueError("Too small of a list, make it > 2")
    
    return helper(0, len(input) - 1)

print(find_inner_sum(7, [1, 2, 3, 4, 5, 6, 7, 8]))

"""Dado um array S não ordenado de inteiros e um inteiro k, crie um algoritmo recursivo para reorganizar os elementos de S tal que todos os elementos menores ou iguais a K apareçam antes do que os elementos maiores."""

def funny_sort(k: int, s: list[int]) -> list[int]:
    if len(s) <= 1: return s
    return [s[0]] + funny_sort(k, s[1:]) if s[0] <= k else funny_sort(k, s[1:]) + [s[0]] 

print(funny_sort(3, [1,2,3,4,5,6,7,8]))
print(funny_sort(3, [3,4,5,6,7,8]))
    

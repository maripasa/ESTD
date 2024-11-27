""" Projete um algoritmo recursivo para determinar o maior elemento em uma sequência de inteiros S com n elementos.
Qual é a complexidade do seu algoritmo? Desenhe a árvore de recursão. """

def biggest_element(numbers: list) -> int:
    return numbers[0] if len(numbers) == 1 else biggest_element(numbers[1:]) if biggest_element(numbers[1:]) > numbers[0] else numbers[0]

# althought this could be made
def biggest_element_2(numbers: list) -> int:
    return max(numbers)

# or even
def biggest_element_3(numbers: list) -> int:
    return sorted(numbers)[-1]

print(biggest_element([2,5,7,3,2,6,1,23,5,4,76]))

""" Faça um diagrama das chamadas recursivas de uma função que resolve o problema das torres de hanoi. """
# depois pq da trabalho

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
    return number

print(zeraPares(28347289684012))


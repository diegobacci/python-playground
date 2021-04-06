import random
import time
import os

# Objetivo desse Script é comprovar que o algoritmo binary search é mais rápido que o algoritmo naive search

# Naive Search: Varre pela lista toda a procura do elemento e caso encontre, retorna indice, senão retorna -1
def naive_search(lista, elemento_escolhido):
    # varre todos os indices da lista (0 até len(lista))
    for i in range(len(lista)):
        if lista[i] == elemento_escolhido:
            return i

    return -1

# Binary Search Algorithm:
#   - Utiliza divisao da lista
#   - Utiliza lista ordenada (sorted(lista)))
def binary_search(lista, elemento_escolhido, menor=None, maior=None):
    if menor is None:
        menor = 0
    if maior is None:
        maior = len(lista) - 1

    # O maior indice nunca deve ser menor que o menor indice
    if maior < menor:
        return -1  # O elemento_escolhido não está na lista

    # Valor inteiro, descartando o decimal # Todos os valores em menor + maior
    # Exemplo: lista = [1, 3, 5, 7, 9] # 2 (indice do ponto_medio)
    ponto_medio = (menor + maior) // 2

    if lista[ponto_medio] == elemento_escolhido:
        return ponto_medio  # ponto medio é o indice
    elif elemento_escolhido < lista[ponto_medio]:
        # Parte da parte esquerda da lista, em relação ao ponto médio
        return binary_search(lista, elemento_escolhido, menor, ponto_medio - 1)
    else:
        # Parte da parte direita da lista, em relação ao ponto médio
        return binary_search(lista, elemento_escolhido, ponto_medio + 1, maior)


if __name__ == '__main__':
    lista = [1, 9, 10, 11, 13, 15]  # ponto_medio == 3
    elemento_escolhido = 11
    # Retorna o indice do elemento_escolhido da lista
    print(naive_search(lista, elemento_escolhido))
    print(binary_search(lista, elemento_escolhido))

    # Análise do tempo de execução de listas maiores:
    tamanho = 15000
    # Criado para não receber valores iguais dentro do loop de repetição
    lista_ordenada = set()
    while len(lista_ordenada) < tamanho:
        # Range de números aleatorios vao de -75000 até 75000, totalizando 150k valores possiveis
        lista_ordenada.add(random.randint(-5*len(lista_ordenada), 5*len(lista_ordenada)))

    # Transformada em lista e ordenada
    lista_ordenada = sorted(list(lista_ordenada))

    os.system('cls' if os.name == 'nt' else 'clear')

    # Naive Search:
    inicio = time.time()  # Tempo atual
    # Quantidade de loops == len(lista_ordenada) -> Todos elementos da lista serão elemento_escolhido uma hora
    for elemento_escolhido in lista_ordenada:
        naive_search(lista_ordenada, elemento_escolhido)
    fim = time.time()  # Tempo após todos os loops
    # Tempo por iteração
    print(f"Tempo de execução:\n\nNaive Search: {(fim - inicio)/tamanho} segundos/iteração")

    # Binary Search:
    inicio = time.time()
    for elemento_escolhido in lista_ordenada:
        binary_search(lista_ordenada, elemento_escolhido)
    fim = time.time()
    print(f"Binary Search: {(fim - inicio)/tamanho} segundos/iteração")

import os

def fibonacci(numero_vezes):
    a = 0
    b = 1

    if numero_vezes > 0:
        if numero_vezes == 1:
            print(a)
        else: 
            print(a)
            print(b)

    # Loop que começa em 2, pois o indice 0 e 1 já possuem valores
    # 0, 1, 1, 2, 3
    for i in range(2, numero_vezes): # numero_vezes vai até o indice 4
        c = a + b
        a = b
        b = c 

        print(c)

def tamanho_fibonacci(): # 5 primeiros valores da sequência
    try:
        tamanho = int(input("Tamanho da sequência: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if tamanho <= 0:
            input("Entrada deve ser um valor positivo.")
            os.system('cls' if os.name == 'nt' else 'clear')
            tamanho_fibonacci()
        else:
            print(f"Tamanho da sequência: {tamanho}\n")
            fibonacci(tamanho)
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        input("Entrada inválida. Tente novamente...")
        os.system('cls' if os.name == 'nt' else 'clear')
        tamanho_fibonacci()

tamanho_fibonacci()
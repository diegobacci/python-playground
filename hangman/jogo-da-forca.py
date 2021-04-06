import random
from palavras import * 
import string
import os

tema_escolhido = random.randint(1, quantidade_temas)
lista_palavras = []
tema = ''

if tema_escolhido == 1:
    lista_palavras = palavras_objetos.copy()
    tema = 'Objetos'
elif tema_escolhido == 2:
    lista_palavras = palavras_paises.copy()
    tema = 'Países'
elif tema_escolhido == 3:
    lista_palavras = palavras_comidas.copy()
    tema = 'Comidas'


def retirar_palavra_escolhida(lista_palavras):
    # Aleatoriamente escolhe uma palavra dentro da lista "lista_palavras"
    palavra_escolhida = random.choice(lista_palavras)
    return palavra_escolhida.upper()


def jogo_da_forca():
    palavra = retirar_palavra_escolhida(lista_palavras)
    letras_palavra = set(palavra)  # Todas as letras da palavra sem repetir
    letras_alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()

    numeros_vida = 4

    while len(letras_palavra) > 0 and numeros_vida > 0:
        print(f"O tema é: {tema}\n")

        # '%'.join(['a', 'e', 'i']) -> Transforma elementos de uma lista em uma string separada pelo elemento especificado -> a%e%i
        print("PALAVRAS: ", ' '.join(letras_usadas))
        print(f"VIDAS: {numeros_vida}\n")

        # Visibilidade atual da palavra de acordo com os acertos do usuário
        palavra_abstrata = [
            letra if letra in letras_usadas else '-' for letra in palavra]
        print("Palavra atual: ", ' '.join(palavra_abstrata))

        # Tentativa deve ser maiuscula pois palavra tambem é
        letra_usuario = input("\nAdivinhe uma letra da palavra: ").upper()

        if letra_usuario in letras_alfabeto - letras_usadas:
            letras_usadas.add(letra_usuario)
            if letra_usuario in letras_palavra:
                # Usuário acertou a letra.
                letras_palavra.remove(letra_usuario)
                # Limpa o terminal cross-plataforma (Windows e Unix)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                numeros_vida = numeros_vida - 1
                os.system('cls' if os.name == 'nt' else 'clear')
        elif letra_usuario in letras_usadas:
            input("\nVocê já tentou essa letra. Tente novamente. . .")
            os.system('cls' if os.name == 'nt' else 'clear')

        else:  # Caractere fora do alfabeto
            input("\nCaractere inválido. Por favor digite uma letra do alfabeto. . .")
            os.system('cls' if os.name == 'nt' else 'clear')

    if numeros_vida == 0:
        print("\nVocê morreu... Tente novamente!!")
    else:
        print(
            f"\nVocê é um vencedor!!\nA palavra selecionada era: {palavra.upper()}")

jogo_da_forca()

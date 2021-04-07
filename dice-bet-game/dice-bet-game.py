import os
import random

def continuar_jogando():
    print("\n[ 0 ] - Sair\n[ 1 ] - Jogar")
    escolha = int(input("\nResposta: "))

    if escolha == 0:
        exit()
    elif escolha != 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        input("Entrada inválida. Tente novamente...")
        os.system('cls' if os.name == 'nt' else 'clear')
        continuar_jogando()

    return True

def escolhada_dado():
    valor_dado_escolhido = int(input("Valor do dado: "))
    if valor_dado_escolhido < 1 and valor_dado_escolhido > 6: 
        input("Entrada inválida. Tente novamente...") 
        quantidade_apostada()
        os.system('cls' if os.name == 'nt' else 'clear')


def quantidade_apostada():
    try: 
        quantidade_apostada = float(input("\nApostar: R$ "))
        quantidade_apostada = round(quantidade_apostada, 2) # Arredonda as duas casas decimais
    except:
        print("Entrada inválida. Tente novamente...")
        quantidade_apostada()
        
    return quantidade_apostada

def usuario_ganhou(escolhada_dado, dado_secreto):
    # Se usuário acertou o número do dado, ele ganha 50% do valor apostado
    if escolhada_dado == dado_secreto:
        print("Parabéns, você acertou o dado!!!")
        return True
    
def status(saldo_total, quantidade_apostada): 
    print("Informar todos status? \n")
    print("[ S ] - Sim\n[ N ] - Não\n")
    resposta = input("Resposta: ").lower()
    if resposta != 's' and resposta != 'n':
        input("Entrada inválida. Tente novamente...")
        status(saldo_total, quantidade_apostada)
    if resposta == 's':
        print(f"Dinheiro apostado na ultima rodada: {quantidade_apostada}")
        print(f"Salto total: {saldo_total}")


def jogar():
    partida_acontecendo = 1
    while partida_acontecendo:
        primeira_vez = 1
        if primeira_vez:
            print("Bem-vindo às apostas com dados!!!\n")
            primeira_vez += 1

        continuar_jogando()

        # Inserção de dados do usuário
        print("Insira suas informações: \n")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        cpf = int(input("CPF: "))
        saldo_total = float(input("Saldo total: R$ "))
        
        os.system('cls' if os.name == 'nt' else 'clear')

        escolhada_dado()
        quantidade_apostada()
        dado_secreto = random.randint(1, 6)

        if usuario_ganhou(escolhada_dado, dado_secreto): 
            saldo_total = saldo_total + quantidade_apostada + (quantidade_apostada / 2) 

            continuar_jogando()

        saldo_total = saldo_total - quantidade_apostada
        continuar_jogando()

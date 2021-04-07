import sys
import os
import string
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

def jogada():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[ Pe ] - Pedra\n[ Pa ] - Papel\n[ Te ] - Tesoura")
    jogada_usuario = input("\nEscolha: ").lower()

    # FAZER VERIFICACAO DE OUTROS TIPOS ALEM DE A-Z
    if jogada_usuario != 'pe' and jogada_usuario != 'pa' and jogada_usuario != 'te': 
        os.system('cls' if os.name == 'nt' else 'clear')
        input("Entrada inválida. Tente novamente...")
        jogada()

    return jogada_usuario

def nome_jogada(jogada_maquina):
    if jogada_maquina == 'pe':
        return 'Pedra'
    elif jogada_maquina == 'pa':
        return 'Papel'
    else:
        return 'Tesoura'


def jogador_venceu(jogada_usuario, jogada_maquina):
    if (jogada_usuario == 'pe' and jogada_maquina == 'te') or (jogada_usuario == 'te' and jogada_maquina == 'pa') \
        or (jogada_usuario == 'pa' and jogada_maquina == 'pe'):
        return True

def jogar():
    partida_acontecendo = 1
    while partida_acontecendo:
        primeira_vez = 1

        if primeira_vez == 1:
            print("Bem-vindo ao jogo da forca!!!")
            primeira_vez += 1

        continuar_jogando()
        jogada_usuario = jogada()
        jogada_maquina = random.choice(['pe', 'pa', 'te'])
    	
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Jogada usuário: {jogada_usuario}")
        print(f"Jogada máquina: {jogada_maquina}")

        if jogada_usuario == jogada_maquina:
            input("\nEmpatou!!!")
            # Transformar em uma função
            jogada_usuario = jogada()
            jogada_maquina = random.choice(['pe', 'pa', 'te'])

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Jogada usuário: {jogada_usuario}")
            print(f"Jogada máquina: {jogada_maquina}")

        if jogador_venceu(jogada_usuario, jogada_maquina):
            input("\nVocê venceu!!!")
            os.system('cls' if os.name == 'nt' else 'clear')
            partida_acontecendo = continuar_jogando()
            
        
        input("Você perdeu...")
        os.system('cls' if os.name == 'nt' else 'clear')
        partida_acontecendo = continuar_jogando()
        
jogar()

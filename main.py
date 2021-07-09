#Para rodar o programa é necessário instalar a biblioteca "pygame"
#Para instalar essa biblioteca é necessário ter o "pip" instalado em sua máquina
#Após a instalção do pip abra o menu de pesquisa do Windows e digite CMD
#Com o CMD aberto digite "pip install pygame"
#Instalar art
#Após esses processos serem feitos você conseguirá jogar normalmente

#import pygame

import time, sys, os
from character import Character
from character_ing import Character_ing
from tutorial import Tutorial
from banner import Banner
from music import Musica

if __name__ == "__main__":
    
    while True:
        personagem = Character()
        personagem_ing = Character_ing()
        tutoriais = Tutorial()
        musicas = Musica()
        banner = Banner()

        musicas.musica_ini()
        banner.title_banner()
        time.sleep(5)
        input("\nAperte ENTER para continuar...")
        os.system("cls")
        print("")
        print("Escolha a linguagem do jogo\n[1] INGLÊS \n[2] PORTUGUÊS")
        lingua = int(input("Sua escolha : "))

        print("")
        if lingua == 2:
            os.system("cls")
            ver_tutorial = input("Deseja ver o tutorial? [S/N] : ").upper()
        elif lingua == 1:
            os.system("cls")
            ver_tutorial = input("Do you wanna see the tutorial? [Y/N] : ").upper()

        while ver_tutorial!= "S" and ver_tutorial!="N" and ver_tutorial!="Y":
            print("")
            if lingua == 2:
                os.system("cls")
                print("Digite a opçao correta [S/N]")
                ver_tutorial = input("Deseja ver o tutorial? [S/N]: ").upper()
                
            elif lingua == 1:
                os.system("cls")
                print("Write correctly [Y/N]")
                ver_tutorial = input("Do you wanna see the tutorial? [Y/N]: ").upper()
                
        if ver_tutorial == "S":
            tutoriais.tutorial_pt()
        elif ver_tutorial == "Y":
            tutoriais.tutorial_ing()

        os.system("cls")

        if lingua == 2:
            musicas.digitar()
            frase = ("Após 6 meses viajando a negócios, você recebeu a noticia que poderia voltar para casa, e chegaria a tempo do casamento da sua filha... Mau sabia que essa viagem mudaria completamente sua vida...\nO avião que você estava sofreu um acidente durante uma tempestade e caiu em uma ilha aparentemente deserta, seu objetivo é sobreviver e escapar da ilha para chegar em tempo de levar sua filha ao altar.")

            for i in list(frase):
                print(i, end='')
                #O stdout só é atualizado quando há nova linha e como nós estamos mandando tudo na mesma é preciso forçar a atualização.
                sys.stdout.flush()
                time.sleep(0.065)
            print("")
            input("\nAperte ENTER para iniciar o jogo...")

        elif lingua == 1:
            musicas.digitar()
            frase = ("After 6 months traveling on business, you received the news that you could return home, and arrive in time for your daughter's wedding... Bad did you know that this trip would completely change your life...\nThe plane you were on had an accident during a storm and crashed on a seemingly deserted island, your goal is to survive and escape the island to reach in time to take your daughter to the altar.")

            for i in list(frase):
                print(i, end='')
                #O stdout só é atualizado quando há nova linha e como nós estamos mandando tudo na mesma é preciso forçar a atualização.
                sys.stdout.flush()
                time.sleep(0.065)
            print("")
            input("\nPress ENTER to start the game...")
        os.system("cls")

        while True:
            if lingua == 1:
                personagem_ing.status_ing()
                print("=-"*25)
                print('''                [1] - EAT 🍗
                [2] - LOOK FOR FOOD 👀
                [3] - LOOK FOR ITENS 🎒
                [4] - HEAL UP 💊
                [5] - SLEEP 😴
                [6] - ESCAPE 🏃
                [7] - LEAVE THE GAME 🚪''')
                print("=-"*25)
                escolha = int(input("Write your action : "))

            elif lingua == 2:
                personagem.status()
                print("=-"*25)
                print('''                [1] - COMER 🍗
                [2] - PROCURAR COMIDA 👀
                [3] - PROCURAR ITENS 🎒
                [4] - SE MEDICAR 💊
                [5] - DORMIR 😴
                [6] - FUGIR 🏃
                [7] - SAIR DO JOGO 🚪''')
                print("=-"*25)
                escolha = int(input("Digite sua açao : "))

            if escolha == 1:
                if lingua == 1:
                    personagem_ing.comer_ing()
                elif lingua == 2:
                    personagem.comer()

            elif escolha == 2:
                if lingua == 1:
                    personagem_ing.procurar_comida_ing()
                elif lingua == 2:
                    personagem.procurar_comida()

            elif escolha == 3:
                if lingua == 1:
                    personagem_ing.procurar_itens_ing()
                elif lingua == 2:
                    personagem.procurar_itens()

            elif escolha == 4:
                if lingua == 1:
                    personagem_ing.medicar_ing()
                elif lingua == 2:
                    personagem.medicar()

            elif escolha == 5:
                if lingua == 1:
                    personagem_ing.dormir_ing()
                elif lingua == 2:
                    personagem.dormir()

            elif escolha == 6:
                if lingua == 1:
                    personagem_ing.fugir_ing()
                elif lingua == 2:
                    personagem.fugir()
                    
            elif escolha == 7:
                if lingua == 1:
                    personagem_ing.sair_ing()
                elif lingua == 2:
                    personagem.sair()
            else:
                print("")
                if lingua == 1:
                    input('Invalid Option! Please choose a valid action')  
                elif lingua == 2:
                    input('Opção Invalida! Por favor escolha uma ação do menu')    
            os.system("cls")        


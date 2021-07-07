#Para rodar o programa é necessário instalar a biblioteca "pygame"
#Para instalar essa biblioteca é necessário ter o "pip" instalado em sua máquina
#Após a instalção do pip abra o menu de pesquisa do Windows e digite CMD
#Com o CMD aberto digite "pip install pygame"
#Após esses processos serem feitos você conseguirá jogar normalmente

import pygame

import time, sys, os
from character import Character



if __name__ == "__main__":
    def tutorial():
        os.system("cls")
        print("=-"*25)
        print("==================== TUTORIAL ====================")
        print("=-"*25)
        print('''       Nesse jogo seu objetivo é sobreviver em uma ilha 
                    deserta, coletando itens para fugir e se alimentar enquanto
                      tenta sobreviver as surpresas que essa ilha lhe reserva''')
        input("\nAperte enter para continuar o tutorial...")
        os.system("cls")
        print("")
        print("O menu abaixo representa as escolhas que podem ser feitas durante o jogo")
        print("=-"*25)
        print('''        [1] - COMER 🍗
        [2] - PROCURAR COMIDA 👀
        [3] - PROCURAR ITENS 🎒
        [4] - SE MEDICAR 💊
        [5] - DORMIR 😴
        [6] - FUGIR 🏃
        [7] - SAIR DO JOGO 🚪''')
        print("=-"*25)
        print("")
        input("\nAperte enter para continuar...")
        os.system("cls")
        
        print("A opção [1] COMER faz com que sua vida regenere em 20 unidades")
        print("A opção [2] PROCURAR COMIDA faz com que o personagem saia em busca de comida")
        print("A opção [3] PROCURAR ITENS faz com que o personagem saia em busca de itens")
        print("A opção [4] SE MEDICAR faz com que sua vida regenere totalmente")
        print("A opção [5] DORMIR faz com sua vida regenere em 10 unidades e passe para o próximo dia")
        print("A opção [6] FUGIR faz com que seu personagem tente fugir da ilha")
        print("A opção [7] SAIR DO JOGO fecha o jogo e apresenta os créditos")
        print("")
        input("\nAperte enter para iniciar o jogo...")

    while True:
        personagem = Character()
        print(''' d888888b db   db d88888b   d888888b .d8888. db       .d8b.  d8b   db d8888b. 
 `~~88~~' 88   88 88'         `88'   88'  YP 88      d8' `8b 888o  88 88  `8D 
    88    88ooo88 88ooooo      88    `8bo.   88      88ooo88 88V8o 88 88   88 
    88    88~~~88 88~~~~~      88      `Y8b. 88      88~~~88 88 V8o88 88   88 
    88    88   88 88.         .88.   db   8D 88booo. 88   88 88  V888 88  .8D 
    YP    YP   YP Y88888P   Y888888P `8888Y' Y88888P YP   YP VP   V8P Y8888D' 
                                                                             ''')

            #Musica de suspense

        input("\nAperte enter para continuar...")
        
        print("")
        ver_tutorial = input("Deseja ver o tutorial? [S/N]: ").upper()
        while ver_tutorial!= "S" and ver_tutorial!="N":
            ver_tutorial = input("Deseja ver o tutorial? [S/N]: ").upper()
            print("Digite a opçao correta [S/N]")
        if ver_tutorial == "S":
            tutorial()
        os.system("cls")

        frase = ("Após 6 meses viajando a negócios, você recebeu a noticia que poderia voltar para casa, e chegaria a tempo do casamento da sua filha... Mau sabia que essa viagem mudaria completamente sua vida...\nO avião que você estava sofreu um acidente durante uma tempestade e caiu em uma ilha aparentemente deserta, seu objetivo é sobreviver e escapar da ilha para chegar em tempo de levar sua filha ao altar.")

        for i in list(frase):
            print(i, end='')
           # O stdout só é atualizado quando há nova linha e como nós estamos mandando tudo na mesma é preciso forçar a atualização.
            sys.stdout.flush()
            time.sleep(0.05)

        input("\nAperte enter para iniciar o jogo...")
        os.system("cls")

        while True:
            personagem.status()

            print("=-"*25)
            print('''            [1] - COMER 🍗
            [2] - PROCURAR COMIDA 👀
            [3] - PROCURAR ITENS 🎒
            [4] - SE MEDICAR 💊
            [5] - DORMIR 😴
            [6] - FUGIR 🏃
            [7] - SAIR DO JOGO 🚪''')
            print("=-"*25)
            escolha = int(input("Digite sua açao : "))

            if escolha == 1:
                personagem.comer()
               
            elif escolha == 2:
                personagem.procurar_comida()

            elif escolha == 3:
                personagem.procurar_itens()

            elif escolha == 4:
                personagem.medicar()

            elif escolha == 5:
                personagem.dormir()

            elif escolha == 6:
                personagem.fugir()
                    
            elif escolha == 7:
                personagem.sair()
            else:
                input('Opção Invalida! Por favor escolha uma ação do menu')    
            os.system("cls")        


import sys, os

class Tutorial:
    def tutorial_pt(ver_tutorial):
        os.system("cls")
        print("=-"*25)
        print("==================== TUTORIAL ====================")
        print("=-"*25)
        print('''Nesse jogo seu objetivo é sobreviver em uma ilha 
                 deserta, coletando itens para fugir e se alimentar 
                 enquanto tenta sobreviver as surpresas que essa 
                 ilha lhe reserva''')
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
        input("\nAperte ENTER para iniciar o jogo...")

    def tutorial_ing(ver_tutorial): #TRADUZIR TUTORIAL
        os.system("cls")
        print("=-"*25)
        print("==================== TUTORIAL ====================")
        print('''In this game your objective is to survive on an island.
                 deserted, collecting items to escape and feed
                 while trying to survive the surprises that this
                 island reserves for you''')
        print("=-"*25)
        input("\nPress ENTER to continue...")       
        os.system("cls")
        print("")
        print("The menu bellow represents the choices that can be made during the game.")
        print("=-"*25)
        print('''        [1] - EAT 🍗
        [2] - LOOK FOR FOOD 👀
        [3] - LOOK FOR ITENS 🎒
        [4] - HEAL UP 💊
        [5] - SLEEP 😴
        [6] - ESCAPE 🏃
        [7] - LEAVE THE GAME 🚪''')
        print("=-"*25)
        print("")
        input("\nPress ENTER to continue...")
        os.system("cls")
        
        print("The option [1] EAT make your health increase in 20 units")
        print("The option [2] LOOK FOR FOOD make your character look for food")
        print("The option [3] LOOK FOR ITENS make your character loof for itens")
        print("The option [4] HEAL UP make your character recovered the full life")
        print("The option [5] SLEEP make your character recovered your life in 10 units and pass the day")
        print("The option [6] ESCAPE you will try escape of the island")
        print("The option [7] LEAVE THE GAME show the credits and close the game")
        print("")
        input("\nPress ENTER to start the game...")

import random
import time, sys, os
from music import Musica
from banner import Banner


musicas = Musica()
banners = Banner()
os.system('cls')

danos = [20,20,20,20,40,40,100] #Lista de chance de danos com opçoes de 20, 40 e 100 de dano
comida = [1,1,1,1,1,2,2] #Lista de chance de achar comida 1 = Achar comida e 2 = Não achar comida
item = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,4] #Lista de chance de achar item, não achar nada ,achar remédio e achar o EasterEgg
mar = [40,40,40,40,40,100] #Dano causado pelo ataque no mar

   

class Character_ing:
    def __init__(self):
        self.__vida = 40 #Vida inicial do personagem
        self.__vidaMax = 100 #Vida máxima do personagem

        self.__fome = 50 #Fome inicial do personagem
        self.__fomeMax = 100 #Fome máxima do personagem

        self.__banana = 2 #Quantidade de comida inicial
        self.__bananaMax = 5 #Quantidade de comida máxima que o personagem carrega

        self.__itens = 0 #Quantidade de itens que o personagem inicia
        self.__itensMax = 3 #Quantidade máxima e necessária para o personagem fugir

        self.__remedio = 1 #Quantidade inicial de rémedios que o personagem carrega
        self.__remedioMax = 2 #Quantidade máxima de remédios que o personagem carrega

        self.__dia = 1 #A contagem dos dias se inicia no dia 1

    def comer_ing(self): #Função para a ação [1] COMER | As opçoes abaixo so funcionam quando a funçao for chamada
        if self.__banana>0: 
            if self.__vida<self.__vidaMax: 
                self.__vida += 20 #Se a quantidade de vida for menor que a quantidade de vida máxima o personagem ira ganhar 20 de vida
                
            if self.__fome<self.__fomeMax:
                if self.__fome>50:
                    self.__vida = self.__vidaMax #Se a quantidade de fome for maior que 50 a fome se encherá completamente
                    
                else:
                    self.__fome += 50 #Se a quantidade de fome for menor que 50 a fome encherá em mais 50 unidades
                    
            self.__banana -= 1 #Ao comer você perde 1 banana
            print("")  
            input("You ate a banana and regained your hunger and life") #Texto informativo sobre o que aconteceu
            
        else:
            print("") 
            input("You don't have any food, go out to find food") #Texto informativo sobre o que aconteceu   
        

    def procurar_comida_ing(self): #Função para a ação [2] PROCURAR COMIDA | As opçoes abaixo so funcionam quando a funçao for chamada
        achar_comida = random.choice(comida) #Variavel que escolhe aleatoriamente entre achar comida ou não achar nada
        
        if achar_comida == 1:
            print("")
            input("Did you find food without problems") #Texto informativo sobre o que aconteceu
            if self.__banana<5:  
                self.__banana += 1 #Adiciona uma banana na "mochila" do personagem
            else:
                input("But your backpack was already full of bananas so your search didn't do any good") #Texto informativo caso o personagem esteja com a mochila cheia de comida
            self.__fome -= 20 #Ao sair para buscar comida o personagem perde 20 de fome
            if self.__fome<0: #Se a fome for menor que 0 o personagem morre de fome
                        musicas.musica_gameover()
                        input("But...you starved to death")#Texto informativo sobre o que aconteceu  
                        os.system("cls") #Limpa o terminal    
                        banners.end_banner()
                        exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER

        else:
            print("")
            input("You couldn't find food on this quest")#Texto informativo sobre o que aconteceu 
            self.__fome -= 20 #Ao não conseguir achar comida o personagem também perde 20 de fome
            if self.__fome<0: #Se a fome for menor que 0 o personagem morrre de fome
                if self.__banana>0:                    
                        musicas.musica_gameover()
                        input("You worried a lot about looking for more food and starved because you forgot to eat") #Texto informativo sobre o que aconteceu 
                        os.system("cls") #Limpa o terminal
                        banners.end_banner()
                        exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER
                else:
                    musicas.musica_gameover()
                    input("You didn´t have food and starved to death") #Texto informativo sobre o que aconteceu 
                    os.system("cls") #Limpa o terminal
                    banners.end_banner()
                    exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER

    def procurar_itens_ing(self): #Função para a ação [3] PROCURAR ITENS | As opçoes abaixo so funcionam quando a funçao for chamada
        achar_item = random.choice(item) #Variavel que escolhe aleatoriamente se o personagem vai achar um item, não achar nada ou achar remédio
        
        if achar_item == 1:
            print("")
            print("You've spotted an item that can help you escape the island, but an angry group of monkeys is nearby.") #Texto informativo sobre o que aconteceu 
            print("You have the option to fight and try to get the item or run away, what will you do?") #Texto informativo sobre o que aconteceu 
            print('''
                
                [1] FIGHT 🥊 
                [2] RUN 🏃
            ''')#O jogador tem duas opções de escolha lutar ou fugir, a escolha afetará no jogo
            print("")
            coletar_item = int(input("Write your option : ")) #Input para o jogador escolher qual opção escolheu
            if coletar_item == 1:
                dano = random.choice(danos) #Variavel que escolhe aleatoriamente o dano que será recebido
                self.__vida-=dano #A vida do personagem é subtraida em relação ao dano sofrido
                print("")
                print(f"You suffered {dano} of damage") #Texto que informa quanto de dano o personagem sofreu
                if self.__vida<=0:
                    musicas.musica_gameover()
                    input("YOU RECEIVED A FATAL ATACK AND DIED") #Mensagem após o personagem tomar um dano critico e ficar sem vida
                    os.system("cls") #Limpa o terminal
                    banners.end_banner()
                    exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER
                else:
                    input("YOU DEFEATED THEM AND GOT THE ITEM") #Mensagem informativa caso o personagem saia vivo do combate
                    if self.__itens<3:
                        if self.__itens == 0:
                            print("")
                            input('Now you have a ROPE. It will be helpful in your escape from the island.')
                            self.__itens += 1 #Personagem adquire um item que é útil para a fuga
                        elif self.__itens ==1:
                            print("")
                            input('Now you have some WOODS. WOOD will be very useful along with ROPE in your escape from the island.')    
                            self.__itens += 1
                        elif self.__itens ==2:
                            print("")
                            input('You found a BED SHEET! This item is very useful to create a boat sail. hmmm i think you know what make with this itens, right!?')    
                            self.__itens += 1   
                    else:
                        input("But your figth wasn´t useful... Your backpack was full") #Texto informativo caso o personagem já esteja lotado de remédios
                    self.__fome -= 20 #Personagem perde 20 de fome 
                    if self.__fome<=0:
                        musicas.musica_gameover()                       
                        input("But... you starved to death") #Mensagem informativa caso o personagem morra de fome
                        os.system("cls") #Limpa o terminal
                        banners.end_banner()
                        exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER
            else:
                input("You ran and didn't took the item...\nBe brave in the next time") #Mensagem caso o jogador opte por fugir do combate
                self.__fome -= 20 #Personagem perde 20 de fome
                if self.__fome<=0:
                        musicas.musica_gameover()
                        input("You ran, but you starved to death") #Mensagem informativa caso o personagem morra de fom
                        os.system("cls") #Limpa o terminal
                        banners.end_banner()
                        exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER
        
        elif achar_item == 3: 
            print("")
            input("You was very lucky, you found a medicine") #Mensagem informativa caso o personagem ache um remédio
            self.__fome -= 20 #Personagem perde 20 de fome 
            if self.__remedio<self.__remedioMax:
                self.__remedio+=1 #Personagem adquire mais um remédio caso o espaço da mochila destino para remédios não esteja cheio
            else:
                input("You was very lucky, you found a medicine... but you was very unlucky because your backpack was full") #Texto informativo caso o personagem já esteja cheio de remédios
            if self.__fome<0:
                musicas.musica_gameover()                
                input("You was very lucky, you found a medicine... but you starved to death because you forgot to eat") #Mensagem informativa caso o personagem morra de fom
                os.system("cls") #Limpa o terminal
                banners.end_banner()
                exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER   
        elif achar_item == 4: #Easter Egg escondido, se encontrado ele eleva para 100% todos atributos do personagem , menos os itens que continuam a ser necessário para fugir da ilha.
            input('****Easter Egg**** Congratulations!! You found a soccer ball, his name will be NIQUE. Nique will be your partner on this journey, your suprements and stats are in the max stats now.')
            self.__fome = self.__fomeMax
            self.__remedio = self.__remedioMax
            self.__banana = self.__bananaMax
            self.__vida = self.__vidaMax

        else:
            input("You leave to look for itens and didnt find nothing") #Mensagem informativa caso o personagem não ache nenhum item
            self.__fome -= 20 #Personagem perde 20 de fome
            if self.__fome<=0:
                    musicas.musica_gameover()
                    input("You got really obsessed with items and forgot to eat so you ended up starving") #Mensagem informativa caso o personagem morra de fome
                    banners.end_banner()
                    exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER

    def medicar_ing(self): #Função para a ação [4] MEDICAR | As opçoes abaixo so funcionam quando a funçao for chamada
        if self.__remedio>0:
            self.__vida = self.__vidaMax #Ao se medicar a vida se restaura totalmente
            self.__remedio -=1 #A quantidade de remédio diminui em um


    def dormir_ing(self): #Função para a ação [5] DORMIR | As opçoes abaixo so funcionam quando a funçao for chamada
       # musica_sono()
        self.__dia +=1 #Dia avança em 1
        self.__fome -= 20 #Ao avançar o dia o personagem perde 20 de fome
        if self.__fome>0:
            if self.__vida<=80:
                self.__vida += 20 #Se a vida estiver menor que 80 o personagem recupera 20 de vida
                
            else:
                self.__vida = self.__vidaMax #Se a vida estiver maior que 80 a vida se regenera totalmente
            print("")
            input("You had a great night's sleep and regained some life") #Texto informativo caso o personagem consiga dormir sem morrer de fome
        else:
            print("")
            input("You managed to sleep, but due to your hunger you didn't have the strength to get up and ended up dying") #Texto informativo caso o personagem durma mas morra de fome
            banners.end_banner()
            musicas.musica_gameover()
            exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER

    def fugir_ing(self): #Função para a ação [6] FUGIR | As opçoes abaixo so funcionam quando a funçao for chamada
        if self.__itens == self.__itensMax:
            musicas.musica_win() 
            final = ("After an arduous fight against angry monkeys and hunger during this journey you finally managed to gather all the necessary items to build a small raft to escape. You awkwardly progressed fast and in building your raft you finally end with the anguish of dying alone, proud of your creation you stop and admire your incredible creation and put it in the sea. You say goodbye to the island remembering all the moments of struggle and fear you went through but you have a smile on your face after realizing that everything has passed and that now you will finally return to your normal life") 
            #Se o personagem estiver com os 3 itens ele conseguirá fugir da ilha            
            for l in list(final):
                print(l, end='')
                #O stdout só é atualizado quando há nova linha e como nós estamos mandando tudo na mesma é preciso forçar a atualização.
                sys.stdout.flush()
                time.sleep(0.05)
            input('Press ENTER...')           
            exit()

        else:
            if self.__itens == 0:
                print("")
                input("Since you didn't have any items to escape, you decided to try swimming until you found some land in sight.")
                input("When you start to get to a certain point you start having a lot of difficulty to swim due to the strong tide.")
                dano_mar = random.choice (mar)
                print(f"In this failed escape attempt you lost {dano_mar} of life")
                self.__vida -= dano_mar
                if self.__vida<=0:
                    input("And ended up drowning")
                    banners.end_banner()
                    musicas.musica_gameover
                else:
                    input("Even though you almost drowned, you stayed alive. It's better to think more about your next actions")

            if self.__itens == 1:
                print("")
                input("After finding a ROPE you were very optimistic and looked for some way to escape using only this single item")
                input("You dove into the sea with your ROPE, and started to see some good results swimming...")
                tubarao_aparece = int(input("When suddenly you were surprised by a shark swimming near you\n\nWhat are you going to do?\n[1] STAND STILL \n[2] RUN AWAY AS FAST AS POSSIBLE"))
                while tubarao_aparece!= 1 and tubarao_aparece!= 2:
                    tubarao_aparece = int(input("TYPE IT CORRECTLY!!!\nWhat are you going to do?\n[1] STAND STILL\n[2] RUN AWAY AS FAST AS POSSIBLE"))
                if tubarao_aparece == 1:
                    print("")
                    input("As much as it didn't seem like a good idea to stand still, it worked perfectly and the shark left. Be more careful with your decisions next time!")
                if tubarao_aparece == 2:
                    print("")
                    input("When trying to run away quickly you shook the water a lot, the shark got angry and swam after you")
                    dano_mar = random.choice (mar)
                    print(f"When trying to escape the shark you lost {dano_mar} of life")
                    self.__vida -= dano_mar

                    if self.__vida<=0:
                        input("After a long time trying to escape you end up getting tired and the shark catches you...")
                        banners.end_banner()
                        musicas.musica_gameover()
                    else:
                        input("After a lot of dedication on your escape you finally manage to escape the shark")
            if self.__itens == 2:
                print("")
                input("By joining the ROPE and the WOODS, an idea for your escape popped into your head and you quickly put it into practice.")
                input("You put the items together and created a raft, but when you tried to run away you ran into a problem...")
                input("Your raft didn't have a sail, so you couldn't move out of place and quickly got surrounded by a group of sharks.")
                tubarao_aparece = int(input("What are you going to do?\n\n[1] FIGHT AGAINST SHARKS \n[2] RUN AWAY"))
                while tubarao_aparece!= 1 and tubarao_aparece!= 2:
                    tubarao_aparece = int(input("TYPE IT CORRECTLY!!!\nWhat are you going to do?\n[1] FIGHT AGAINST SHARKS\n[2] RUN AWAY"))
                if tubarao_aparece == 1:
                    self.__vida = 0
                    input("So you had the stupid idea to fight them all... And you obviously ended up dying")
                    banners.end_banner()
                    musicas.musica_gameover()
                if tubarao_aparece == 2:
                    self.__itens = 0
                    input("Your escape was a success, until you realized that the raft you created with all the items you gathered were devoured by sharks.")

                        
    def sair_ing(self): #Função para a ação [7] SAIR DO JOGO | As opçoes abaixo so funcionam quando a funçao for chamada
        os.system("cls")
        print("=-"*52)
        print("\nThanks for playing!!!\nCreators Fábio Henrique - Thiago Roberto\nSpecial dedications to teachers Gabriel Lima and Gustavo Cervelin for their dedication and quality in teaching.\n") #Créditos
        print("=-"*52)
        input("Press ENTER to close the game")
        exit()
        
    def status_ing(self): #Função que mostra os itens e informações sobre o personagem 
        print(f"Day {self.__dia} 📅                        Medicines {self.__remedio}/{self.__remedioMax} 💊")
        print("")
        print(f"Life {self.__vida}/{self.__vidaMax} ❤️                    Hunger {self.__fome}/{self.__fomeMax} 🍗 \U0001F601")
        print("")
        print(f"Food {self.__banana}/{self.__bananaMax} 🍌                    Escape {self.__itens}/{self.__itensMax} 🏃")
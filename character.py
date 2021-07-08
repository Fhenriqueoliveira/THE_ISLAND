import random
import time, sys, os
from banner import Banner
from music import Musica

musicas = Musica()
banners = Banner()
os.system('cls')

danos = [20,20,20,20,40,40,100] #Lista de chance de danos com opçoes de 20, 40 e 100 de dano
comida = [1,1,1,1,1,2,2] #Lista de chance de achar comida 1 = Achar comida e 2 = Não achar comida
item = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,4] #Lista de chance de achar item, não achar nada ,achar remédio e achar o EasterEgg
mar = [40,40,40,40,40,100] #Dano causado pelo ataque no mar

   

class Character:
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

    def comer(self): #Função para a ação [1] COMER | As opçoes abaixo so funcionam quando a funçao for chamada
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
            input("Você comeu uma banana e recuperou sua fome e vida") #Texto informativo sobre o que aconteceu
            
        else:
            print("") 
            input("Você não tem mais comida, saia para procurar comida") #Texto informativo sobre o que aconteceu   
        

    def procurar_comida(self): #Função para a ação [2] PROCURAR COMIDA | As opçoes abaixo so funcionam quando a funçao for chamada
        achar_comida = random.choice(comida) #Variavel que escolhe aleatoriamente entre achar comida ou não achar nada
        
        if achar_comida == 1:
            print("")
            input("Você conseguiu achar comida sem problemas") #Texto informativo sobre o que aconteceu
            if self.__banana<5:  
                self.__banana += 1 #Adiciona uma banana na "mochila" do personagem
            else:
                input("Mas sua mochila ja estava cheia de bananas então sua busca não adiantou de nada") #TExto informativo caso o personagem esteja com a mochila cheia de comida
            self.__fome -= 20 #Ao sair para buscar comida o personagem perde 20 de fome
            if self.__fome<0: #Se a fome for menor que 0 o personagem morre de fome
                        musicas.musica_gameover()
                        input("Mas... acabou morrendo de fome antes de conseguir comer")#Texto informativo sobre o que aconteceu  
                        os.system("cls") #Limpa o terminal
                        banners.end_banner()    
                        input('Aperte o Enter para sair')
                        exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER

        else:
            print("")
            input("Você não conseguiu achar comida nessa busca")#Texto informativo sobre o que aconteceu 
            self.__fome -= 20 #Ao não conseguir achar comida o personagem também perde 20 de fome
            if self.__fome<0: #Se a fome for menor que 0 o personagem morrre de fome
                if self.__banana>0:                    
                        musicas.musica_gameover()
                        input("Você se preocupou muito em procurar mais comida e morreu de fome pois esqueceu de comer") #Texto informativo sobre o que aconteceu 
                        os.system("cls") #Limpa o terminal
                        banners.end_banner()    
                        input('Aperte o Enter para sair')
                        exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER
                else:
                    musicas.musica_gameover()
                    input("Você não tinha nenhuma comida e morreu de fome") #Texto informativo sobre o que aconteceu 
                    os.system("cls") #Limpa o terminal
                    banners.end_banner()    
                    input('Aperte o Enter para sair')
                    exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER

    def procurar_itens(self): #Função para a ação [3] PROCURAR ITENS | As opçoes abaixo so funcionam quando a funçao for chamada
        achar_item = random.choice(item) #Variavel que escolhe aleatoriamente se o personagem vai achar um item, não achar nada ou achar remédio
        
        if achar_item == 1:
            print("Você avistou um item que pode ajudar a fugir da ilha, porém um um grupo furioso de macacos está por perto") #Texto informativo sobre o que aconteceu 
            print("Você tem a opção de lutar e tentar pegar o item ou fugir, o que irá fazer?") #Texto informativo sobre o que aconteceu 
            print('''
                
                [1] LUTAR 🥊 
                [2] FUGIR 🏃
            ''')#O jogador tem duas opções de escolha lutar ou fugir, a escolha afetará no jogo
            print("")
            coletar_item = int(input("Digite sua opção : ")) #Input para o jogador escolher qual opção escolheu
            if coletar_item == 1:
                dano = random.choice(danos) #Variavel que escolhe aleatoriamente o dano que será recebido
                self.__vida-=dano #A vida do personagem é subtraida em relação ao dano sofrido
                print("")
                print(f"Você sofreu {dano} de dano") #Texto que informa quanto de dano o personagem sofreu
                if self.__vida<=0:
                    musicas.musica_gameover()
                    input("VOCÊ SOFREU UM ATAQUE FATAL E MORREU") #Mensagem após o personagem tomar um dano critico e ficar sem vida
                    os.system("cls") #Limpa o terminal
                    banners.end_banner()    
                    input('Aperte o Enter para sair')
                    exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER
                else:
                    input("VOCÊ DERROTOU O GRUPO E AINDA PEGOU O ITEM") #Mensagem informativa caso o personagem saia vivo do combate
                    if self.__itens<3:
                        if self.__itens == 0:
                            input('Agora você tem uma CORDA. Ela será utíl na sua fuga da ilha.')
                            self.__itens += 1 #Personagem adquire um item que é útil para a fuga
                        elif self.__itens ==1:
                            input('Agora você tem algumas MADEIRAS. A MADEIRA será muito util junto com a CORDA em sua fuga da ilha.')    
                            self.__itens += 1
                        elif self.__itens ==2:
                            input('Você acho um LENÇOL! Ótimo para criar uma vela... hummm acho que sabe o que fazer com todos esses itens né!?')    
                            self.__itens += 1   
                    else:
                        input("Mas sua luta pelo item foi em vão... Sua mochila já estava cheia e você não conseguiu carregar mais nada") #Texto informativo caso o personagem já esteja lotado de remédios
                    self.__fome -= 20 #Personagem perde 20 de fome 
                    if self.__fome<=0:
                        musicas.musica_gameover()                       
                        input("Mas... acabou morrendo de fome") #Mensagem informativa caso o personagem morra de fome
                        os.system("cls") #Limpa o terminal
                        banners.end_banner()    
                        input('Aperte o Enter para sair')
                        exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER
            else:
                input("Você fugiu e não pegou o item...\nSeja mais corajoso na próxima") #Mensagem caso o jogador opte por fugir do combate
                self.__fome -= 20 #Personagem perde 20 de fome
                if self.__fome<=0:
                        musicas.musica_gameover()
                        input("Mesmo fugindo a morte chegou para você, que acabou morrendo de fome") #Mensagem informativa caso o personagem morra de fom
                        os.system("cls") #Limpa o terminal
                        banners.end_banner()    
                        input('Aperte o Enter para sair')
                        exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER
        
        elif achar_item == 3: 
            print("")
            input("Você deu muita sorte e conseguiu achar um remédio") #Mensagem informativa caso o personagem ache um remédio
            self.__fome -= 20 #Personagem perde 20 de fome 
            if self.__remedio<self.__remedioMax:
                self.__remedio+=1 #Personagem adquire mais um remédio caso o espaço da mochila destino para remédios não esteja cheio
            else:
                input("Por mais sortudo que você seja ao achar o remédio você foi azarado de não ter espaço suficiente para guarda-lo") #Texto informativo caso o personagem já esteja cheio de remédios
            if self.__fome<0:
                musicas.musica_gameover()                
                input("Mesmo com toda sua sorte você morreu de fome pois esqueceu de comer") #Mensagem informativa caso o personagem morra de fom
                os.system("cls") #Limpa o terminal
                banners.end_banner()    
                input('Aperte o Enter para sair')
                exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER   
        elif achar_item == 4: #Easter Egg escondido, se encontrado ele eleva para 100% todos atributos do personagem , menos os itens que continuam a ser necessário para fugir da ilha.
            print("")
            input('****Easter Egg**** Parabéns!! Você encontrou uma bola de futebol, seu nome será NIQUE. Nique vai ser seu companheiro nesse desafio, e ele eleva seus suprimentos em 100% ! ')
            self.__fome = self.__fomeMax
            self.__remedio = self.__remedioMax
            self.__banana = self.__bananaMax
            self.__vida = self.__vidaMax

        else:
            print("")
            input("Você saiu para procurar itens e não achou nada") #Mensagem informativa caso o personagem não ache nenhum item
            self.__fome -= 20 #Personagem perde 20 de fome
            if self.__fome<=0:
                    musicas.musica_gameover()
                    input("Você ficou muuito obcecado por itens e esqueceu de comer então acabou morrendo de fome") #Mensagem informativa caso o personagem morra de fome
                    banners.end_banner()    
                    input('Aperte o Enter para sair')
                    exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER

    def medicar(self): #Função para a ação [4] MEDICAR | As opçoes abaixo so funcionam quando a funçao for chamada
        if self.__remedio>0:
            self.__vida = self.__vidaMax #Ao se medicar a vida se restaura totalmente
            self.__remedio -=1 #A quantidade de remédio diminui em um


    def dormir(self): #Função para a ação [5] DORMIR | As opçoes abaixo so funcionam quando a funçao for chamada
       # musica_sono()
        self.__dia +=1 #Dia avança em 1
        self.__fome -= 20 #Ao avançar o dia o personagem perde 20 de fome
        if self.__fome>0:
            if self.__vida<=80:
                self.__vida += 20 #Se a vida estiver menor que 80 o personagem recupera 20 de vida
                
            else:
                self.__vida = self.__vidaMax #Se a vida estiver maior que 80 a vida se regenera totalmente
            print("")
            input("Você teve uma ótima noite de sono e recuperou um pouco de vida") #Texto informativo caso o personagem consiga dormir sem morrer de fome
        else:
            print("")
            input("Você conseguiu dormir, mas devido a sua fome você não conseguiu ter forças para se levantar e acabou morrendo") #Texto informativo caso o personagem durma mas morra de fome
            banners.end_banner()    
            input('Aperte o Enter para sair')
            musicas.musica_gameover()
            exit() #Mensagem de GAME OVER e depois o jogo fecha ao apertar ENTER

    def fugir(self): #Função para a ação [6] FUGIR | As opçoes abaixo so funcionam quando a funçao for chamada
        if self.__itens == self.__itensMax:
            musicas.musica_win() 
            final = ("Após uma árdua luta contra macacos furiosos e contra a fome durante essa jornada você finalmente conseguiu juntar todos os itens necessários para construir uma pequena jangada para fugir.Desengonçadamente você progrediu rápido e na construção da sua jangada vc finalmente  termina com a angustia de morrer sozinho, orgulhoso de sua criação você para e admira um pouco sua incrivel criação e o coloca no mar. Você se despede da ilha relembrando todo os momentos de luta e medo que passou mas esboça um sorriso no rosto após perceber que tudo já passou e que agora você finalmente voltará para sua vida normal, e consiguirá levar sua filha ao altar") 
            #Se o personagem estiver com os 3 itens ele conseguirá fugir da ilha            
            for l in list(final):
                print(l, end='')
                #O stdout só é atualizado quando há nova linha e como nós estamos mandando tudo na mesma é preciso forçar a atualização.
                sys.stdout.flush()
                time.sleep(0.03)
            input('Aperte ENTER...')           
            exit()

        else:
            if self.__itens == 0:
                print("")
                input("Como você não tinha itens para fugir, você decidiu tentar nadar até achar algum resquício de terra a vista.")
                input("Ao começar a chegar em um certo ponto você começa a ter muita dificuldade para nadar devido a forte maré")
                dano_mar = random.choice (mar)
                print(f"Nessa tentativa falha de fuga você perdeu {dano_mar} de vida")
                self.__vida -= dano_mar
                if self.__vida<=0:
                    input("E acabou morrendo afogado")
                    banners.end_banner()
                else:
                    input("Apesar de quase ter morrido afogado você se manteve vivo. É melhor pensar mais nas suas próximas ações")

            if self.__itens == 1:
                print("")
                input("Após ter achado uma CORDA você foi bem otimista e buscou alguma maneira de fugir usando apenas esse único item")
                input("Você mergulhou no mar com sua CORDA, e começou a ver algum bom resultado nadando...")
                tubarao_aparece = int(input("Quando derrepente foi surpreendido por um tubarão nadando perto de você\n\n O que ira fazer?\n[1] FICAR PARADO \n[2] FUGIR O MAIS RÁPIDO POSSÍVEL "))
                while tubarao_aparece!= 1 and tubarao_aparece!= 2:
                    tubarao_aparece = int(input("DIGITE CORRETAMENTE!!!\n O que ira fazer?\n[1] FICAR PARADO\n[2] FUGIR O MAIS RÁPIDO POSSÍVEL"))
                if tubarao_aparece == 1:
                    print("")
                    input("Por mais que não parecesse uma boa ideia ficar parado, isso funcionou perfeitamente e o tubarão foi embora. Tome mais cuidado com suas decisões nas próximas vezes!")
                if tubarao_aparece == 2:
                    print("")
                    input("Ao tentar fugir rapidamente você agitou muito a água, o tubarão ficou irritado e nadou atrás de você")
                    dano_mar = random.choice (mar)
                    print(f"Ao tentar fugir do tubarão você perdeu {dano_mar} de vida")
                    self.__vida -= dano_mar

                    if self.__vida<=0:
                        input("Após muito tempo tentando fugir você acaba cansando e o tubarão te alçança...")
                        banners.end_banner()
                    else:
                        input("Depois de muita dedicação na sua fuga você finalmente consegue escapar do tubarão")
                        #mas acabou voltando a estaca 0, perdendo todos os itens
            if self.__itens == 2:
                print("")
                input("Ao juntar a CORDA e as MADEIRAS, uma ideia para sua fuga surgiu em sua cabeça e você foi rapidamente bota-la em prática.")
                input("Você uniu os itens e criou uma jangada, mas ao tentar fugir se deparou com um problema...")
                input("Sua jangada não tinha uma vela, então você não conseguia sair do lugar e rapidamente foi cercado por um grupo de tubarões")
                tubarao_aparece = int(input("O que ira fazer?\n\n[1] LUTAR CONTRA OS TUBARÕES \n[2] FUGIR "))
                while tubarao_aparece!= 1 and tubarao_aparece!= 2:
                    tubarao_aparece = int(input("DIGITE CORRETAMENTE!!!\n O que ira fazer?\n[1] LUTAR CONTRA OS TUBARÕES\n[2] FUGIR"))
                if tubarao_aparece == 1:
                    self.__vida = 0
                    input("Então você teve a estúpida idéia de lutar contra todos eles... E obviamente acabou morrendo")
                    banners.end_banner()
                if tubarao_aparece == 2:
                    self.__itens = 0
                    input("Sua fuga foi um sucesso, até perceber que a jangada que vc criou com todos os itens que você juntou foram devorados pelos tubarões")

                        
    def sair(self): #Função para a ação [7] SAIR DO JOGO | As opçoes abaixo so funcionam quando a funçao for chamada
        os.system("cls")
        print("=-"*52)
        print("\nObrigado por jogar!!!\nCriadores Fábio Henrique - Thiago Roberto\nDedicações especiais aos professores Gabriel Lima e Gustavo Cervelin pela dedicação e qualidade no ensino.\n") #Créditos
        print("=-"*52)
        input("Aperte ENTER para fechar o jogo")
        exit()
        
    def status(self): #Função que mostra os itens e informações sobre o personagem 
        print(f"Dia {self.__dia} 📅                        Remédios {self.__remedio}/{self.__remedioMax} 💊")
        print("")
        print(f"Vida {self.__vida}/{self.__vidaMax} ❤️                    Fome {self.__fome}/{self.__fomeMax} 🍗 \U0001F601")
        print("")
        print(f"Comida {self.__banana}/{self.__bananaMax} 🍌                    Fugir {self.__itens}/{self.__itensMax} 🏃")
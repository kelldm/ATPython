import random

#Definir variaveis de jogo: pontuacao, perguntas, perguntas feitas
#loop com 5 perguntas, anotando a pontuacao(verificando se acertou a pergunta) e se acertou 5, faz o loop de novo
#menu
#perguntas nao podem se repetir entre jogos
#lista com perguntas já feitas.

banco_perguntas = [
            {
                "pergunta": "Qual é o maior animal terrestre?",
                "alternativas": ["a) Elefante africano", "b) Girafa", "c) Hipopótamo", "d) Gorila"],
                "resposta_correta": "a"
            },
            {
                "pergunta": "Qual é o animal mais veloz do mundo?",
                "alternativas": ["a) Guepardo", "b) Falcão-peregrino", "c) Leão", "d) Antílope"],
                "resposta_correta": "b"
            },
            {
                "pergunta": "Qual é o único mamífero capaz de voar?",
                "alternativas": ["a) Morcego", "b) Pássaro", "c) Esquilo", "d) Serpente"],
                "resposta_correta": "a"
            },
            {
                "pergunta": "Qual é o animal com o maior cérebro em proporção ao tamanho do corpo?",
                "alternativas": ["a) Elefante", "b) Golfinho", "c) Humano", "d) Cachorro"],
                "resposta_correta": "b"
            },
            {
                "pergunta": "Qual é o animal que tem o maior tempo de gestação?",
                "alternativas": ["a) Elefante", "b) Baleia", "c) Girafa", "d) Ornitorrinco"],
                "resposta_correta": "a"
            },
            {
                "pergunta": "Qual é o animal mais venenoso do mundo?",
                "alternativas": ["a) Cobra", "b) Aranha", "c) Medusa", "d) Vespa"],
                "resposta_correta": "d"
            },
            {
                "pergunta": "Qual é o único animal que não consegue pular?",
                "alternativas": ["a) Elefante", "b) Cachorro", "c) Gato", "d) Elefante-marinho"],
                "resposta_correta": "a"
            },
            {
                "pergunta": "Qual é o animal com a mordida mais forte do mundo?",
                "alternativas": ["a) Tubarão-branco", "b) Crocodilo", "c) Hiena", "d) Leão"],
                "resposta_correta": "b"
            },
            {
                "pergunta": "Qual é o animal mais resistente do mundo?",
                "alternativas": ["a) Tardígrado", "b) Barata", "c) Camelo", "d) Urso"],
                "resposta_correta": "a"
            },
            {
                "pergunta": "Qual é o animal que dorme mais tempo por dia?",
                "alternativas": ["a) Morcego", "b) Gato", "c) Preguiça", "d) Urso"],
                "resposta_correta": "c"
            },
            {
                "pergunta": "Qual é o animal que tem o maior número de dentes?",
                "alternativas": ["a) Tubarão", "b) Golfinho", "c) Elefante", "d) Leão"],
                "resposta_correta": "a"
            },
            {
                "pergunta": "Qual é o animal mais inteligente depois dos humanos?",
                "alternativas": ["a) Macaco", "b) Golfinho", "c) Chimpanzé", "d) Elefante"],
                "resposta_correta": "b"
            },
            {
                "pergunta": "Qual é o único mamífero que pode voar de verdade?",
                "alternativas": ["a) Morcego", "b) Pássaro", "c) Esquilo", "d) Serpente"],
                "resposta_correta": "a"
            },
            {
                "pergunta": "Qual é o animal mais lento do mundo?",
                "alternativas": ["a) Caracol", "b) Tartaruga", "c) Lesma", "d) Preguiça"],
                "resposta_correta": "d"
            },
            {
                "pergunta": "Qual é o animal com o maior número de patas?",
                "alternativas": ["a) Aranha", "b) Centopeia", "c) Escorpião", "d) Sapo"],
                "resposta_correta": "b"
            }
        ]
perguntas_feitas = [] #Lista para armazenar as perguntas já feitas
pontuacao = 0 #Pontuação do jogador na rodada atual
pontuacao_total = 0 #Pontuação total do jogador em todas as rodadas
fase = 1 #Fase atual do jogo

def selecionar_pergunta():
    """
    Seleciona uma pergunta aleatória que ainda não foi feita no jogo atual.
    Return:
    dict: Um dicionário representando uma pergunta selecionada.
    """
    for pergunta in banco_perguntas:
            if pergunta not in perguntas_feitas:
                perguntas_feitas.append(pergunta)
                return pergunta

def selecionar_perguntas():
    #List Comprehension
    """
    Seleciona 5 perguntas aleatórias, garantindo que não sejam repetidas entre si nem com perguntas já feitas.
    Return:
    list: Uma lista de dicionários representando as perguntas selecionadas.
    """
    return [selecionar_pergunta() for _ in range(5)]

#jogar pode retornar true ou false caso a pontuacao nao seja 5, ou a main pode verificar e decidir se chama jogar de novo
def jogar():
    """
    Inicia o jogo, apresentando perguntas ao jogador e registrando sua pontuação.
    """

    global pontuacao
    global pontuacao_total
    global fase
    
    perguntas = selecionar_perguntas()
        
    for pergunta in perguntas:
        print("-------------------------------------------")
        print(pergunta["pergunta"])
        print("-------------------------------------------")
        for alternativa in pergunta["alternativas"]:
                
            print(alternativa)
            
        resposta = input("Escolha a alternativa correta (a, b, c ou d): ").lower()
              
                      
        if resposta == pergunta["resposta_correta"]:
            print("***********************")
            print("* Resposta correta! *")
            print("***********************\n")
            pontuacao += 1    
                  
        else:
            print("***********************")
            print("* Resposta incorreta!*")
            print("***********************\n")

    print("Pontuação desta rodada:", pontuacao)
        
    if pontuacao == 5:
        pontuacao_total += pontuacao
        if pontuacao_total == 15:
            print("Pontuação total: ", pontuacao_total)
            
            print("***********************")
            print("Parabéns! você zerou o jogo!!")
            print("***********************")
            
            return    
        
        print("\n---------------------------------------------------------------------")
        print(f"Parabéns! Você acertou todas as perguntas! Iniciando fase {fase}/3")
        print("---------------------------------------------------------------------")
        fase +=1
        pontuacao = 0 
        #usei recursao sem querer :P
        jogar()
    else:
        pontuacao_total += pontuacao
        print("-------------------------------------------")
        print("GAME OVEEER! Pontuação total alcançada:", pontuacao_total)
        print("-------------------------------------------")
        return
    

def main():
    """
    Função principal que executa o jogo 
    """
    #menu
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("* SEJA BEM VINDO AO JOGO TRIVIA !!! VAMOS COMEÇAR? *")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    jogar()
    
    
main()

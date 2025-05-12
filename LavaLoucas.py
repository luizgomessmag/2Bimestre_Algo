import time

#variáveis globais
ligado=False
tempo=0
temperatura =0


def ligar(novoTempo,novaTemperatura):
    global ligado, tempo, temperatura
    if not ligado:
        ligado=True
        tempo=novoTempo
        temperatura=novaTemperatura
        print(f"A lava Louças foi ligada por {tempo} segundos em {temperatura} graus")
        iniciarCronometro(tempo)
        desligar()
    else:
        print(f"A lava louças já está ligada")

def desligar():
    global ligado
    if ligado:
        ligado=False
        print("Lava Louças Desligou")
    else:
        print("Lava Louças já está desligado")

def iniciarCronometro(segundos):
    while segundos>=0:
        print(f"Tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos-=1
    print("\nTempo Esgotado")

#funçoes lava louças

def vidro():
    print("Limpeza de Vidro")
    ligar(120,100)
    print("Os vidros estão limpos!")

def plastico():
    print("Limpeza de Plástico")
    ligar(60,21)
    print("Os Plásticos estão limpos!")

def metal():
    print("Limpeza de Metal")
    ligar(120,30)
    print("Os Metais estão limpos!")

#rodando as funções
escolha=input("escolha o modo(vidro, plastico, metal) ")

if escolha =="vidro":
    vidro()
elif escolha == "plastico":
    plastico()
else:
    metal()
import time

#variáveis globais
ligado=False
tempo=0
potencia =0

def ligar(novoTempo,novaPotencia):
    global ligado, tempo, potencia
    if not ligado:
        ligado=True
        tempo =novoTempo
        potencia=novaPotencia
        print(f"O microondas foi ligado por {tempo} segundos na potência {potencia}")
        iniciarCronometro(tempo)
        desligar()
    else:
        print("O microondas já está ligado")

def desligar():
    global ligado
    if ligado:
        ligado=False
        print("PI! PI! PI! ... PI! PI! PI! ... PI! PI! PI!")
        print("Microondas Desligou")
    else:
        print("Microondas já está desligado")

def status():
    if ligado:
        print(f"tempo: {tempo} segundos \n Potência: {potencia}")
    else:
        print("Desligado")

def iniciarCronometro(segundos):
    while segundos>=0:
        print(f"Tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos-=1
    print("\nTempo Esgotado")
    


#funçoes microondas

def pipoca():
    ligar(30,100)
    #print("Sua pipoca está pronta")

def descongelar(tipo):
    if tipo=="frango":
        ligar(60,50)
    elif tipo=="carne":
        ligar(60,70)



#rodando as funções

pipoca()

descongelar("frango")
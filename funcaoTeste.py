# tabuada do 7

# print("tabuada do 7")
# for i in range(0,11):
#     print("7 x",i,"=", 7*i)


# tabuada do 8

# print("tabuada do 8")
# for i in range(0,11):
#     print("8 x",i,"=", 8*i)

# tabuada do 9

# print("tabuada do 9")
# for i in range(0,11):
#     print("9 x",i,"=", 9*i)

#-----------------------------------------------------------------------------------------

#tabuada com função:

# def tabuada(numero):
#     print(f"tabuada do:{numero}:")
#     for i in range(1,11):
#         print(f"{numero} x {i} = {numero*i}")

# # exibindo as tabuadas:
# # tabuada(7)
# # tabuada(8)
# # tabuada(9)

#-----------------------------------------------------------------------------------------

#tabuada escalável em python
# def tabuada(base):
#     print(f"tabuada do:{base}:")
#     for j in range(1,11):
#         print(f"{base} x {j} = {base*j}")
#     print()#espaço extra para separar as tabuadas

# #gerar tabuadas de 1 a 100
# for i in range(1,101):
#     tabuada(i)

#-----------------------------------------------------------------------------------------
#tabuada personalizada
def tabuadaPersonalizada(base,inicio,fim):
    print(f"tabuada do:{base} de {inicio} a {fim}:")
    for j in range(inicio,fim+1):
        print(f"{base} x {j} = {base*j}")
    print()#espaço extra para separar as tabuadas

tabuadaPersonalizada(7,1,10)#tabuada do 7 de 1 a 10
tabuadaPersonalizada(5,5,15)#tabuada do 5 de 5 a 15


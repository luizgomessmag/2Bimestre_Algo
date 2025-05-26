compras=[]

opcao=""

while opcao!="finalizar":

    opcao=input("o que você deseja fazer? (adicionar, remover ou finalizar)\n")

    if opcao =="adicionar":
        compras.append(input(str("insira um produto\n")))
        print(compras)
    elif opcao == "remover":
        if len(compras)!=0:
            print(compras)
            compras.remove(input(str("remova um item\n")))
            print(compras)
        else:
            print("A lista de compras está vazia")
    elif opcao=="finalizar":
        print("Compra finalizada, suas compras foram")
        print(compras)
    else:
        print("Opção incorreta")











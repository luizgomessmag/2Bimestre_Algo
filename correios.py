
pacotes =( ("ABC123","Enviado"), ("XYZ789","Recebido"), ("DEF456","Em Trânsito"),("JKL321","Enviado"), ("MNO654","Recebido"), ("PQR987","Em Trânsito"), ("STU741","Enviado"))

contEnviado = 0
contTransito = 0
contRecebido = 0

codigoEmTransito = []

for pacote in pacotes:
    if pacote[1]=="Enviado":
        contEnviado+=1
    elif pacote[1]=="Recebido":
        contRecebido+=1
    else:
        contTransito+=1
        codigoEmTransito.append(pacote[0])

print(f"A quantidade de itens enviados é: {contEnviado}")
print(f"A quantidade de itens em trânsito é: {contTransito}")
print(f"A quantidade de itens recebidos é: {contRecebido}")

print(f"O código dos pacotes em trânsito são: {codigoEmTransito}")

def verificaStatus(codigo):
    for pacote in pacotes:
        if codigo==pacote[0]:
            return "O produto de código " + codigo +  " está: " + pacote[1]
    return "O produto de código " + codigo + " não está listado"

print(verificaStatus("ABC123"))
print(verificaStatus("SMAG"))

codigos = []
codigosOrdenados=[]

for pacote in pacotes:
    codigos.append(pacote[0])
codigosOrdenados= sorted(codigos)

pacotesOrdenados = []

for codigo in codigosOrdenados:
    for pacote in pacotes:
        if codigo==pacote[0]:
            pacotesOrdenados.append(pacote)

print(f"Os pacotes em ordem são:\n{pacotesOrdenados}")



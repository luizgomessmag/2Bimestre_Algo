numero= (5, 8, 12, 8, 7, 8, 3)
#para ser uma tupla precisa estar entre parênteses!

print (f"Tupla original: {numero}")
#imprimindo para o usuário a tupla original, sem manipulações

print(f"Tamanho do tupla: {len(numero)}")

print("acessando pelo índice", numero[2])
#escolhendo qual item será mostrado através do índice

print(f"Fazendo um slice do 2 ao 5: {numero[2:5]}")
#O slice não pega o ultimo item definido no recorte

print(f"Quantas vezes o número 8 repete {numero.count(8)} vezes")
#O count conta quantas vezes o número se repete

print(f"O numero 7 aparece a primeira vez no índice: {numero.index(7)}")
#O index

menorValor = min(numero)
print(f"O menor número da tupla é {menorValor}")

print(f"O maior valor da tupla é {max(numero)}")

print(f"A soma dos itens da tupla é {sum(numero)}")

print(f"A tupla em ordem fica {sorted(numero)}")

print(f"O número 4 está na tupla??? {4 in numero}")

numero2 = (15, 20)
tupla_concatenada=numero+numero2
print(f"a concatenação das tuplas 1 e 2 resulta na nova tupla:{tupla_concatenada}")


tupla_duplicada=numero*2

print(tupla_duplicada)

def calculadora_imc(pessoa):
    imc= pessoa["peso"]/ (pessoa["altura"]*pessoa["altura"])
    resultado = "o imc de "+pessoa["nome"]+" é "+str(round(imc, 2))
    #comando ternário:
    saudavel = 18.5 < imc < 25
    return {
        "nome": pessoa["nome"],
        "imc": imc,
        "resultado": resultado,
        "saudavel": saudavel,
    } 
pessoa1={
    "nome": input("digite seu nome"),
    "peso": float(input("digite seu peso")),
    "altura": float(input("digite sua altura")),

}
print(calculadora_imc(pessoa1))












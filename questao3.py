numero = int(input(""))

if 10 <= numero <= 99:
    dezena, unidade = divmod(numero, 10)
    if dezena % 2 == 0 and unidade % 2 == 0:
        mensagem = "Nenhum dígito é ímpar."
    elif dezena % 2 == 1 and unidade % 2 == 1:
        mensagem = "Os dois dígitos são ímpares."
    else:
        mensagem = "Apenas um dígito é ímpar."
    print(mensagem)
else:
    print("")

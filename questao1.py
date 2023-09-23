def estado_civil(nome, estado):
    if estado == 2:
     print(len(nome))
    else:
        print(len(nome + str(input("").strip())))

nome = str(input("")).strip()
estado = int(input(""))
estado_civil(nome, estado)

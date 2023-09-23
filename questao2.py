num = int(input(""))
d1 = num // 100 % 10
d2 = num // 10 % 10
d3 = num // 1 % 10

def eh_par():
    if not (num >= 100 and num <= 999):
        return "0"
    if d1 % 2 == 0:
        return pares + 1
    if d2 % 2 == 0:
        return pares + 1
    if d3 % 2 == 0:
        return pares + 1
    else:
        return "0"

pares = 0
pares = pares + 1
resultado = eh_par()
print(resultado)


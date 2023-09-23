def ordernar(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

num1 = float(input(""))
num2 = float(input(""))
num3 = float(input(""))

num_ordenados = ordernar(num1, num2, num3)
for numeros in num_ordenados:
    print(int(numeros))

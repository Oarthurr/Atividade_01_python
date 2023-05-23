n1 = int(input("Informe o primeiro número: "))

n2 = int(input("Informe o segundo número: "))

n3 = int(input("Informe o terceiro número: "))

if n1 <= n2 and n1 <= n3:
    menor = numero1

elif n2 <= n1 and n2 <= n3:
    menor = n2

else:
    menor = n3
print("O menor número é o número:", menor)
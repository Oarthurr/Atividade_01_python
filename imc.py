p = float(input("Digite o seu peso em kg: "))

h = float(input("Digite a sua altura em metros: "))

imc = p / h **2

if imc < 18.5:
    diagnostico = "Abaixo do peso"
elif imc < 25:
    diagnostico = "O peso está normal"
elif imc < 30:
    diagnostico = "Sobrepeso"
elif imc < 35:
    diagnostico = "Obesidade classe I"
elif imc < 40:
    diagnostico = "Obesidade classe II"
else:
    diagnostico = "Obesidade classe III"

print("Seu IMC é de:", imc)

print("Diagnóstico:", diagnostico)

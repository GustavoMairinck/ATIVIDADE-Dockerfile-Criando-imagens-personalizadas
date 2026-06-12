def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por zero."
    return a / b


print("=== Calculadora Docker ===")

numero1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, * ou /): ")
numero2 = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = somar(numero1, numero2)
elif operacao == "-":
    resultado = subtrair(numero1, numero2)
elif operacao == "*":
    resultado = multiplicar(numero1, numero2)
elif operacao == "/":
    resultado = dividir(numero1, numero2)
else:
    resultado = "Operação inválida."

print(f"Resultado: {resultado}")
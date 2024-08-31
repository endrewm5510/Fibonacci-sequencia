def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Entrada do usuário
try:
    usuario = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    if is_fibonacci(usuario):
        print(f"O número {usuario} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {usuario} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
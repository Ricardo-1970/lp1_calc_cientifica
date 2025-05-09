# Passo 1: definir funções para a realização das operações
def adicionar(n1,n2):
    """Retorna a soma de dois números."""
    return n1 + n2

def subtrair(n1,n2):
    """Retorna a diferença entre dois números."""
    return n1 - n2

def multiplicar(n1,n2):
    """Retorna o produto de dois números."""
    return n1 * n2

def dividir(n1,n2):
    """Retorna o quociente da divisão de dois números."""
    return n1 / n2
# Passo 2: solicitar ao usuário que insira os números e operações
num1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))
# Passo 3: Realizar a operação correspondente
if operador == '+':
    resultado = adicionar(num1,num2)
elif operador =='-':
    resultado = subtrair(num1,num2)    
elif operador =='*':
    resultado = multiplicar(num1,num2)
elif operador =='/':
    resultado = dividir(num1,num2)
else:
    print("Operador inválido!")
    resultado = None
# Passo 3: exibir o resultado
if resultado is not None:
    print(f"O resultado é: {resultado}") 
           


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

try:
    num1_str = input("Digite o primeiro número: ")
    operador = input("Digite o operador (+, -, *, /): ")
    num2_str = input("Digite o segundo número: ")

    # Passo 1: verificar se os números inseridos são válidos.
    if not num1_str.replace('.','',1).isdigit() or not num2_str.replace('.','',1).isdigit():
        raise ValueError("Por favor, insira números válidos.")
    else:
        num1 = float(num1_str)
        num2 = float(num2_str)

        # Passo 2: verificar se o operador inserido é válido.
        if operador in ['+','-','*','/']:
            # Passo 4: chamar a função correspondente.
            if operador == '+':
                resultado = adicionar(num1,num2)
            elif operador == '-':
                resultado = subtrair(num1,num2)
            elif operador == '*':
                resultado = multiplicar(num1,num2)    
            elif operador == '/':
                #considerar a divisão por zero aqui.
                if num2 == 0:
                    raise ZeroDivisionError("Não é possível dividir por zero.")
                else:
                    resultado = dividir(num1,num2)
            # Passo 5: exibir o resultado.
            print(f"O resultado é:{resultado}") 
        else:
            # Passo 3: exibir mensagens de erro apropriadas.
            raise ValueError("Operador inválido. Use: +, -, * ou /.")
        

except ValueError as e:
    print(f"Erro:{e}") 
except ZeroDivisionError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

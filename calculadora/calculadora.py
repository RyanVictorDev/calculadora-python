# Importando a biblioteca difflib para fazer comparações de strings
import difflib

# criando a função comparar para assim fazer a comparaçao entre a escolha do usuário e as opções
def comparar(decisao, opcoes):
    escolha = difflib.get_close_matches(decisao, opcoes, n=1)
    if escolha:
        return escolha[0]
    else:
        return None
    
# criando a função de chamada da calculadora
def calculadora():
    # lista de opções
    opcoes = ["soma", "subtracao", "multiplicacao", "divisao"]

    print("Bem-vindo(a) a calculadora! o que deseja?\n - Soma?\n - Subtração?\n - Multiplicação?\n - Divisão?")

    decisao = str(input("Escreva aqui a sua escolha:"))

    # chamada da função com o valor sendo colocado na variável "resultado"
    resultado = comparar(decisao, opcoes)

    if resultado:
        print(f"Então você quer {resultado}!")
    else:
        print("Desculpe, não entendi sua escolha.")

    match resultado:
        case "soma":
            calc_soma()
        
        case "subtracao":
            calc_subtracao()

        case "multiplicacao":
            calc_multiplicacao()

        case "divisao":
            calc_divisao()

        case _:
            print("Desculpas, houve um erro..")
            calculadora()

    
# criando a função de soma
def calc_soma():
    numeros = 0
    soma = 0
    print("caso deseje cancelar ou finalizar, digite '0.001'\n")
    while numeros != 0.001:
        try:
            numeros = float(input("Adicione o numero que quer somar.\n"))
            soma = soma + numeros
            print(f"Resultado: {soma}\n")
        
        except ValueError:
            print("Desculpe, houve um erro. Tente novamente")
            print(f"Aqui o resultado antes do erro: {soma}\n")
            calc_soma()
    
    print(f"Resultado final: {soma}")
    calculadora()

# criando a função de subtração
def calc_subtracao():
    numeros = 0
    print("caso deseje cancelar ou finalizar, digite '0.001'\n")
    while numeros != 0.001:
        try:
            subtracao = float(input("Adicione o primeiro número que quer subtrair. \n"))
            numeros = float(input("Adicione o numero que quer subtrair.\n"))
            subtracao = subtracao - numeros
            print(f"Resultado: {subtracao}\n")

        except ValueError:
            print("Desculpe, houve um erro. Tente novamente")
            print(f"Aqui o resultado antes do erro: {subtracao}\n")
            calc_subtracao()

    print(f"Resultado final: {subtracao}")
    calculadora()

# criando a função de multiplicação
def calc_multiplicacao():
    numeros = 0
    print("caso deseje cancelar ou finalizar, digite '0.001'\n")
    while numeros != 0.001:
        try:
            multiplicacao = float(input("Adicione o primeiro número que deseja multiplicar.\n"))
            numeros = float(input("Adicione o número que deseja multiplicar.\n"))
            multiplicacao = multiplicacao * numeros
            print(f"Resultado: {multiplicacao}\n")

        except ValueError:
            print("Desculpe, houve um erro. Tente novamente")
            print(f"Aqui o resultado antes do erro: {multiplicacao}\n")
            calc_multiplicacao()

    print(f"Resultado final: {multiplicacao}")
    calculadora()

# criando a função de divisão
def calc_divisao():
    numeros = 0
    print("caso deseje cancelar ou finalizar, digite '0.001'\n")
    while numeros != 0.001:
        try:
            divisao = float(input("Adicione o primeiro número que deseja dividir.\n"))
            numeros = float(input("Adicione o número que deseja dividir.\n"))
            divisao = divisao / numeros
            print(f"Resultado: {divisao}\n")

        except ValueError:
            print("Desculpe, houve um erro. Tente novamente")
            print(f"Aqui o resultado antes do erro: {divisao}")
            calc_divisao()

        except ZeroDivisionError:
            print("Desculpe, houve um erro. Tente novamente")
            print(f"Aqui o resultado antes do erro: {divisao}\n")
            calc_divisao()    

    print(f"Resultado final: {divisao}")
    calculadora()

calculadora()
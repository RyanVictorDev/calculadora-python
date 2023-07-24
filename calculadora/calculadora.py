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
    opcoes = ["soma", "subtração", "multiplicação", "divisão", "potenciação"]

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
        
        case "subtração":
            calc_subtracao()

        case "multiplicação":
            calc_multiplicacao()

        case "divisão":
            calc_divisao()

        # case "potenciação":
        #     calc_potenciacao()

        case _:
            print("Desculpas, houve um erro..")
            calculadora()

    
# criando a função de soma
def calc_soma():
    parcela_01 = 0
    parcela_02 = 0
    print("caso deseje cancelar ou finalizar, digite '0.001'\n")
    while parcela_01 != 0.001 or parcela_02 != 0.001:
        try:
            parcela_01 = float(input("Adicione o numero que quer somar.\n"))
            soma = parcela_01 + parcela_02
            parcela_02 = soma
            print(f"Resultado: {soma}\n")
        
        except ValueError:
            print("Desculpe, houve um erro. Tente novamente")
            print(f"Aqui o resultado antes do erro: {soma}\n")
            calc_soma()
    
    print(f"Resultado final: {soma}")
    calculadora()

# criando a função de subtração
def calc_subtracao():
    minuendo = 0
    print("caso deseje cancelar ou finalizar, digite '0.001'\n")
    while minuendo != 0.001 or subtraendo != 0.001:
        try:
            subtraendo = float(input("Adicione o primeiro número que quer subtrair. \n"))
            minuendo = float(input("Adicione o numero que quer subtrair.\n"))
            subtracao = subtraendo - minuendo
            print(f"Resultado: {subtracao}\n")

        except ValueError:
            print("Desculpe, houve um erro. Tente novamente")
            print(f"Aqui o resultado antes do erro: {subtracao}\n")
            calc_subtracao()

    print(f"Resultado final: {subtraendo}")
    calculadora()

# criando a função de multiplicação
def calc_multiplicacao():
    fator_01 = 0
    print("caso deseje cancelar ou finalizar, digite '0.001'\n")
    while fator_01 != 0.001 or fator_02 != 0.001:
        try:
            fator_01 = float(input("Adicione o primeiro fator:\n"))
            fator_02 = float(input("Adicione o segundo fator:\n"))
            produto = fator_01 * fator_02
            print(f"Resultado: {produto}\n")

        except ValueError:
            print("Desculpe, houve um erro. Tente novamente")
            print(f"Aqui o resultado antes do erro: {produto}\n")
            calc_multiplicacao()

    print(f"Resultado final: {produto}")
    calculadora()

# criando a função de divisão
def calc_divisao():
    dividendo = 0
    print("caso deseje cancelar ou finalizar, digite '0.001'\n")
    while dividendo != 0.001 or divisor != 0.001:
        try:
            print("="*25)
            dividendo = float(input("Adicione o dividendo:\n"))
            divisor = float(input("Adicione o divisor:\n"))
            divisao = dividendo / divisor
            print(f"Resultado: {divisao}\n")
            print("="*25)

        except ValueError:
            print("="*25)
            print("Desculpe, houve um erro. Tente novamente")
            print(f"Aqui o resultado antes do erro: {divisao}")
            print("="*25)

            calc_divisao()

        except ZeroDivisionError:
            print("="*25)
            print("Desculpe, houve um erro. Tente novamente")
            print(f"Aqui o resultado antes do erro: {divisao}\n")
            print("="*25)

            calc_divisao()
    
    print("="*25)
    print(f"Resultado final: {divisao}")
    print("="*25)
    calculadora()



# criando a função de potenciação
# def calc_potenciacao():
#     print("caso deseje cancelar ou finalizar, digite '0.001'\n")
#     while numeros != 0.001 or potencia != 0.001:
#         try:
#             potencia = float(input("Adicione o número que será potenciado:\n"))
            


calculadora()
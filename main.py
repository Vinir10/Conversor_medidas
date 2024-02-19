from funcoes import *

opcao = 0 


while opcao != "sair":


    print("[1] - metros")
    print("[2] - temperatura")
    print("[3] - velocidade")
    print("[4] - peso")
    print("sair")

    opcao = (input("QUAL UNIDADE DE MEDIDA GOSTARIA DE CONVERTER? [1], [2], [3], [4] ou sair: "))


    if opcao == "1":
        metros()

    elif opcao == "2":
        temperatura()

    elif opcao == "3":
        velocidade()

    elif opcao == "4":
        peso()

    elif opcao == "sair":
        print("encerrando...")

    else:
        print("Erro, tente novamente!")




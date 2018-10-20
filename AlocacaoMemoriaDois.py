espaco = 10
memoria = [" "] * espaco
opcao = 0
caso = 0
menorespaco = 0
menorinicio = 0
maiorinicio = 0
algoritmo = "First-fit"
A, B, C, D, E, F, G = 0, 0, 0, 0, 0, 0, 1

def variaveis():
    global A, B, C, D, E, F, memoria
    if caso == 0:
        A, B, C, D, E, F = 1, 3, 1, 2, 2, 0
        memoria[1] = "A"
        for i in range(6,9):
            memoria[i] = "B"

    elif caso == 1:
        A, B, C, D, E, F = 1, 1, 3, 1, 2, 1
        memoria[2] = "A"
        memoria[6] = "B"

    elif caso == 2:
        A, B, C, D, E, F = 1, 1, 2, 3, 2, 1
        memoria[2] = "A"
        memoria[6] = "B"
        memoria[9] = "G"

def primeiraEscolha():
    global cont, inicio, achou
    for i in range(espaco):
        if memoria[i] == ' ':
            cont += 1
            if cont == 1:
                inicio = i
        else:
            cont = 0
        if cont == tamanho:
            achou = True
            for i in range(tamanho):
                local = inicio + i
                memoria[local] = letra
            break
    if not achou:
        print("Espaço não encontrado para programa", letra)

def melhorEscolha():
    global cont, achou, menorinicio
    primeiro = True
    menorespaco = 0
    for i in range(espaco):
        if memoria[i] == " ":
            cont += 1
            if cont == 1:
                inicio = i
            if cont == tamanho:
                achou = True
        elif memoria[i] != " ":
            if achou:
                if primeiro:
                    menorinicio = inicio
                    menorespaco = cont
                    primeiro = False
                else:
                    if cont < menorespaco:
                        menorinicio = inicio
                        menorespaco = cont
            achou = False
            cont = 0

    if achou and (cont < menorespaco or primeiro):
        menorinicio = inicio
        menorespaco = cont
    if menorespaco == 0:
        print("Espaço não encontrado para o programa", letra)
    else:
        for c in range(tamanho):
            memoria[menorinicio + c] = letra

def piorEscolha():
    global cont, achou, maiorinicio
    primeiro = True
    maiorespaco = 0
    for i in range(espaco):
        if memoria[i] == " ":
            cont += 1
            if cont == 1:
                inicio = i
            if cont == tamanho:
                achou = True
        elif memoria[i] != " ":
            if achou:
                if primeiro:
                    maiorinicio = inicio
                    maiorespaco = cont
                    primeiro = False
                else:
                    if cont > maiorespaco:
                        maiorinicio = inicio
                        maiorespaco = cont
            achou = False
            cont = 0

    if achou and (cont > maiorespaco or primeiro):
        maiorinicio = inicio
        maiorespaco = cont
    if maiorespaco == 0:
        print("Espaço não encontrado para o programa", letra)
    else:
        for i in range(tamanho):
            memoria[maiorinicio + i] = letra

print(A, B, C, D, E, F)
print(memoria)
print("==========================\n")
for caso in range(3):
    memoria = [" "] * espaco
    variaveis()

    for opcao in range(3):

        print("\nCaso:", (caso+1), "Algoritmo: ", algoritmo)
        print(memoria)
        if opcao == 0:
            algoritmo = "First-fit"
            for tam in range(3):
                achou = False
                cont = 0
                if tam == 0:
                    letra="C"
                    tamanho = C
                elif tam == 1:
                    letra = "D"
                    tamanho = D
                elif tam == 2:
                    letra = "E"
                    tamanho = E
                primeiraEscolha()
                print("executando first-fit")
                print(memoria)
        elif opcao == 1:
            algoritmo = "Best-fit"
            for tam in range(4):
                achou = False
                cont = 0
                if tam == 1:
                    letra = "C"
                    tamanho = C
                elif tam == 2:
                    letra = "D"
                    tamanho = D
                elif tam == 3:
                    letra = "E"
                    tamanho = E
                elif tam == 4:
                    letra = "F"
                    tamanho = F
                melhorEscolha()
                print("executando best-fit")
                print(memoria)
        elif opcao == 2:
            algoritmo = "Worst-fit"
            for tam in range(4):
                achou = False
                cont = 0
                if tam == 1:
                    letra = "C"
                    tamanho = C
                elif tam == 2:
                    letra = "D"
                    tamanho = D
                elif tam == 3:
                    letra = "E"
                    tamanho = E
                elif tam == 4:
                    letra = "F"
                    tamanho = F
                piorEscolha()
                print("executando worst-fit")
                print(memoria)
        print("====================")
'''
while(caso != 4):
    opcao = 0
    memoria = [" "] * 10
    print("Escolha o número do caso, ou digite 4 para sair:")
    caso = int(input())
    variaveis()

    if caso == 4:
        print("See ya o/")
        break
    elif caso == 1 or caso == 2 or caso == 3:
        while(opcao != 4):
            cont = 0
            achou = False
            print("memoria: ", memoria)
            print("\nEscolha o algoritmo de alocação:\n1 - First-fit")
            print("2 - Best-fit")
            print("3 - Worst-fit")
            print("4 - Voltar ao inicio")
            opcao = int(input())
            if opcao == 4:
                break
            elif opcao == 1 or opcao == 2 or opcao == 3:
                print("Escolha o programa a ser alocado:")
                if caso == 1:
                    print("C:", C, "D:", D, "E:", E)
                    letra = input().upper()

                    if letra=="C":
                        tamanho = C
                    elif letra=="D":
                        tamanho = D
                    elif letra == "E":
                        tamanho = E
                    else:
                        print("Digite uma opção válida")
                        tamanho = " "

                    if opcao == 1:
                        primeiraEscolha()
                    elif opcao == 2:
                        melhorEscolha()
                    elif opcao == 3:
                        piorEscolha()

                elif caso == 2:
                    print("C:", C, "D:", D, "E:", E, "F:", F)
                    letra = input().upper()
                    if letra == "C":
                        tamanho = C
                    elif letra == "D":
                        tamanho = D
                    elif letra == "E":
                        tamanho = E
                    elif letra == "F":
                        tamanho = F
                    else:
                        print("Digite uma opção válida")
                        tamanho = " "
                    if opcao == 1:
                        primeiraEscolha()
                    elif opcao == 2:
                        melhorEscolha()
                    elif opcao == 3:
                        piorEscolha()

                elif caso == 3:
                    print("C:", C, "D:", D, "E:", E, "F:", F)
                    letra = input().upper()
                    if letra == "C":
                        tamanho = C
                    elif letra == "D":
                        tamanho = D
                    elif letra == "E":
                        tamanho = E
                    elif letra == "F":
                        tamanho = F
                    else:
                        print("Digite uma opção válida")
                        tamanho = " "
                    if opcao == 1:
                        primeiraEscolha()
                    elif opcao == 2:
                        melhorEscolha()
                    elif opcao == 3:
                        piorEscolha()

                else:
                    print("Como você conseguiu chegar até essa parte do programa? Parabéns por quebrar meu código!\n"
                          "De qualquer forma, escolha um dos casos disponíveis, por favor...")
            else:
                print("Digite um dos algoritmos pelo número deles.")
    else:
        print("Escolha um dos casos: 1, 2 ou 3, ou digite 4 para sair do programa.")
'''

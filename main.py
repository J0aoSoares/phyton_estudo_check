resposta = input("Você quer conhecer minha calculadora ? (s/n): ")
while resposta != "s" and resposta != "n":  #not (resposta == "s" or resposta == "n")
    resposta = input("Tem que ser s ou n: ")

if resposta == "n":
    print("Ok então mano, falou.")

else:
    while True:
        opcao = input("O que você quer fazer? (s, div, sub, mult): ")
        while opcao != "s" and opcao != "sub" and opcao != "div" and opcao != "mult":
            opcao = input("Pfv escolha uma das opções (s, div, sub, mult")

        num1 = input("Diga o primeiro número: ")
        while not num1.isnumeric():
            num1 = input("Tem que ser num inteiro: ")
        num1 = int(num1)

        num2 = input("Diga o segundo número: ")
        while not num2.isnumeric():
            num2 = input("Tem que ser num inteiro: ")
        num2 = int(num2)

        if opcao == "s":
            resultado = num1+num2

        elif opcao == "div":
            resultado = num1/num2

        elif opcao == "sub":
            resultado = num1-num2

        else:
            resultado = num1*num2

        print(f"O resultado entre {num1} e {num2} é {resultado}")

        novamente = input("Voce quer fazer algo mais? (s/n): ")
        while novamente!= "s" and novamente != "n":
            input("Sério? denovo? po me ajudaí: ")
        if novamente == "s":
            continue
        else:
            break


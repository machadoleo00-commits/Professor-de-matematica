import random
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = input("Digite o número da operação: ")
maximo =  int(input('escolha o numero maximo da tabuada desejada: '))
quantidade =  int(input('escolha o numero de perguntas que deseja: '))
acertos = 0
gabarito = []
for i in range(quantidade):
    n1 = random.randint(1,maximo)
    n2 = random.randint(1,maximo)
    if operacao == "1":
        resposta_certa = n1 + n2
        simbolo = "+"
    if operacao == "2":
        resposta_certa = n1 - n2
        simbolo = "-"
    if operacao == "3":
        resposta_certa = n1 * n2
        simbolo = "x"
    if operacao == "4":
        n1 = n1 * n2
        resposta_certa = n1 / n2
        simbolo = "/"
    
    resposta = int(input(f'\n{i+1}: {n1} {simbolo} {n2} = '))
    if resposta == resposta_certa:
        print("\nCerto!")
        acertos += 1
    else:
        print(f"\nErrado! A resposta certa era {resposta_certa}.")
    gabarito.append((n1, simbolo, n2, resposta_certa))
print(f"\nVocê acertou {acertos} de {quantidade} de perguntas.")
print(f"\nVocê tirou {acertos / quantidade * 100}")
print(f"\n--- GABARITO ---")
for i, (numero1, simb, numero2, resultado) in enumerate (gabarito, start=1):
    print(f"Pergunta {i} : {numero1} {simb} {numero2} = {resultado}")

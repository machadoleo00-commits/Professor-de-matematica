import random
maximo =  int(input('escolha o numero maximo da tabuada desejada: '))
quantidade =  int(input('escolha o numero de perguntas que deseja: '))
acertos = 0
gabarito = []
for i in range(quantidade):
    n1 = random.randint(1,maximo)
    n2 = random.randint(1,maximo)
    resposta_certa = n1 * n2
    resposta = int(input(f'\n{i+1}: {n1} x {n2} = '))
    if resposta == resposta_certa:
        print("\nCerto!")
        acertos += 1
    else:
        print(f"\nerrado! a resposta certa era {resposta_certa}.")
    gabarito.append((n1, n2, resposta_certa))
print(f"\nvoce acertou {acertos} de {quantidade} de perguntas.")
print(f"\nvocê tirou {acertos / quantidade * 100}")
print(f"\n--- GABARITO ---")
for i, (numero1, numero2, resultado) in enumerate (gabarito, start=1):
    print(f"pergunta {i} : {numero1} x {numero2} = {resultado}")

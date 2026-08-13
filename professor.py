import random
maximo =  int(input('escolha o numero maximo da tabuada desejada: '))
quantidade =  int(input('escolha o numero de perguntas que deseja: '))
acertos = 0
for i in range(quantidade):
    n1 = random.randint(1,maximo)
    n2 = random.randint(1,maximo)
    resposta_certa = n1 * n2
    resposta = int(input(f'{i+1}: {n1} x {n2} = '))
    if resposta == resposta_certa:
        print("Certo!")
        acertos += 1
    else:
        print(f"errado! a resposta certa era {resposta_certa}.")
print(f"voce acertou {acertos} de {quantidade} de perguntas.")
print(f"você tirou {acertos / quantidade * 100}")


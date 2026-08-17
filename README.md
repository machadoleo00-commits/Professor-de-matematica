<<<<<<< HEAD
# 🎓 Professor de Matemática

Um gerador de exercícios de matemática via linha de comando, desenvolvido em Python. Permite ao usuário praticar operações básicas com perguntas aleatórias, recebendo feedback na hora e um gabarito completo ao final.

## Funcionalidades

- ✅ Escolha entre 4 operações: soma, subtração, multiplicação e divisão
- ✅ Definição do valor máximo dos números sorteados
- ✅ Definição da quantidade de perguntas
- ✅ Feedback imediato (certo/errado) a cada resposta
- ✅ Placar final com total de acertos e percentual de aproveitamento
- ✅ Gabarito completo com todas as contas e respostas corretas ao final

## Como funciona

O programa pede ao usuário para escolher a operação desejada, o valor máximo dos números e a quantidade de perguntas. Em seguida, gera perguntas aleatórias dentro do intervalo escolhido, comparando a resposta do usuário com o resultado correto.

Na divisão, os números são ajustados automaticamente para garantir que o resultado seja sempre um número inteiro exato.

Ao final, é exibido o total de acertos, o percentual de aproveitamento e um gabarito com todas as perguntas e respostas corretas.

## Tecnologias e conceitos aplicados

- Python 3
- Módulo `random` (`random.randint`)
- Loops (`for`, com `range`)
- Estruturas condicionais (`if`)
- Listas e tuplas
- `enumerate()`
- f-strings
- Entrada e saída de dados (`input`, `print`)

## Como executar

Pré-requisito: Python 3 instalado.

```bash
python nome_do_arquivo.py
```

## Possíveis melhorias futuras

- Validação de entrada (evitar erro se o usuário digitar um valor não numérico)
- Uso de `elif` no lugar de `if` para melhorar a legibilidade da escolha de operação
- Cronômetro para medir o tempo de resposta
- Diferentes níveis de dificuldade
=======
Um projeto simples, mas com bastante conteúdo prático de lógica de programação. O programa permite ao usuário:

✅ Escolher entre as 4 operações básicas (soma, subtração, multiplicação e divisão)
✅ Definir o valor máximo dos números e a quantidade de perguntas
✅ Responder cada pergunta e receber feedback na hora (certo/errado)
✅ Ver um placar final com o total de acertos
✅ Consultar um gabarito completo com todas as contas e respostas corretas
>>>>>>> 6560db20da70553f964b153d8c9300cac7fb7eb5

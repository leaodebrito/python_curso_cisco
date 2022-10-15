
#O comando continue é utilizada para saltar o bloco atual e avançar para a próxima iteração, sem executar as declarações dentro do loop.
#Pode ser utilizada tanto com os loops while e for .
#A sua tarefa aqui é muito especial: tem de conceber um vowel eater (comedor de vogais)! Escreva um programa que use:

#um loop for ;
#o conceito de execução condicional (if-elif-else)
#a declaração continue .
#O seu programa deve:

#pedir ao utilizador para introduzir uma palavra;
#usar user_word = user_word.upper() para converter a palavra introduzida pelo utilizador em maiúsculas; falaremos sobre os chamados métodos de strings e o método upper() muito em breve - não se preocupe;
#usar execução condicional e a declaração continue para “comer” as seguintes vogais A, E, I, O, U da palavra introduzida;
#imprimir as letras não comidas para o ecrã, cada uma delas numa linha separada.


palavra = input("Digite uma palavra: ")

palavra = palavra.upper()

letter = len(palavra)
i = 0

for i in range(letter):
    if palavra[i] == "A":
        continue
    elif palavra[i] == "E":
        continue
    elif palavra[i] == "I":
        continue
    elif palavra[i] == "O":
        continue
    elif palavra[i] == "U":
        continue
    print(palavra[i])
    i = i + 1

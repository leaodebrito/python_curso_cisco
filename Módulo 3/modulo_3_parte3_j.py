blocks = int(input("Enter the number of blocks: "))

#declaração do contador
i = 0

while i < blocks:
    # contagem de voltas
    i = i + 1
    #  Quantidade de blocos ainda disponíveis.
    blocks = blocks - i

    # A cada interação a quantidade blocos diminui e a quantidade de voltas aumenta
    # para cada linha, o valor do contador é igual a quantidade de blocos em cada linha.
    # A Quantidade de blocos deve ser reduzidade do valor das voltas

#atribuir a altura da pirâmide a quantidade de voltas da função while
height = i

print("The height of the pyramid:", height)

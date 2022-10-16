c0 = int(input("Digite um número inteiro: "))

i = 0

while c0 != 1:
    if c0%2 == 0:
        c0 = c0 / 2
        print (int(c0))
    elif c0%2 == 1:
        c0 = 3 * c0 + 1
        print(int(c0))
    i = i + 1

print("steps: ", i)
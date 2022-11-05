my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

# Encontrar o maior valor de uma lista
my_list = [15, 3, 11, 5, 1, 9, 7, 15, 13, 20, 33]
largest = my_list[0]
print(largest)

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

# TODO: Revisar código abaixo
# Agora vamos encontrar a localização de um dado elemento dentro de uma lista:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")
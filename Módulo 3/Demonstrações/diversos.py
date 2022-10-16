my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)


#troca de itens em listas
my_list = [10, 1, 8, 3, 5]
print(my_list) #[10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list) #[5, 3, 8, 1, 10]
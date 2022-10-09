#função input()
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)


#operadores de string
# Concatenação de strings
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")


#exercício
num_a = float(input("Digite um número: "))
num_b = float(input("Digita um outro número: "))


print(num_a + num_b)
print(num_a - num_b)
print(num_a * num_b)
print(num_a / num_b)

print("\nThat's all, folks!")


#exercício
x = float(input("Enter value for x: "))

y = 1 / (x + (1/(x +(1/(x + (1/x))))))

print("y =", y)

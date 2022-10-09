i = 0
a = True
while a:
    print("I'm stuck inside a loop.")
    i = i + 1
    print(i)
    if i == 666:
        a = False


counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)


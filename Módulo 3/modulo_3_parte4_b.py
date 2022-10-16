#Passo 1
beatles = []
print("Step 1:", beatles)

#Passa 2
beatles.append("John Lennon")
beatles.append("Paul MacCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

#Passo 3
for i in range(2):
    new_member = input("Diga o novo membro: ")
    beatles.append(new_member)

print(print("Step 3:", beatles))

#Passo 4
del beatles[3]
del beatles[3]
print("Step 4:", beatles)

#Passo 5
beatles.insert(4,"Ringo Starr")
print("Step 5:", beatles)

#Testing List lenght
print("The Fab", len(beatles))
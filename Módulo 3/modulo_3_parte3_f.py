palavra_secreta = "chupacabra"
contador = 0

while True:
    palavra = input("Qual a palavra secreta? ")
    if palavra == palavra_secreta:
        print("You've successfully left the loop.")
        break
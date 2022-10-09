secret_number = 77

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess_number = int(input("Adivinhe o número: "))

while guess_number != secret_number:
    print("Ha ha! You're stuck in my loop!")

print("Well done, muggle! You are free now.")

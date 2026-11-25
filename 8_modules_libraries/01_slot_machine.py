import random

symbols = ["🍒", "🍇", "🍉", "7️⃣"]


def play():

    for i in range(1, 51):
        results = random.choices(symbols, k=3)
        print(f"{results[0]} | {results[1]} | {results[2]}")
        win = results[0] == "7️⃣" and results[1] == "7️⃣" and results[2] == "7️⃣"

        if win:
            print("Jackpot!!! 💰")
            break
        else:
            results = random.choices(symbols, k=3)


answer = ""
while answer.upper() != "N":
    play()
    answer = input("Keep playing? (Y/N) ")

print("Thanks for playing!")

import random

print("🎲 Добро пожаловать в игру 21!")

player_score = 0
computer_score = random.randint(15, 21)

while True:
    card = random.randint(2, 11)
    player_score += card
    print(f"Твоя карта: {card}. Твоя сумма: {player_score}")

    if player_score > 21:
        print("Перебор! 😢 Ты проиграл.")
        break
    elif player_score == 21:
        print("Ты набрал 21! 🥳 Победа!")
        break

    choice = input("Хочешь взять ещё карту? (д/н): ").lower()
    if choice != 'д':
        print(f"Твоя сумма: {player_score}")
        print(f"Сумма компьютера: {computer_score}")
        if player_score > computer_score or computer_score > 21:
            print("Ты выиграл! 🎉")
        elif player_score == computer_score:
            print("Ничья 🤝")
        else:
            print("Компьютер победил 💻")
        break

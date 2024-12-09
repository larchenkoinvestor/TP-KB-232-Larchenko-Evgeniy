import random

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Нічия!"
    elif (user_choice == "stone" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "stone"):
        return "Ви перемогли!"
    else:
        return "Переміг комп'ютер!"

def main_game():
    print("Гра - Камінь, Ножиці, Папір!")
    options = ["stone", "scissor", "paper"]
    
    while True:
        user_choice = input("Введіть ваш вибір (stone, scissor, paper) або 'exit' для виходу: ").strip().lower()
        if user_choice == "exit":
            print("Гра завершена. Дякуємо за гру!")
            break
        if user_choice not in options:
            print("Некоректний вибір. Спробуйте ще раз.")
            continue
        
        computer_choice = random.choice(options)
        print(f"Комп'ютер обрав: {computer_choice}")
        print(get_winner(user_choice, computer_choice))
        
if __name__ == "__main__":
    main_game()

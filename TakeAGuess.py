# ==========================================
# Number Guessing Game
# Made by Rishi Vatish
# Week 2 Python Project
# ==========================================

import random

print("=" * 40)
print("🎮 Welcome to Rishi's Number Guessing Challenge!")
print("=" * 40)

while True:

    # Difficulty Selection
    easy = 10
    medium = 7
    hard = 5
    print("\nChoose Difficulty:")
    print(f"1. Easy ({easy} attempts)")
    print(f"2. Medium ({medium} attempts)")
    print(f"3. Hard ({hard} attempts)")

    difficulty = input("Select difficulty (1/2/3): ")

    if difficulty == "1":
        max_attempts = easy
    elif difficulty == "2":
        max_attempts = medium
    else:
        print("⚠️ Invalid choice, defaulting to Hard mode.")
        max_attempts = hard

    # Generate random secret number
    secret_number = random.randint(1, 100)

    # Track attempts
    attempts = 0

    print("\nI'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts.")
    print("Good luck!\n")

    while attempts < max_attempts:

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        attempts += 1

        # Player guessed correctly
        if guess == secret_number:

            print("\n🎉 CORRECT!")
            print(f"You guessed the number in {attempts} attempts.")

            # Accuracy Score
            accuracy = (1 / attempts) * 100
            print(f"📊 Accuracy Score: {accuracy:.1f}%")

            # Performance Rating
            if attempts <= 3:
                print("🔥 Incredible guessing skills!")
            elif attempts <= 5:
                print("👍 Great job!")
            else:
                print("😅 You got there eventually!")

            break

        # Distance from answer
        difference = abs(guess - secret_number)

        if difference <= 5:
            print("🔥 Very Close!")

        elif difference <= 10:
            print("👀 Close!")

        # Odd/Even Hint
        if guess % 2 == secret_number % 2:
            print("💡 Hint: Your guess has the same odd/even property as the secret number.")

        # High/Low Hint
        if guess < secret_number:
            print("📉 Too Low!")
        else:
            print("📈 Too High!")

        print(f"Attempts Left: {max_attempts - attempts}\n")

    else:
        print("\n💀 GAME OVER!")
        print(f"The secret number was {secret_number}")

    # Play Again Option
    play_again = input("\nPlay Again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n===================================")
        print("Thanks for playing!")
        print("Created by Rishi Vatish")
        print("===================================")
        break
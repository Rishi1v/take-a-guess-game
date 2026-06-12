# ==========================================
# Number Guessing Game
# Made by Rishi Vatish
# Week 2 Python Project
# ==========================================

import random

# difficulty options - storing as a dict so i dont have to repeat myself
DIFFICULTIES = {
    "1": ("Easy",   10),
    "2": ("Medium",  7),
    "3": ("Hard",    5),
}

def get_difficulty():
    print("\nChoose Difficulty:")
    for key, (label, attempts) in DIFFICULTIES.items():
        print(f"  {key}. {label} ({attempts} attempts)")

    while True:
        choice = input("Select difficulty (1/2/3): ").strip()
        if choice in DIFFICULTIES:
            label, max_attempts = DIFFICULTIES[choice]
            print(f"✅ {label} mode — {max_attempts} attempts. Let's go!\n")
            return max_attempts
        print("⚠️ That's not valid, pick 1, 2 or 3.")


def calc_accuracy(attempts, max_attempts):
    # 1 attempt = 100%, using all attempts = ~0%
    # scales based on how many attempts the difficulty gives you
    return max(0, ((max_attempts - attempts) / (max_attempts - 1)) * 100)


def play_round():
    max_attempts = get_difficulty()
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:

        try:
            guess = int(input("Enter your guess: ").strip())
        except ValueError:
            print("❌ Enter a whole number!\n")
            continue

        # out of range check
        if not (1 <= guess <= 100):
            print("❌ Has to be between 1 and 100!\n")
            continue

        attempts += 1

        if guess == secret_number:
            accuracy = calc_accuracy(attempts, max_attempts)
            print(f"\n🎉 CORRECT! Got it in {attempts} attempt{'s' if attempts != 1 else ''}.")
            print(f"📊 Accuracy Score: {accuracy:.1f}%")

            if attempts == 1:
                print("🤯 No way — first try?!")
            elif attempts <= 3:
                print("🔥 That's crazy good!")
            elif attempts <= 5:
                print("👍 Nice one!")
            else:
                print("😅 Got there eventually lol")
            return True

        # how far off are they
        difference = abs(guess - secret_number)

        if difference <= 5:
            print("🔥 SO close!")
        elif difference <= 10:
            print("👀 Getting warmer...")

        # odd/even hint
        if guess % 2 == secret_number % 2:
            print("💡 Hint: same odd/even as the secret number.")

        # direction
        if guess < secret_number:
            print("📉 Too low!")
        else:
            print("📈 Too high!")

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Attempts left: {remaining}\n")

    print(f"\n💀 GAME OVER! It was {secret_number}. Better luck next time.")
    return False


def main():
    print("=" * 42)
    print("  🎮 Rishi's Number Guessing Challenge!")
    print("=" * 42)

    wins = 0
    rounds = 0

    while True:
        won = play_round()
        rounds += 1
        if won:
            wins += 1

        print(f"\n📊 Score: {wins}W / {rounds - wins}L this session.")

        again = input("\nPlay again? (y/yes): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n" + "=" * 42)
            print("  Thanks for playing!")
            print("  Created by Rishi Vatish")
            print("=" * 42)
            break


if __name__ == "__main__":
    main()
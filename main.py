#Developed a command - line Rock - Paper - Scissors game using Python, integrating real - time gameplay logic, CSV logging, and player statistics.

#🔹 Implemented input handling, randomization, and winner determination logic.
#🔹 Automatically logged each round with timestamp, choices, and winner to a CSV file.
#🔹 Tracked game stats(wins, losses, ties, win percentage) and displayed them after each round.
#🔹 Structured for scalability(can be extended with GUI, AI, or multiplayer).

import random
import csv
from datetime import datetime

# Scoreboard initialization
score = {
    "User": 0,
    "Computer": 0,
    "Ties": 0,
    "Total": 0
}


def get_user_choice():
    choice = input("\nEnter your choice (rock/paper/scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("❌ Invalid choice. Try again.")
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return choice


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user, computer):
    print(f"\n🧑 You chose: {user}")
    print(f"💻 Computer chose: {computer}")

    score["Total"] += 1

    if user == computer:
        score["Ties"] += 1
        return "Tie"
    elif (user == 'rock' and computer == 'scissors') or \
            (user == 'paper' and computer == 'rock') or \
            (user == 'scissors' and computer == 'paper'):
        score["User"] += 1
        return "User"
    else:
        score["Computer"] += 1
        return "Computer"


def log_to_csv(user, computer, result):
    with open("rps_results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user, computer, result])


def show_stats():
    user_wins = score["User"]
    computer_wins = score["Computer"]
    ties = score["Ties"]
    total = score["Total"]
    win_pct = (user_wins / total) * 100 if total > 0 else 0

    print("\n📊 Game Stats:")
    print(f"🧑 Your Wins: {user_wins}")
    print(f"💻 Computer Wins: {computer_wins}")
    print(f"🤝 Ties: {ties}")
    print(f"🎯 Total Games: {total}")
    print(f"🏆 Your Win %: {win_pct:.2f}%")


def main():
    print("🎮 Welcome to Rock-Paper-Scissors!")

    # Ensure CSV file has a header row if new
    try:
        with open("rps_results.csv", "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "User Choice", "Computer Choice", "Winner"])
    except FileExistsError:
        pass

    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        result = determine_winner(user, computer)

        # Result message
        if result == "Tie":
            print("🤝 It's a tie!")
        elif result == "User":
            print("🎉 You win!")
        else:
            print("💻 Computer wins!")

        # Save result and show stats
        log_to_csv(user, computer, result)
        show_stats()

        # Play again?
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing!")
            break


if __name__ == "__main__":
    main()


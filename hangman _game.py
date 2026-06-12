import random

print("=" * 50)
print("🎮 WELCOME TO THE HANGMAN GAME 🎮")
print("=" * 50)


word_list = [
    "python",
    "computer",
    "programming",
    "developer",
    "technology"
]


secret_word = random.choice(word_list)


display_word = ["_"] * len(secret_word)


guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


while wrong_guesses < max_wrong_guesses and "_" in display_word:

    print("\n" + "=" * 50)
    print(hangman_stages[wrong_guesses])

    print("Word:", " ".join(display_word))
    print("Guessed Letters:", guessed_letters)
    print(f"Remaining Chances: {max_wrong_guesses - wrong_guesses}")

    guess = input("\nEnter a letter: ").lower()

  
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.")
        continue

  
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

   
    if guess in secret_word:
        print("✅ Correct Guess!")

        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                display_word[index] = guess

    else:
        print("❌ Wrong Guess!")
        wrong_guesses += 1



print("\n" + "=" * 50)

if "_" not in display_word:
    print("🎉 CONGRATULATIONS! YOU WON 🎉")
    print("The word was:", secret_word)
else:
    print(hangman_stages[6])
    print("💀 GAME OVER!")
    print("You have used all 6 chances.")
    print("The correct word was:", secret_word)

print("=" * 50)
print("Thank you for playing Hangman!")
print("=" * 50)
import random

words = ["apple", "banana", "mahindra"]
secret = random.choice(words).lower()
secret_letters = list(secret)

print("Welcome to Hangman Game!")
print(f"You need to guess {len(secret_letters)} letters.")


attempts_left = max(6, len(secret_letters) + 1)


guessed = set()
correct = set()
display = ["_" for _ in secret_letters]

while attempts_left > 0 and "_" in display:
    print("\nWord: " + " ".join(display))
    print(f"Attempts left: {attempts_left}")
    guess = input("Enter a single letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one alphabetic character.")
        continue

    if guess in guessed:
        print(f"You already guessed '{guess}'. Try another letter.")
        continue

    guessed.add(guess)

    if guess in secret_letters:
        print(f"Good — '{guess}' is in the word!")
        for i, ch in enumerate(secret_letters):
            if ch == guess:
                display[i] = guess
        correct.add(guess)
    else:
        attempts_left -= 1
        print(f"Sorry — '{guess}' is not in the word.")

if "_" not in display:
    print("\nCongratulations! You guessed the word:", secret)
else:
    print("\nOut of attempts. The word was:", secret)

print("Thanks for playing!")

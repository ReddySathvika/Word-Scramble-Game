import random

# List of words and optional hints
word_list = [
    ("python", "Popular programming language"),
    ("apple", "A fruit and a tech company"),
    ("planet", "Orbits a star"),
    ("keyboard", "Used to type"),
    ("notebook", "Used to take notes or a laptop")
]

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def play_game():
    print("🔤 Welcome to the Word Scramble Game!\nUnscramble the words to earn points.\n")
    score = 0

    for word, hint in random.sample(word_list, len(word_list)):
        scrambled = scramble_word(word)
        print(f"\nScrambled word: {scrambled}")
        user_input = input("Your guess (or type 'hint'): ").lower()

        if user_input == "hint":
            print(f"Hint: {hint}")
            user_input = input("Your guess: ").lower()

        if user_input == word:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct word was '{word}'.")

    print(f"\n🎯 Game over! Your total score: {score}/{len(word_list)}")

# Run the game
if __name__ == "__main__":
    play_game()

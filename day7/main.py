import random
import art
import word_list

word = random.choice(word_list.word_list)
display = []
end_game = False
lives = 6
wrong = []
for letter in word:
    display.append("_")

print(art.logo)

while not end_game:
    print(word)
    guess = input("Guess a letter: ").lower()

    if display.count(guess) > 0:
        print(f"You already guess the letter {guess}, and its in the word.")

    elif wrong.count(guess) > 0:
        print(f"You already guess the letter {guess}, and its not in the word.")

    else:
        for position in range(len(word)):
            if word[position] == guess:
                display[position] = guess
    if guess not in word:
        lives -= 1
        wrong.append(guess)
        if lives == 0:
            print("LOSER")
            end_game = True
    print(art.stages[lives])
    print(display)
    print(f"Tease are the wrong guesses: {wrong}")
    if "_" not in display:
        end_game = True
        print("You Win")


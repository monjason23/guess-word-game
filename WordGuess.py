import random


def hide_letters(word):
    # Initial value is empty string
    word_letters_hidden = ""
    # For every in the word, add string "-"
    for letter in word:
        word_letters_hidden += "-"

    # Return the result
    return word_letters_hidden


def get_random_word():
    words = open("Words.txt", "r")
    words_list = []

    # Append every word to words_list and remove "\n"
    for word in words:
        words_list.append(word.replace("\n", ""))

    # Get a random word from list
    return words_list[random.randint(1, len(words_list) - 1)]


def reveal_letter(word, current_word, letter):
    # word refers to the actual word_to_guess
    # current_word refers to the word with hidden letters
    # letter refers to the entered letter

    # Covert current_word to list
    to_list = list(current_word)

    # Check every letter in word and if matches with the entered letter, override the value in to_list
    for i in range(len(word)):
        if word[i] == letter:
            to_list[i] = letter

    # Join list to make string
    return "".join(to_list)


def word_guess_game(word_to_guess):
    guesses = 8
    is_completed = False
    current_word = hide_letters(word_to_guess)

    # Function to show current_word
    def show_current_word():
        print(f"The word now looks like this: {current_word}")

    # Function to show number of guesses
    def show_current_guesses():
        print(f"You have {guesses} left!")

    show_current_word()
    show_current_guesses()

    while guesses != 0 and not is_completed:
        letter = input("Type a single letter here, then press enter: ")
        upper_letter = letter.upper()

        if upper_letter in current_word:
            print("You already entered that letter!")

        elif upper_letter in word_to_guess:
            # If letter is in word_to_guess, reveal the position of letter by calling reveal_letter function
            current_word = reveal_letter(word_to_guess, current_word, upper_letter)

            # After revealing a letter and is equal to the actual word_to_guess, set is_completed to True
            if current_word == word_to_guess:
                is_completed = True
                break

            print("That guess is correct!")
            show_current_word()

        else:
            guesses = guesses - 1
            print(f"There are no {letter}'s in the word")
            show_current_word()
            show_current_guesses()

    if not is_completed:
        print("Sorry try again...")

    else:
        print("Congrats!")
        print(f"You got it right! The word is {current_word}")


def main():
    word_guess_game(get_random_word())


if __name__ == '__main__':
    main()


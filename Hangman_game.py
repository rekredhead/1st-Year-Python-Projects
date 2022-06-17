import random
import string

word_list_filename = "words.txt"

# Responses to in-game events
responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]


def choose_random_word(all_words):
    """ Uses the Random module to choose a random word from list containing all words, which have been taken from a
    text file """
    return random.choice(all_words)


def load_words():
    """
    1. Informs the user that the words are loading from the file since different devices might take longer time to
    collect and the return the word list
    2. Uses try-except function to avoid errors if file is not in the directory, if so the user will be shown the
        warning and the program stops to avoid further errors
    3. If the file does exist, open the text file as a readable file
    4. Read each line of the file and remove '\n' from each line, until there are no more lines with text
    5. Store each word of the line into a list by separating each word from their space
    6. Concatenate each list per line into another list, which will contain every word from the text file
    7. After all the words are stored in the list, close the file, display the number of words there are and return the
        the list
    """
    print("Loading word list from file:", word_list_filename)

    try:
        text_file = open(word_list_filename, "r")
        word_lst = []
        while True:
            line = text_file.readline().replace("\n", "")
            if line == "":
                break

            line_list = line.split(" ")
            word_lst += line_list

        text_file.close()
        print(len(word_lst), "words loaded.")
        return word_lst

    except FileNotFoundError:
        print("Error: word list not found in the directory")
        quit()


word_list = load_words()


def welcome_message():
    """ Display the welcome message """
    print("Welcome to Hangman Ultimate Edition")


# From this point onwards, letters_guessed is a set containing letters which the user has guessed
def is_word_guessed(word, letters_guessed):
    """
    Remove each letter that is in the set from the word
    If the word is completely blank(user guessed the word), return True
    If there are letters still remaining, return False
    """
    for letter in letters_guessed:
        word = word.replace(letter, "")

    if word == "":
        return True
    else:
        return False


def get_guessed_word(word, letters_guessed):
    """
    Replace each letter that the user guessed from the word with "_ "
    Return the newly formatted word
    """
    for letter in word:
        if letter not in letters_guessed:
            word = word.replace(letter, "_ ")

    return word


def get_remaining_letters(letters_guessed):
    """
    Uses the String module to get all the alphabetical letters in lower case, store it in a string named alphabet
    Remove each letter that the user has guessed from alphabet
    Return the newly formatted alphabet string
    """
    alphabet = string.ascii_lowercase
    for letter in letters_guessed:
        alphabet = alphabet.replace(letter, "")

    return alphabet


def hangman(word):
    """
    This is the main game program
    Strings from the responses global list will be used to respond to the user's actions

    1. Display the number of letters in the word and draw a line
    User has 6 chances to guess the word and the letters they guessed will be stored in a set to avoid letters which
        they have already guessed.
    The unique letters in the word will be stored in a set, by adding spaces between each letter and using those spaces
        to separate each letter into a list which will be converted to a set
    A while loop is used to keep prompting the user for a letter until they reach the limit or when they guessed the
        word
    2. If the user has guessed the word, display their congratulating message and score, return the score and
        end the game
    3. If the user used up all their guesses, display the message to them, return the score of 0 and end the game
    4. If none of step 2 and step 3 are True, display the number of guesses the user has remaining and the available
        letters left and prompt them to enter a letter, which is converted to lower
    5. If the user enters a letter which isn't in the alphabet, they are informed the guess is invalid and lost a
        chance to guess, draws a line and go back to step 2
    6. Otherwise, if their letter is valid, and the letter exists in the word but is already in letters_guessed (user
        guessed that letter before)

        - the guessed letter is added to the set and user is informed the letter is already guessed
        - the guessed word is displayed (Eg: _ a_ _ _ )
        - draws a line and goes back to step 2

    7. Otherwise, if their letter exists in the word and is not in letters_guessed (user hasn't guessed the letter yet)

        - the letter is added to set and the user is informed they made a good guess
        - the guessed word with the newly added letter is displayed (Eg: t_ g_ )
        - draws a line and goes back to step 2

    8. If their letter does not exist in the word and is already in letters_guessed (user guessed the letter before)

        - the guessed letter is added to the set and user is informed the letter is already guessed
        - the guessed word is displayed
        - draws a line and goes back to step 2

    9. If their letter does not exist in the word but is not in letters_guessed (user enters letter which isn't in the
        word)

        - If their letter is a vowel, number of guesses decreases by 2. Otherwise, number of guesses decreases by 1
        - letter is added to the set and user is informed the letter is not in the word
        - draws a line and goes back to step 2
    """
    print(responses[0].format(len(word)))
    print("-------------")

    number_of_guesses = 6
    vowels = ('a', 'e', 'i', 'o', 'u')

    # Using a set to prevent duplicate letters
    letters_guessed = set()
    unique_letters_in_word = set(" ".join(word).split(" "))

    while True:
        if is_word_guessed(word, letters_guessed):
            score = number_of_guesses * len(unique_letters_in_word)
            print(responses[1])
            print(responses[2].format(score))
            return score
            break

        if number_of_guesses < 1:
            score = 0
            print(responses[3].format(word))
            return score
            break

        print(responses[4].format(number_of_guesses))
        print(responses[5].format(get_remaining_letters(letters_guessed)))
        input_letter = str(input("Please guess a letter: ")).lower()

        if input_letter not in string.ascii_lowercase:
            print("Guess is invalid")
            number_of_guesses -= 1

        else:
            if input_letter in word:
                if input_letter in letters_guessed:
                    letters_guessed.add(input_letter)
                    print(responses[8].format(get_guessed_word(word, letters_guessed)))

                else:
                    letters_guessed.add(input_letter)
                    print(responses[6].format(get_guessed_word(word, letters_guessed)))

            else:
                if input_letter in letters_guessed:
                    letters_guessed.add(input_letter)
                    print(responses[8].format(get_guessed_word(word, letters_guessed)))

                else:
                    if input_letter in vowels:
                        number_of_guesses -= 2

                    else:
                        number_of_guesses -= 1

                    letters_guessed.add(input_letter)
                    print(responses[7].format(get_guessed_word(word, letters_guessed)))

        print("-------------")


def get_file():
    """
    If the scores.txt file is in directory, open the file as read-and-write type and return the file.
    Otherwise, create a new scores.txt file and open it as read-and-write type and return it
    """
    # 'r+' means read-and-write type
    try:
        score_file = open("scores.txt", "r+")
    except FileNotFoundError:
        # 'x' means create the file
        open("scores.txt", "x")
        score_file = open("scores.txt", "r+")

    return score_file


def get_scores_dictionary():
    """
    Player names and scores are stored in a dictionary to avoid duplicate names and update player's scores
    - Creates an empty dictionary
    - Call get_file() as variable score_file and read the line and remove '\n' from the line
    - Split the player name and score from the file by their space and store in a list
    - Store the player name and score into the dictionary
    - Keep repeating until it reaches a line containing no text and return the dictionary
    """
    score_file = get_file()
    scores_dict = dict()
    while True:
        line = score_file.readline().replace("\n", "")
        if line == "":
            break

        line_list = line.split(" ")
        scores_dict[line_list[0]] = line_list[1]

    return scores_dict


def get_score(name):
    """
    Checking if name of the player is in the dictionary and return their score as an integer if true.
    Otherwise, return 0.
    """
    scores_dict = get_scores_dictionary()

    if name in scores_dict:
        return int(scores_dict[name])
    else:
        return 0


def save_score(name, score):
    """
    - Adds the player's name and score in the dictionary. Updates the player's score if name already is in dictionary
    - '.truncate' will clear all content in the file and '.seek' sets the pointer to the start of the file
        if '.seek' is not used, excessive spaces will be written into the file when writing
    - Writes the players name and score into the empty file line by line in the form '(player_name) (score)'
    """
    score_file = get_file()
    scores_dict = get_scores_dictionary()

    scores_dict[name] = score

    score_file.truncate(0)
    score_file.seek(0)

    for each_name in scores_dict:
        score_file.write("{0} {1}\n".format(each_name, scores_dict[each_name]))


def print_leaderboard():
    """ Display the leader-board in a tabular form by accessing the scores_dict and printing 'Score' and
    'Name'(10 spaces after 'Score') and printing each score and name from the dictionary below the previous print
    statement
    """
    scores_dict = get_scores_dictionary()

    print("{0} {1:>10}".format("Score", "Name"))
    print("------------------------------")
    for name in scores_dict:
        print("{0} {1:>14}".format(scores_dict[name], name))


def main():
    """
    1. Displays the welcome message to the user
    2. Use choose_random_word function to generate a random
    3. Ask the user if they want to play, view leader board or quit the game, keep prompting until the user enters
        a valid input
    4. Display the leader board, if 'l' is entered. If 'q' is entered, display a thank you message to the user and stop
        the program
    5. If 'p' is entered, ask the user for their name and convert into lower case. Get the user's previous score from
        scores.txt.(If user does not exist in scores.txt, previous score is 0)
    6. Start the hangman game obtain the player's new score after they complete the game
    7. If the new score exceeds their previous score, inform the user they reached a personal best and ask them
        if they want to save their score. Save the score if 'y' is entered and go back to step 2,
        else go back to step 2 if 'n' is entered. Keep prompting the user until they enter y or n.
    8. If new score doesn't exceed the user's previous score, go back to step 2
    9. After user quits the game. Close the scores.txt file to avoid errors with the text file
    """
    welcome_message()

    while True:
        # Generating a new word for each loop
        word = choose_random_word(word_list)

        user_option = str(input("Do you want to Play (p), view the leader-board (l) or quit (q): "))
        if user_option == "l":
            print_leaderboard()

        elif user_option == "q":
            print("Thanks for playing, goodbye!")
            break

        elif user_option == "p":
            user_name = str(input("What is your name: ")).lower()
            user_score = get_score(user_name)
            new_score = hangman(word)

            if new_score > user_score:
                while True:
                    can_save_score = str(input("A new personal best! Would you like to save your score (y/n): "))

                    if can_save_score == "y":
                        save_score(user_name, new_score)
                        print("Ok your score has been saved.")
                        break
                    elif can_save_score == "n":
                        break

    get_file().close()


if __name__ == "__main__":
    main()
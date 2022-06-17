MORSE_CODE = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"),
    ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
)


def print_intro():
    """ Display a Welcome message and an introduction to the program """
    print("Welcome to Wolmorse\nThis program encodes and decodes Morse code.")


def get_input():
    """ Get and return the user input for the mode of conversion and message to be converted(in upper case), keep
    prompting the user until they enter a valid input for the mode of conversion """
    while True:
        mode_of_conversion = str(input("Would you like to encode (e) or decode (d): "))
        if mode_of_conversion == "e" or mode_of_conversion == "d":
            message_input = input("What message would you like to encode: ")
            return mode_of_conversion, str(message_input.upper())
            break
        else:
            print("Invalid Mode")
            continue


def encode(message):
    """ To encode the message:
    1. Split each word in the message into a list by 1 space
    2. Match each character in each word with the ones in code_tuple
    3. Append the corresponding morse code into an empty string and add spaces after each character and word
    Return the encoded message """
    encoded_message = ""
    for word in message.split(" "):
        for character in word:
            for code_tuple in MORSE_CODE:
                if code_tuple[1] == character:
                    encoded_message = encoded_message + code_tuple[0] + " "
        encoded_message += "  "

    return encoded_message


def decode(message):
    """ To decode the message:
    1. Split each word in morse code into a list by 3 spaces
    2. Split each character in morse code into a list by 1 space
    3. Match each morse character with the corresponding english character from code_tuple
    4. Append the corresponding english character into an empty string and add 1 space after each word
    Return the decoded message """
    decoded_message = ""
    for morse_word in message.split("   "):
        for morse_character in morse_word.split(" "):
            for code_tuple in MORSE_CODE:
                if code_tuple[0] == morse_character:
                    decoded_message = decoded_message + code_tuple[1]
        decoded_message += " "

    return decoded_message


def process_lines(filename, mode):
    """ Open the text file as a readable file.
    Append each line in the file into a list after removing the '\n'.
    Encode or Decode each line according to the user's mode of conversion choice.
    Append the encoded/decoded lines into a list and remove spaces at the ends of each element
    Return the encoded/decoded list and close the text file afterwards """
    morse_file = open(filename, "r")

    # Using morse_file.readlines() adds each line in file into a list but adds "\n" at the end of each element
    # Removing the "\n" from the end of each element in the list
    new_list = []
    [new_list.append(each_line.replace("\n", "")) for each_line in morse_file.readlines()]  # Short-hand for loop

    # Encoding each element in the list
    encoded_decoded_list = []
    if mode == "e":
        [encoded_decoded_list.append(encode(str(message_line).upper())) for message_line in new_list]

        # Removing spaces at the ends of each element in the list
        for index in range(len(encoded_decoded_list)):
            encoded_decoded_list[index] = encoded_decoded_list[index].strip()

        return encoded_decoded_list

    # Decoding each element in the list
    else:
        [encoded_decoded_list.append(decode(str(message_line))) for message_line in new_list]

        # Removing spaces at the ends of each element in the list
        for index in range(len(encoded_decoded_list)):
            encoded_decoded_list[index] = encoded_decoded_list[index].strip()

        return encoded_decoded_list

    morse_file.close()


def write_lines(lines):
    """ Open/Create and open a file named result.txt
    Convert each element in the lines list to a string and add '\n' to the end of each element
    Write each element into the result_file and close it afterwards """
    result_file = open("results.txt", "w")
    for element in lines:
        result_file.write(str(element) + "\n")
    result_file.close()


def check_file_exists(filename):
    """ Attempt to open the text file with 'filename'
    Return True if it opens(file is in directory
    Return False if it raises the error FileNotFoundError(file is not in directory) """
    try:
        open(filename)
    except FileNotFoundError:
        return False
    else:
        return True


def get_filename_input():
    """ Ask the user if they want to encode or decode and if they want to read from a file or use the console.
        Keep prompting until enters valid inputs.
    If the user wants to read from a file, keep prompting them for a valid filename in the directory
    If user wants to use the console, ask for the message they want to encode/decode
    Return the mode of conversion, user's message and file name
    User's message will return as None if user chooses to read a file,
    Similarly, the filename will return as None if user chooses to use the console """
    while True:
        message_input = ""
        mode_of_conversion = str(input("Would you like to encode (e) or decode (d): "))
        if mode_of_conversion == "e" or mode_of_conversion == "d":
            file_console_option = str(input("Would you like to read from a file(f) or the console(c)? "))
            if file_console_option == "f" or file_console_option == "c":
                if file_console_option == "f":
                    while True:
                        file_name = str(input("Enter a filename: "))
                        if check_file_exists(file_name):
                            message_input = None
                            print("Output written to results.txt")
                            break
                        else:
                            print("Invalid Filename")
                            continue
                else:
                    message_input = str(input("What message would you like to encode: ").upper())
                    file_name = None
            else:
                continue

            return mode_of_conversion, message_input, file_name
            break
        else:
            print("Invalid Mode")
            continue


def main():
    """
    1. Display the welcome message and introduction of the program
    2. Use function get_filename_input() to decide whether to encode or decode a message or file
    3. Display the encoded/decoded message or write them in a text file
    4. Ask the user if they want to encode/decode another message, keep prompting until a valid input is entered
    5. If yes, return to step 2. Else, display a goodbye message and stop the program """
    print_intro()

    while True:
        # Store returning values from get_input() into the following variables
        mode_of_conversion, message_input, file_name = get_filename_input()
        if mode_of_conversion == "e":
            if file_name is None:
                print(encode(str(message_input)))
            else:
                write_lines(process_lines(file_name, mode_of_conversion))
        else:
            if file_name is None:
                print(decode(str(message_input)))
            else:
                write_lines(process_lines(file_name, mode_of_conversion))

        user_repeat_process = str(input("Would you like to encode/decode another message? (y/n): "))
        while user_repeat_process != "y" and user_repeat_process != "n":
            user_repeat_process = str(input("Would you like to encode/decode another message? (y/n): "))

        if user_repeat_process == "y":
            continue
        else:
            break
    print("Thanks for using the program, goodbye!")


if __name__ == '__main__':
    main()
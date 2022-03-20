HANGMAN_ASCII_ART = """
 _    _  
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __ 
|  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | | 
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  
                     __/ |            
                    |___/     """


def hangman_art(HANGMAN_ASCII_ART):
    """this function showing the 'hangman' sketch
    :param HANGMAN_ASCII_ART: sketch.
    :type HANGMAN_ASCII_ART: str.
    :return: the sketch.
    """
    return HANGMAN_ASCII_ART


HANGMAN_PHOTOS = {"picture1": """
x-------x
""",
                  "picture2": """ 
x-------x
|
|
|
|
|""",
                  "picture3": """   
x-------x
|       |
|       0
|
|
|""",
                  'picture4': """
x-------x
|       |
|       0
|       |
|
|""",
                  'picture5': """ 
x-------x
|       |
|       0
|      /|\ 
|
|""",
                  'picture6': """
x-------x
|       |
|       0
|      /|\ 
|      /
|""",
                  'picture7': """ 
x-------x
|       |
|       0
|      /|\ 
|      / \ 
|"""}


num_of_tries = 0
MAX_TRIES = 6
# how many times the user can fail.

print(hangman_art(HANGMAN_ASCII_ART))
old_letters_guessed = []
file = input("Please enter a file path: ")
file_path = open(file, "r")
file_content = file_path.read()
index = int(input("Enter a number(represent the chosen secret word): "))
print("Let's start !")
print(HANGMAN_PHOTOS["picture1"])


def choose_word(file_path, index):
    """this function defines to the player which word will be the secret word for guessing.
    :param file_path: File path to the secret's words.
    :param index: Word placement in the file path.
    :type file_path: str
    :type index: int
    :return: tuple with two element
    :rtype: tuple
    """
    file1 = file_content.split(" ")
    pose = (index - 1) % len(file1)
    secret_word1 = file1[pose]
    return secret_word1


secret_word = str(choose_word(str(file_path), index))
len_sentence = len(secret_word)
string = int(len_sentence) * "_ "
print(string + '\n')
letter_guessed = input("Guess a letter: ").lower()


def is_valid_input(letter_guessed):
    """this function present if letter guessed is valid.
       :param letter_guessed: Represents the letter from the player.
       :type letter_guessed: str.
       :return: if the letter is true.
       :rtype: bool."""
    if len(letter_guessed) > 1:
        return False
        pass
    elif letter_guessed.isspace() and letter_guessed.isnumeric and letter_guessed.isdigit:
        return False
        pass
    elif letter_guessed.isascii() and not letter_guessed.isalpha():
        return False
        pass
    else:
        return True


def check_valid_input(letter_guessed, old_letters_guessed):
    """this function will check if the letter is true so the letter will save in a new list.
       :param letter_guessed: Represents the letter from the player.
       :param old_letters_guessed: A list  containing the letters the player has guessed already.
       :type letter_guessed: str.
       :type old_letters_guessed: list.
       :return: if the letter is true.
       :rtype: bool."""
    if not is_valid_input(letter_guessed):
        return False
    elif is_valid_input(letter_guessed) and is_valid_input(letter_guessed) not in old_letters_guessed:
        if old_letters_guessed.count(letter_guessed) == 1:
            return True



def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """the function add the new letter to the list or write an error if the letter already in the list.
    :param letter_guessed: Represents the letter from the player.
    :param old_letters_guessed: A list  containing the letters the player has guessed already.
    :type letter_guessed: str.
    :type old_letters_guessed: list.
    :return if the letter is in the list
    :rtype bool
    """
    if not is_valid_input(letter_guessed) or check_valid_input(letter_guessed,old_letters_guessed):
        separator = " -> "
        print(f'X\n{separator.join(sorted(old_letters_guessed))}')
        return False
        pass
    else:
        old_letters_guessed.append(letter_guessed)
        return True



def show_hidden_word(secret_word, old_letters_guessed):
    """the function shows the player his progress in guessing the secret word.
    :param secret_word: the string represents the secret word the player has to guess.
    :param old_letters_guessed:the list contains the letters the player has guessed so far.
    :type secret_word: str
    :type old_letters_guessed: list
    :return:
    :rtype: str."""
    secret_word_string = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            secret_word_string += letter + " "
        else:
            secret_word_string += "_ "
    return secret_word_string


def check_win(secret_word, old_letters_guessed):
    """ the function checks if the player has guessed the secret word.
    :param secret_word: the string represents the secret word the player has to guess.
    :param old_letters_guessed:the list contains the letters the player has guessed so far.
    :type secret_word: str
    :type old_letters_guessed: list
    :return: If all the letters compose the secret word and included in the list old_letters that the user guessed
    :rtype: bool."""
    if "_ " not in show_hidden_word(secret_word, old_letters_guessed):
        return True
    else:
        return False


win = check_win(secret_word, old_letters_guessed)


def print_hangman(num_of_tries):
    """this function is counting how many times the player tried
    :param num_of_tries: how many times
    :type num_of_tries: int
    :return:
    """
    global HANGMAN_PHOTOS
    if num_of_tries == 0:
        print(HANGMAN_PHOTOS['picture1'])
        pass
    elif num_of_tries == 1:
        print(HANGMAN_PHOTOS['picture2'])
        pass
    elif num_of_tries == 2:
        print(HANGMAN_PHOTOS['picture3'])
        pass
    elif num_of_tries == 3:
        print(HANGMAN_PHOTOS['picture4'])
        pass
    elif num_of_tries == 4:
        print(HANGMAN_PHOTOS['picture5'])
        pass
    elif num_of_tries == 5:
        print(HANGMAN_PHOTOS['picture6'])
        pass
    elif num_of_tries == 6:
        print(HANGMAN_PHOTOS['picture7'])
    return None


if letter_guessed not in secret_word and is_valid_input(letter_guessed):
    print(":(")
    num_of_tries += 1
    print_hangman(num_of_tries)


def main():
    hangman_art(HANGMAN_ASCII_ART)
    global num_of_tries, MAX_TRIES, letter_guessed
    is_valid_input(letter_guessed)
    check_valid_input(letter_guessed, old_letters_guessed)
    try_update_letter_guessed(letter_guessed, old_letters_guessed)
    print(show_hidden_word(secret_word, old_letters_guessed))
    while True:
        if check_win(secret_word, old_letters_guessed):
            print('WIN')
            break
        else:
            letter_guessed = input('Guess a letter: ')
            is_valid_input(letter_guessed)
            check_valid_input(letter_guessed, old_letters_guessed)
            try_update_letter_guessed(letter_guessed, old_letters_guessed)
            print(show_hidden_word(secret_word, old_letters_guessed))
            if check_win(secret_word, old_letters_guessed):
                print('WIN')
                break
            if letter_guessed not in secret_word and is_valid_input(letter_guessed):
                print(":(")
                num_of_tries += 1
                print_hangman(num_of_tries)

            if num_of_tries == MAX_TRIES:
                print("Sorry, you FAILED")
                break


if __name__ == "__main__":
    main()


file_path.close()
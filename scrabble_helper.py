#******************************************************************************#
#                                                                              #
#                        TABIND scrabble project                               #
#                                                                              #
#******************************************************************************#
#                                                                              #
# FILE: Tabind scrabble project                                                #
#                                                                              #
# USAGE: Tabind scrabble project                                               #
#                                                                              #
# DESCRIPTION: Gegerates all valid Scrabble words from a set                   #
#              of given letters, in this case "TABIND"                         #
#                                                                              #
# OPTIONS: List options for the script [-h]                                    #
#                                                                              #
# DEVELOPER: Zhaoyu Li                                                         #
# DEVELOPER PHONE: +1 (530) 234-2513                                           #
# DEVELOPER EMAIL: bruce040729@gmail.com                                       #
#                                                                              #
# VERSION: 1.0                                                                 #
# CREATED DATE-TIME: 20240809-10:00 Western Time Zone USA                      #
#                                                                              #
# VERSION: 1.1                                                                 #
# REVISION DATE-TIME: YYYYMMDD-HH:MM                                           #
# DEVELOPER MAKING CHANGE: First_name Last_name                                #
# DEVELOPER MAKING CHANGE: PHONE: +1 (XXX) XXX-XXXX                            #
# DEVELOPER MAKING CHANGE: EMAIL: first.last@email.com                         #
#                                                                              #
#******************************************************************************#

import itertools

# Load the dictionary of valid words
def load_dictionary(filepath):
    with open(filepath, 'r') as file:
        valid_words = set(word.strip().lower() for word in file)
    return valid_words

# Generate all permutations of the given letters
def generate_permutations(letters):
    permutations = set(
        ''.join(p) for i in range(2, len(letters) + 1)
        for p in itertools.permutations(letters, i)
    )
    return permutations

# Filter permutations to find valid words
def filter_valid_words(permutations, valid_words):
    return sorted(word for word in permutations if word in valid_words)

if __name__ == "__main__":
    # Path to the downloaded Scrabble dictionary file
    dictionary_path = "C:\\python\\dictionary.txt"
    
    letters = "tabind"
    
    try:
        valid_words = load_dictionary(dictionary_path)
        permutations = generate_permutations(letters)
        valid_scrabble_words = filter_valid_words(permutations, valid_words)
        
        if valid_scrabble_words:
            print(f"Valid Scrabble words from '{letters}':")
            for word in valid_scrabble_words:
                print(word)
        else:
            print(f"No valid Scrabble words found for the letters '{letters}'.")
    except FileNotFoundError as e:
        print(f"Dictionary file not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

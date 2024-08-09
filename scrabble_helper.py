import itertools

# Load the dictionary of valid words
def load_dictionary(filepath):
    with open(filepath, 'r') as file:
        valid_words = set(word.strip().lower() for word in file)
    return valid_words

# Generate all permutations of the given letters
def generate_permutations(letters):
    # Generate permutations for 2 or more letters
    permutations = set(
        ''.join(p) for i in range(2, len(letters) + 1)
        for p in itertools.permutations(letters, i)
    )
    
    # Manually add "A" and "I" to the set of permutations
    if 'a' in letters:
        permutations.add('a')
    if 'i' in letters:
        permutations.add('i')
    
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
        
        # Directly check if 'a' and 'i' are in valid words
        single_letter_words = [letter for letter in ['a', 'i'] if letter in valid_words and letter in letters]
        
        permutations = generate_permutations(letters)
        valid_scrabble_words = filter_valid_words(permutations, valid_words)
        
        # Include single letter words 'a' and 'i' explicitly
        valid_scrabble_words = single_letter_words + valid_scrabble_words
        
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

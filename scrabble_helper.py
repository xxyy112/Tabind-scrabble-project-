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
            for word in valid_scrabble_words:
                print(word)
        else:
            print("No valid Scrabble words found.")
    except FileNotFoundError as e:
        print(e)

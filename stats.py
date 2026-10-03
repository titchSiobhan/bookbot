def get_num_words(text):
    words = text.split()
    word_length = len(words)
    return f"Found {word_length} total words"

def char_counter(text):
    char_counting:{str, int} = {}
   
    
    for char in text:
        letter = char.lower()
        if letter not in char_counting:
            if not letter.isalpha():
                continue
            char_counting[letter] = 0
        char_counting[letter] += 1

    
    return char_counting

def chars_dict_to_sorted_list(char_counting: dict[str, int]) -> list[tuple[str, int]]:
    sorted_chars = []

    def sort_on(item: tuple[str, int]) -> int:
        return item[1]
    
    sorted_chars = sorted(char_counting.items(), key=sort_on, reverse=True)
    return sorted_chars

import sys
from stats import get_num_words
from stats import char_counter
from stats import chars_dict_to_sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

    

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
   
    num_of_words = get_num_words(text)
    char_counting = char_counter(text)
    char_list = chars_dict_to_sorted_list(char_counting)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(num_of_words)
    print("--------- Character Count -------")
    for char in char_list:
        print(f"{char[0]}: {char[1]}")
    print("============= END ===============")
    

main()

"""
python3 main.py books/frankenstein.txt
python3 main.py books/prideandprejudice.txt
python3 main.py books/mobydick.txt

"""
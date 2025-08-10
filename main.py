import sys

from stats import get_num_words,get_num_char,chars_dict_to_sorted_list

def main():
    book_path = ""
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_num = get_num_char(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_num)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):
    with open(path) as book:
        return book.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()






    
    


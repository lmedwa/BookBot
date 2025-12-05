import sys
from stats import get_num_words
from stats import count_characters
from stats import sorted_list


def get_book_text(path_to_file):	
	with open(path_to_file) as f:
		file_contents = f.read()
        
		return file_contents


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    path = sys.argv[1]

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    text = get_book_text(path)
    

    print('----------- Word Count ----------')
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    
    print('--------- Character Count -------')
    num_char = count_characters(text)
    sorted_chars = sorted_list(num_char)
    
    for characters in sorted_chars:
        char = characters['char']
        num = characters['num']
        if char.isalpha():
            print(f'{char}: {num}')
    
    print('============= END ===============')


main()


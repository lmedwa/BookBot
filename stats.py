def get_book_text(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()

                return file_contents

def get_num_words(text):
        words = text.split()
        num_words = len(words)
        return num_words

def count_characters(text):
	low_character = text.lower()
	char_count = {}
	for character in low_character:
		if character.isalpha():
			if character in char_count:
				char_count[character] += 1
			else:
				char_count[character] = 1
	return char_count

def sort_on(characters):
	return characters['num']

def sorted_list(count_characters):
	sorted_list = []
	for character, char_count in count_characters.items():
		new_dict_item = {'char': character, 'num': char_count}
		sorted_list.append(new_dict_item)
	
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list

def main():
        text = get_book_text("books/frankenstein.txt")
        print(text)
        num_words = get_num_words(text)
        print(f"Found {num_words} total words")

main()

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("book_path", help="This is the file path to your .txt file")
    args = parser.parse_args()
    text, error = get_book_text(args.book_path)
    if error:
        print(error)
    elif text is not None:
        words = text.split()
        word_count = get_word_count(words)
        character_count = get_char_count(words)
        frequency_list = create_char_frequency_list(character_count)
        generate_report(args.book_path, word_count, frequency_list)


def get_book_text(path):
    try:
        if path.endswith(".txt"):
            with open(path) as f:
                return f.read(), None
        else:
            raise TypeError
    except FileNotFoundError:
        return None, "File not found"
    except TypeError:
        return None, "File is not of text type"


def get_word_count(words):
    return len(words)


def get_char_count(words):
    character_count = {}
    for word in words:
        for character in word:
            lowercase_char = character.lower()
            if lowercase_char in character_count:
                character_count[lowercase_char] += 1
            else:
                character_count[lowercase_char] = 1
    return character_count


def sort_on(dict_to_sort):
    return dict_to_sort["count"]


def create_char_frequency_list(char_dict):
    character_report = []
    for index in char_dict:
        if index.isalpha():
            character_report.append({"char": index, "count": char_dict[index]})
    character_report.sort(reverse=True, key=sort_on)
    return character_report


def generate_report(book_path, word_count, frequency_list):
    print(f"--- Report of {book_path} ---")
    print(f"Word count of doc is: {word_count}\n")
    for item in frequency_list:
        print(f"{item['char']} was found {item['count']} times")
    print("--- End report ---")


main()

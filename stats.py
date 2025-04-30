
def get_num_words(book_text):
    num_words = len(book_text.split())
    return num_words

def get_num_characters(book_text):
    characters = {}

    for i in book_text:
        char = i.lower()
        if (char in characters):
            characters[char] += 1
        else:
            characters[char] = 1

    return characters

def sort_dict_char_count(dict):
    return dict["num"]

def format_dict(dict):
    char_list = []

    for i in dict:
        char_list.append({"char": i, "num": dict[i]})
    char_list.sort(reverse=True, key=sort_dict_char_count)
    return char_list
    
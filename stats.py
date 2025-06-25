def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    letters = {}
    text = text.lower()
    for char in text:
        letters[char] = letters.get(char, 0) + 1
    return letters

def sort_dict(dict):
    sorted_list = [{"char": char, "num": count} for char, count in dict.items()]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
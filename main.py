def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    report = get_report(chars_dict, book_path, num_words)
    



def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
  
def get_report(chars_dict, book, num_words):
    
    book = book.replace("books/", '').replace(".txt", '')
    

    print("----Begin report of " + book.title() + "----")
    print(f"{num_words} words found in document")
    print()

    for key in sorted(chars_dict, key=chars_dict.get, reverse=True):
        if key.isalpha():
          print(f"The letter {key} was found {chars_dict[key]} times")
    print("--------- End Report -----------")
    
    

        
        


main()
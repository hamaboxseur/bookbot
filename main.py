def main():
    book_path = ".gitignore/books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    num = count_word(text)
    print(f"the number word is : {num}")


def count_word(text):
    tab = text.split()
    return len(tab) 

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
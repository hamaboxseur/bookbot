def main():
    book_path = ".gitignore/books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    num = count_word(text)
    print(f"the number word is : {num}")
    tab = count_lettre(text)
    print(f"the dictionary is : {tab}")


def count_word(text):
    tab = text.split()
    return len(tab) 
def count_lettre(text):
    dic = {}
    text = text.lower()
    for i in text:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1

        
    return dic
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
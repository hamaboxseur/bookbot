def main():
    book_path = ".gitignore/books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- being report of {book_path}---")
    num = count_word(text)
    print(f"{num} word found in the document")
    print ()
    show_dic(text)
    print(' ')
    print('--- end of report ---')

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

def show_dic(text):
    tab = count_lettre(text)
    for i in sorted(tab):
        if i.isalpha():
            print(f"the {i} character was found   {tab[i]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
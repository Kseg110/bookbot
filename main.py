# See ref doc in google drive for steps followed and different syntax 

# define main function below w/ variables defined 
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

# define function to split words on whitespace for counting
def get_num_words(text):
    words = text.split()
    return len(words)

# define function to open, read and count file
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
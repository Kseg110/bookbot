# See ref doc in google drive for steps followed and different syntax 

# define main function below w/ variables defined 
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)

# define function to split words on whitespace for counting
def get_num_words(text):
    words = text.split()
    return len(words)

# NEW function defined for counting charachters
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# define function to open, read and count file
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
# See ref doc in google drive for steps followed and different syntax 

# define main function below w/ variables defined 
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

# convert dictionary to list of dictionaries
    char_list = [] 
    for char, num in chars_dict.items():
        char_list.append({"char": char, "num": num})
# sort the list by frequency
    char_list.sort(reverse=True, key=sort_on)
# now print the report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
# loop to print each charachter and the stats with f string to format body of report
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    print("--- End report ---")

# define function to split words on whitespace for counting
def get_num_words(text):
    words = text.split()
    return len(words)

# function defined for counting uniqe charachters 
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha(): # added condition - only counts it if it's a letter
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

# define function to open and read file/path
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
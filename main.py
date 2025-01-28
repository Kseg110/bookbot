# See ref doc in google drive for steps followed
def main():
    with open("books/frankenstein.txt") as f: 
        file_contents = f.read()
        print(file_contents) #print the contents of the file
# defined function main to open and read

# below = standard python idiom to ensure main only runs when script is executed directly
if __name__ == "__main__":
    main()

import sys

def main(filename):
    with open(filename) as fh:
        text = fh.read()
        # print(text)
        
        char_counter = len(text)
        line_counter = text.count("\n") + 1
        word_counter = len(text.split())

        print(f"Number of characters in file: {char_counter}")
        print(f"Number of lines in file: {line_counter}")
        print(f"Number of words in file: {word_counter}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} FILENAME")
    else:
        main(sys.argv[1])
import sys

def char_count(text):
    return len(text)

def line_count(text):
    return text.count("\n") + 1

def word_count(text):
    return len(text.split())

def main(filename):
    with open(sys.argv[1]) as file:
        text = file.read()
        
        char_counter = char_count(text)
        line_counter = line_count(text)
        word_counter = word_count(text)

        print(f"Character count: {char_counter}")
        print(f"Line count: {line_counter}")
        print(f"Word count: {word_counter}")

# main(sys.argv[1])
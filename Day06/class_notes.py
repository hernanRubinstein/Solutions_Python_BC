import sys
from my_function_lib import process_file

def main():
    print("Executing main() from class_notes.py")
    # print(sys.argv)
    for filename in sys.argv[1:]:
        try:
            process_file(filename)

        # except FileNotFoundError:
        #     print(f"File {filename} not found")
        # except ZeroDivisionError:
        #     print("Cannot divide by zero")
            # break

        except Exception as error:
            print(f"An error occurred: {error}")
main()
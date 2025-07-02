from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

if __name__ == "__main__":

    print(get_file_content("calculator", "main.py"))
    print()
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()
    print(get_file_content("calculator", "/bin/cat"))
    print()
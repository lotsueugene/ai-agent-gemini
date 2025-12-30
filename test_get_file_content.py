from functions.get_file_content import get_file_content
from config import MAX_CHARS



def test_get_file_content():
    lorem_result = get_file_content("calculator", "lorem.txt")
    print(len(lorem_result))          # see how long the returned string is
    print(lorem_result[-120:])        # look at the end: should include the truncation message

    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    
    test_get_file_content()
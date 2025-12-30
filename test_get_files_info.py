from functions.get_files_info import get_files_info



def test_get_files_info():
    print(get_files_info("calculator", "."))
    print('\n')
    print(get_files_info("calculator", "pkg"))
    print('\n')
    print(get_files_info("calculator", "/bin"))
    print('\n')
    print(get_files_info("calculator", "../"))


if __name__ == "__main__":
    test_get_files_info()
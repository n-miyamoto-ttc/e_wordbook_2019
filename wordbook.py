# coding= utf-8


def print_txt(file_dir):
    with open(file_dir, "r", encoding="utf-8") as f:
        first_str = f.readline()
        return first_str


def main():
    print(print_txt("input/article1.txt"))


if __name__ == '__main__':
    main()
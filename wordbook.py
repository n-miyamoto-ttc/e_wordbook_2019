# coding= utf-8


def print_txt(file_dir):
    with open(file_dir, "r", encoding="utf-8") as f:
        first_str = f.readline()
        return first_str


def main():
    print("私は英単語帳アプリです。")
    print("私は秋田若奈です\n")

if __name__ == '__main__':
    main()




with open("kari.txt","r",encoding = "utf-8") as f:
    kari_text = f.read()

import re


kari = []
moji = re.findall("\D\w+",kari_text)
for s in moji:
    kari.append(s.lower())


print(kari)
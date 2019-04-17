# coding= utf-8


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
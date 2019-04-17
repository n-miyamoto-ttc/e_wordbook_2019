# coding= utf-8
import re
from collections import Counter
def main():
    print("私は英単語帳アプリです。")
    f = open("input\\article1.txt","r",encoding="utf-8")
    fr = f.read()
    words = re.split("\\s|\,|\.|\(|\)|\-|[0-9]", fr.lower())
    print(words)
    counter = Counter(words)
    print(counter)
    for word, count in counter.most_common():
        if len(word) > 0:
            print("%s,%d" % (word, count))

if __name__ == '__main__':
    main()
# 読み込んだデータを表示
f = open("article1.txt","r",encoding="UTF-8")
txt = f.read()
# print(txt)

# wantに(入力した分)出力させる
want = int(input("上位何位まで表示させますか?(数字のみ入力)>>>"))

# カウント
words = {}
for word in txt.split():
    words[word] = words.get(word, 0) + 1

# カウント回数でソート
d = [(a,b) for b,a in words.items()]
d.sort()
d.reverse()
print("********************************")
print("単語"'\t'"出現回数"'\t'"意味")
print("********************************")
mean=""
for cnt, word in d[:want]:
    print(word,'\t',cnt,'\t')
    mean = input("意味を入力>>>")
    print(word,'\t',cnt,'\t',mean)
    print('\n')
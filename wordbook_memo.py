import re
import json
# import collections as cl

# 読み込んだデータを表示
f = open("article1.txt","r",encoding="UTF-8")
txt = f.read()
f.close()

# （自分のアドバンス)wantに(入力した分)出力させる
# want = int(input("上位何位まで表示させますか?(数字のみ入力)>>>"))

# カウント
wordcount = {}
for word in txt.split():
    wordcount[word] = wordcount.get(word, 0) + 1

# カウント回数でソート(内包表記)
d = [(kazu,word) for word,kazu in wordcount.items()]
d.sort(reverse = True)

mean = []
i = 1
print("********************************")
print("単語"'\t'"出現回数"'\t'"意味")
print("********************************")

word_dict = {}
# 10を上記のwantに変えれば欲しい個数に変更可能
for cnt, word in d[:10]:
    print(i,"番目に多い英単語",word,'\t')
    mean = (input("意味を入力>>>"))
    vlist = [word, mean]
    word_dict[cnt] = vlist
    i+=1
    # print(word,'\t',cnt,'\t',mean)
    # json.dump(word,cnt,mean)
print(word_dict)

f = open("memo.json","w",encoding="UTF-8")
json.dump(word_dict,f)
f.close()
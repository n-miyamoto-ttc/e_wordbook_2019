import sys
import re
import json

# 読み込んだデータを表示 (例外:ファイルがないとき)
try:
    # \ufeff(ボム)が1つ数えられていたため、utf-8-sigに変更
    f = open("article1.txt","r",encoding="UTF-8-sig")
    txt = f.read()
    f.close()
except FileNotFoundError:
    print("--------------------------------")
    print("Error:存在していないtxtデータです")
    print("読み込みたいtxtデータを確認してください")
    print("--------------------------------")
    sys.exit()

# txtデータに何も入っていなかったときの処理
if txt == " ":
    print("--------------------------------")
    print("Error:このtxtデータには何もはいっていません")
    print("--------------------------------")
    sys.exit()

# （自分のアドバンス)wantに(入力した分)出力させる (例外:数字以外)
try:
    want = int(input("上位何位まで表示させますか?(数字のみ入力)>>>"))
except ValueError:
    print("--------------------------------")
    print("Error:数字以外の入力は受け付けません")
    print("--------------------------------")
    sys.exit()

# 変換
texts = re.split(r'\s|\,|\.|\(|\\|\-|\)|\'',txt.lower())

# 文字をキーに 数をバリューにしたdict(wordcount)
wordcount = {}
for word in texts:
    # 除けなかった空白をここで除くことにする
    if word != '':
        wordcount[word] = wordcount.get(word, 0) + 1
    else:
        None
# 英単語がちゃんと表示されているか確認
# print(wordcount)

# カウント回数でソート(内包表記) 数をキーにして、英単語を値に
kazuword = [(kazu,word) for word,kazu in wordcount.items()]
kazuword.sort(reverse = True)

i = 1
mean = []
word_dict = {}

# 10を上記のwantに変えれば欲しい個数に変更可能
for cnt, word in kazuword[:want]:
    print(i,"番目に多い英単語",word,'の意味を入力')
    mean = (input(">>>"))
    if mean == " " or mean == "" or mean == "　":
        print("--------------------------------")
        print("Error:未入力や空文字は使えません")
        print("もう一度入力しなおしてください")
        print("--------------------------------")
        sys.exit()
    vlist = [word, mean]
    word_dict[cnt] = vlist
    i+=1
    # print(word,'\t',cnt,'\t',mean)
    # json.dump(word,cnt,mean)

print("********************************")
print("出現回数['単語','意味']")
print("********************************")
for key,val in word_dict.items():
    print(key,"回","\t",val)

f = open("memo.json","w",encoding="UTF-8")
# jsonはunicode出力するためensure_asciiで解決,indentで見やすく
json.dump(word_dict,f,ensure_ascii=False,indent=4,separators=(',', ': '))
f.close()
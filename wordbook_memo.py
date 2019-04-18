import sys
import re
import json

# [入力]読み込んだデータを表示 (例外:ファイルがないとき)
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
if txt == "":
    print("--------------------------------")
    print("Error:このtxtデータには何もはいっていません")
    print("--------------------------------")
    sys.exit()

# （塩崎アドバンス)wantに(入力した分)出力させる (例外:数字以外)
try:
    want = int(input("上位何位まで表示させますか?(数字のみ入力)>>>"))
except ValueError:
    print("--------------------------------")
    print("Error:数字以外の入力は受け付けません")
    print("--------------------------------")
    sys.exit()

# [機能:切り出す]区低区切り文字で切り出し、数字を除き、小文字に変換する
texts = re.split(r'\s|\,|\.|\(|\\|\-|\)|\'|\d+',txt.lower())

# キー(文字):バリュー(数)にしたdict(wordcount)
wordcount = {}
for word in texts:
    # [機能]で除けなかった空白をここで除くことにした
    if word != '':
        # [機能:出現回数を求める]getメソッドでキー(文字)に割り当てられた値に+1していく(これが出現回数)
        wordcount[word] = wordcount.get(word, 0) + 1
    else:
        # 説明できないので復習する
        None
# 英単語が"全部"ちゃんと表示されているか確認(テスト用)
# print(wordcount)

# P235,236
# [機能:出現回数でソート]カウント回数でソート(内包表記) 数をキーにして、英単語を値にする
kazuword = [(kazu,word) for word,kazu in wordcount.items()]
kazuword.sort(reverse = True)

# 用意
i=1
mean = []
word_dict = {}

# [塩崎アドバンス]wantによって欲しい個数に変更可能(実際は10)
for cnt, word in kazuword[:want]:
    # [機能:英単語の日本語訳を聞く]wantで指定された回数、単語の意味を聞く
    print(i,"番目に多い英単語",word,'の意味を入力')
    mean = (input(">>>"))
    # 空文字やEnter入力されたときはプログラム終了(実はエラーじゃない)
    if mean == " " or mean == "" or mean == "　":
        print("--------------------------------")
        print("Error:未入力や空文字は使えません")
        print("もう一度入力しなおしてください")
        print("--------------------------------")
        sys.exit()
    # リストに[英単語,意味]を追加していく
    vlist = [word, mean]
    # [機能:英単語一覧]cnt(出現回数)をキーにしたdictの値にリストを追加する
    word_dict[cnt] = vlist
    i+=1

print("********************************")
print("出現回数['英単語','意味']")
print("********************************")

#　[出力]keyは出現回数 valは[英単語,意味] キーと値を取り出す (P195)
for key,val in word_dict.items():
    print(key,"回","\t",val)
print("********************************")

f = open("memo.json","w",encoding="UTF-8")
# [ファイル出力]
# jsonはunicode出力するためensure_asciiで解決 separateとは? (P407)
json.dump(word_dict,f,ensure_ascii=False,indent=4,separators=(',', ': '))
f.close()
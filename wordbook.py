# coding= utf-8
# インポート：正規表現・json
import re
import sys
import json
import os

def main():
    print("start")
if __name__ == "__main__":
    main()

# ーーーーーー英単語帳アプリーーーーーー
try:    # ファイルの読み込み
    with open("input\\article1.txt","r",encoding = "utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print("ファイルが存在しないか別のフォルダに入っています")
    sys.exit()

# ファイルから英単語の抽出・小文字にする
l_moji = []
l_moji = re.findall("\w[a-z]+",text.lower())

mojicount = {}  # 数を数えて辞書の作成（setを使用）
if not l_moji:
    print("ファイルの中身がない、または英単語がファイルに入っていません")
    sys.exit()
else:
    for content in set(l_moji):
        mojicount[content] = l_moji.count(content)

#（個数＞a-z)降順に並び替え、トップ１０をリストにする
hight = list(sorted(mojicount.items(),key = lambda x:(-x[1],x[0]))[:10])

# 意味の初期値を定義、ディクショナリの作成、
mean = "回出現。訳：日本語訳を入力してください"
d_hight = dict(hight)
for k,v in d_hight.items():
    d_hight[k] = str(v).rjust(5," ") + mean

# 作成のオブジェクト
def sakusei():
    print("\n-----出現頻度の高い英単語TOP10-----")
    print("リストを作成します")
    print("まずは日本語訳を記入してください")
    for d in d_hight:
        print(d)
        ja = input()
        if ja == "":
            pass
        else:
            d_hight[d] = d_hight[d][:11] + ja
    print("\n-----出現頻度の高い英単語TOP10-----")
    print("英単語" + "\n頻出回数と日本語訳")
    print("-----------------------------------")
    for d in d_hight:
        print(d,"\n",d_hight[d])
    print("---------------終了----------------\n")
    # jsonファイルに書き込み
    with open ("word.json","w",encoding="utf-8") as f:
        json.dump(d_hight,f,indent = 4, ensure_ascii=False)

# 更新オブジェクト
def kousin():
    print("日本語訳を記入してください")
    with open ("word.json","r",encoding="utf-8") as f:
        nd_hight = json.load(f)
    for nd in nd_hight:
        print(nd)
        ja = input()
        if ja == "":
            pass
        else:
            nd_hight[nd] = nd_hight[nd][:11] + ja
    # jsonファイルに書き込み
    with open ("word.json","w",encoding="utf-8") as f:
        json.dump(nd_hight,f,indent = 4, ensure_ascii=False)
    hyouji()

# 表示オブジェクト
def hyouji():
    with open ("word.json","r",encoding="utf-8") as f:
        nd_hight = json.load(f)
    print("\n-----出現頻度の高い英単語TOP10-----")
    print("英単語" + "\n頻出回数と日本語訳")
    print("-----------------------------------")
    for nd in nd_hight:
        print(nd,"\n",nd_hight[nd])
    print("---------------終了----------------\n")

# 誘導コード
if os.path.getsize("word.json") < 10:
    sakusei()
else:
    print("\nメニューを入力してください")
    print("一覧 or 更新 or 終了")
    menu = input()
    if menu == "更新":
        kousin()
    elif menu == "一覧":
        hyouji()
    elif menu == "終了":
        print("終了します")
    else:
        print("無効な入力です。終了します")
# coding= utf-8

def print_txt(file_dir):
    with open(file_dir, "r", encoding="utf-8") as f:
        first_str = f.readline()
        return first_str

def main():
    print("\n私は英単語帳アプリです。")
    #print("私は秋田若奈です\n")

if __name__ == '__main__':
    main()



#ーーーーーー英単語帳アプリーーーーーー
#ファイルの読み込み
with open("input\\article1.txt","r",encoding = "utf-8") as f:
    text = f.read()
#インポート：正規表現・json
import re
import json



#l_moji = [] #ファイルから英単語の抽出・小文字にする
l_moji = re.findall("\w[a-z]+",text.lower())

mojicount = {}  #数を数えて辞書の作成（setを使用）
for content in set(l_moji):
    mojicount[content] = l_moji.count(content)

hight = list(sorted(mojicount.items(),key = lambda x:(-x[1],x[0]))[:10])    #（個数＞a-z)降順に並び替え、トップ１０をリストにする

#意味の初期値を定義、ディクショナリの作成、
mean = "回出現。訳：日本語訳を入力してください"
d_hight = dict(hight)
for k,v in d_hight.items():
    d_hight[k] = str(v).rjust(5," ") + mean

#メニューの表示と入力
print("\nメニューを入力してください")
print("一覧 or 更新 or 終了")
menu = input()

def hyouji():   #英単語一覧の出力
    print("\n-----出現頻度の高い英単語TOP10-----")
    print("英単語" + "\n頻出回数と日本語訳")
    for d in d_hight:
        print(d,"\n",d_hight[d])
    print("---------------終了----------------\n")

if menu == "更新":  #誘導コード
    print("日本語訳を記入してください")
    for d in d_hight:
        print(d[0])
        ja = input()
        if ja == "":
            pass
        else:
            d_hight[d] = d_hight[d][:11] + ja
    hyouji()
elif menu == "一覧":
    hyouji()
elif menu == "終了":
    print("終了します")
else:
    print("無効な入力です。終了します")

    #jsonファイルに書き込み
with open ("word.json","w",encoding="utf-8") as f:
    json.dump(d_hight,f,indent = 4, ensure_ascii=False)
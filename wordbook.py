# coding= utf-8

def print_txt(file_dir):
    with open(file_dir, "r", encoding="utf-8") as f:
        first_str = f.readline()
        return first_str

def main():
    print("私は英単語帳アプリです。")
    #print("私は秋田若奈です\n")

if __name__ == '__main__':
    main()



#ーーーーーー英単語帳アプリーーーーーー
#ファイルの読み込み
with open("input\\article1.txt","r",encoding = "utf-8") as f:
    kari_text = f.read()
#正規表現をインポート
import re



#l_moji = [] #ファイルから英単語の抽出・小文字にする
l_moji = re.findall("\w[a-z]+",kari_text.lower())

mojicount = {}  #数を数えて辞書の作成（setを使用）
for content in set(l_moji):
    mojicount[content] = l_moji.count(content)

hight = list(sorted(mojicount.items(),key = lambda x:(-x[1],x[0]))[:10])    #（個数＞a-z)降順に並び替え、トップ１０をリストにする

mean = "日本語訳を入力してください" #意味の初期値を定義・最終的なリストを定義（単語、回数、意味を一塊に）
word = []
for h in hight:
    word.append([h[0],h[1],mean])

def hyouji():   #一覧の出力
    print(["英単語","回数","日本語訳"])
    for w in word:
        print(w)

print("\n-----出現頻度の高い英単語TOP10-----")  #出力文字を定義
print("一覧 or 更新 or 終了")
menu = input()

if menu == "更新":  #誘導コード
    print("日本語訳を記入してください")
    for m in word:
        print(m[0])
        ja = input()
        if ja == "":
            pass
        else:
            m[2] = ja
    hyouji()
elif menu == "一覧":
    hyouji()
else:
    print("終了します")


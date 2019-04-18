coding= "utf-8"
import re
import json

def main():
    menu()

# メニューを表示してそれぞれの処理を行う
def menu():
    menu_list = [
        "英単語帳作成　　: 1", 
        "日本語訳の更新　: 2",
        "英単語帳一覧　　: 3",
        "ソート方法選択　: 4",
        "終了　　　　　　: 0"
    ]
    for s in menu_list:
        print(s)
    print("メニューから行うことを数字で選んでください")
    try:
        select = int(input())
        if select == 1:
            print("英単語帳作成")
            create_wordbook()
        elif select == 2:
            print("日本語訳の更新")
            update_wordbook()
        elif select == 3:
            print("英単語帳一覧")
            print_word_count_mean()
        elif select == 4:
            print("ソート方法選択")
        elif select == 0:
            print("終了します")
        else:
            print("その数字は存在しません")
            menu()
    except ValueError:
        print("数字を入力してください")
        menu()
        
# 元の文から英単語帳を作成する
def create_wordbook():
    s_pass = "input\\article1.txt"
    r_pass   = "input\\remove.txt"
    word_dict = count_per_word(cut_sentence(s_pass, r_pass))
    word_list = add_japanese(sort_count(word_dict))
    output(list_to_json(word_list))
    print("\n英単語帳が作成されました\n")
    print_word_count_mean()

# 作成された英単語帳から単語の意味を更新する
def update_wordbook():
    try:
        with open('output\\output.json', encoding='utf-8') as f:
            data_dict = json.load(f)
            print_word_mean()
            print("\nどの英単語の日本語訳を更新しますか？")
            word = input()
            for key, val in data_dict.items():
                if word == val["name"]:
                    print(word + "の意味を入力してください")
                    data_dict[key]["means"] = input()
                    output(data_dict)
                    print_word_mean()
                    print("更新しました")
                    break
            else:
                print("入力された英単語は存在しません\n")
    except FileNotFoundError:
        print("はじめに英単語帳に作成を行ってください")

# 元の文を小文字に直し単語ごとのリストを作る。
# その後そのリストから除外対象の要素を除外し返す。
def cut_sentence(s_pass, r_pass):
    with open(s_pass, "r") as f:
        sentence = f.read()
        word_list = re.findall('(\w+)[\W+]', sentence.lower())
    return remove(word_list, r_pass)

# リストから数字のみの要素と除外リストの要素を除外する
def remove(word_list, r_pass):
    with open(r_pass, "r") as f:
        remove_list = f.read()
        i = 0
    while i < len(word_list):
        if re.search("[a-z]", word_list[i]) and not(word_list[i] in remove_list):
            i += 1
        else:
            word_list.pop(i)
    return word_list

# 英単語リストから重複を消し単語ごとの回数を数え辞書型で返す
def count_per_word(word_list):
    word_count_dict = {}
    for word in word_list:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict

# 英単語と回数を表示する(仮、空白の数を考える(表示の形成))
def print_word_count(word_list):
    print("{:10}".format("word") + "{:10}".format("count"))
    for word, cnt in word_list:
       print("{:10}".format(word) + "{:10}".format(str(cnt)))

# JSON形式のファイルを読み込み英単語と意味を表示する(仮、空白の数を考える(表示の形成))
def print_word_mean():
    try:
        with open('output\\output.json', encoding='utf-8') as f:
            print("{:10}".format("word") + "mean")
            data_dict = json.load(f)
            for data in data_dict.values():
                print("{:10}".format(data["name"]) + data["means"])
    except FileNotFoundError:
        print("はじめに英単語帳に作成を行ってください")

# JSON形式のファイルを読み込み英単語と回数と意味を表示する(仮、空白の数を考える)
def print_word_count_mean():
    try:
        with open('output\\output.json', encoding='utf-8') as f:
            print("{:10}".format("word") + "{:10}".format("count") + "mean")
            data_dict = json.load(f)
            for data in data_dict.values():
                print("{:10}".format(data["name"]) + "{:<10}".format(data["count"]) + data["means"])
    except FileNotFoundError:
        print("はじめに英単語帳に作成を行ってください")

# 英単語を出現回数でソートし上位10個だけをリストで返す
def sort_count(word_dict):
    word_list = []
    for k, v in sorted(word_dict.items(), key=lambda x: -x[1])[:10]:
        word_list.append([k, v])
    return word_list

# 英単語をアルファベット順でソートし上位10個だけをリストで返す
def sort_atoz(word_dict):
    word_list = []
    for k, v in sorted(word_dict.items(), key=lambda x: -x[0])[:10]:
        word_list.append([k, v])
    return word_list

# 英単語リストに和訳をつけたリストを返す
def add_japanese(word_list):
    print_word_count(word_list)
    new_word_list = []
    for word in word_list:
        new_word = word
        print(word[0] + "の意味を入力してください")
        while 1:
            mean = input()
            if mean:
                break
        new_word.append(mean)
        new_word_list.append(new_word)
    return new_word_list

# 受け取ったリストをJSONの形式に変える
def list_to_json(word_list):
    output_dict = {}
    for cnt, data in enumerate(word_list):
        set_data = {}
        set_data["name"]     = data[0]
        set_data["count"]    = data[1]
        set_data["means"] = data[2]
        output_dict["word" + str(cnt)] = set_data
    return output_dict

# JSON形式のディクショナリーをファイルに出力する
def output(word_dict):
    with open('output\\output.json', 'w', encoding="utf-8") as f:
        json.dump(word_dict, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()

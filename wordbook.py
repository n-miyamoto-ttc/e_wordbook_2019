# coding= utf-8
import re
import json


# 単語帳作成
def create(text_file, sort_flg):
    # テキストデータ読み込み
    with open(text_file, 'r', encoding='utf-8') as f:
        line = f.read()
        word_list = re.split("[^a-z]+", line.lower())

    # 単語JSON雛型
    notebook = {}
    # 出現回数測定用
    stack_dict = {}

    # 特定の単語を除去する
    word_list = remove(word_list)
    for word in word_list:
        stack_dict[word] = stack_dict.get(word, 0) + 1
    # 出現回数順にソート
    for k, v in sorted(stack_dict.items(), key=lambda x: -x[1]):
        mean = input('{}の意味を入力して下さい。\n>'.format(k))
        notebook[k] = [v, mean]
        if len(notebook) >= 10:
            break
    # 書き込み：sort_keys=Trueでa-z順に
    with open('output/result.json', 'w') as f:
        json.dump(notebook, f, indent=2, sort_keys=sort_flg, ensure_ascii=False)
    # 結果表示
    display('output/result.json')


# コンソール出力
def display(json_file):
    with open(json_file, 'r') as f:
        json_dict = json.load(f)

    max_key_blank = 0
    max_value_blank = 0
    for k, v in json_dict.items():
        if len(k) > max_key_blank:
            max_key_blank = len(k)
        if len(v[1]) * 2 > max_value_blank:
            max_value_blank = len(v[1]) * 2

    # ヘッダー
    print("*" * (max_key_blank + max_value_blank + 16))
    print("単語{0}   意味{1}   出現回数".format(" " * (max_key_blank - 4), " " * (max_value_blank - 4)))
    print("*" * (max_key_blank + max_value_blank + 16))
    # 中身
    for k, v in json_dict.items():
        print("{0}{1} | {2}{3} | {4}".format(k, (" " * (max_key_blank - len(k))), v[1],
                                             (" " * (max_value_blank - (len(v[1]) * 2))), v[0]))
    # フッター
    print("*" * (max_key_blank + max_value_blank + 16))


# アドバンス：単語帳の意味を更新
def update(json_file):
    with open(json_file, 'r') as f:
        json_dict = json.load(f)
    # 一覧表示
    display(json_file)
    select_word = input("\n意味を変更する単語を入力してください\n> ")
    print("入力された単語：{0}".format(select_word))
    if select_word in json_dict.keys():
        print("単語の意味：{0}".format(json_dict[select_word][1]))
        select_mean = input("変更後の意味を入力してください\n> ")
        print("入力された単語：{0}".format(select_word))
        print("入力された意味：{0}".format(select_mean))
        print("以上の内容で間違いありませんか？")
        res = input("[yes|no]\n> ")
        if res in ["yes", "Yes", "YES", "y", "Y"]:
            json_dict[select_word][1] = select_mean
            with open(json_file, 'w') as f:
                json.dump(json_dict, f, indent=2, ensure_ascii=False)
            display(json_file)
        elif res in ["no", "No", "NO", "n", "N"]:
            print("終了します")
        else:
            print("無効な入力です。最初からやり直してください")
    else:
        print("入力した単語が単語帳に存在しません。最初からやり直してください")


# アドバンス：特定の単語を除去する
def remove(word_list):
    with open('input/remove.txt', 'r', encoding='utf-8') as f:
        line = f.read()
        remove_list = re.split("[,. \\n]+", line)
    return filter(lambda x: (not x in remove_list), word_list)


def main():
    args1 = input("[create|update|display]\n> ")
    if args1 == "create":
        args2 = bool(input("ソート：0→出現回数順, 1→A-Z順\n> "))
        # 第二引数：ソート 0→出現回数順, 1→A-Z順
        create('input/article1.txt', int(args2))
    elif args1 == "update":
        update('output/result.json')
    elif args1 == "display":
        display('output/result.json')
    else:
        print("exit")


if __name__ == '__main__':
    main()
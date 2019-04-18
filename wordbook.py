# coding= utf-8
import re
import json

print("私は英単語帳アプリです。")
def main():
    print("作成|更新|表示|終了")
    senntaku = input()
    if senntaku == "作成":
        create()
    elif senntaku == "更新":
        update()
    elif senntaku == "表示":
        display()
    elif senntaku == "終了":
        return 0
    else:
        print("不正な入力です。もう一度入力してください")
        main()
        return 0
    print("操作を続けますか？(y or n)")
    y_or_n=input()
    if y_or_n == "y":
        main()
    else:
        return 0

def create():
    print("input内にあるファイル名を入力してください(拡張子不要、txtファイル確定)")
    string_input = input()
    try:
        fileread = open("input\\"+string_input+".txt",'r',encoding='utf-8')
    except FileNotFoundError:
        print(string_input+".txtというファイルは存在しません。もう一度ファイル名を入力してください")
        create()
        return 0
    readlower = fileread.read().lower()

    # 数字と記号の削除
    delete_number = re.sub('[0-9]'," ",readlower)
    delete_fread = re.sub('\W'," ",delete_number).split()

    if len(delete_fread) == 0:
        print("英単語がありません。もう一度ファイル名を入力してください")
        fileread.close()
        create()
    
    key_length = 0
    meaning_length = 0
    appearance = {}
    meaning = {}
    
    for key in delete_fread:
        if key in appearance:
            appearance[key] += 1
        else:
            appearance[key] = 1
            meaning[key] ="未入力"
        if key_length < len(key):
            key_length = len(key)
    
    # print("単語           |意味           |出現回数")
    # print("----------------------------------------")
    # for key in appearance:
    #     print(key.ljust(key_length," ")+"|"+meaning[key].ljust(15," ")+"|"+str(appearance[key]))
    
    
    if len(appearance) >= 10:
        length = 10
    else:
        length = len(appearance)
    
    list_c={}
    list_d={}
    
    print("ソートを選んでください")
    print("a-z順はa,出現回数順はn")

    sort = input()
    if sort == "a":
        for st in meaning:
            min_appearance = min(appearance)
            print(min_appearance.ljust(key_length," ")+"|"+meaning[min_appearance].ljust(15," ")+"|"+str(appearance[min_appearance]))
            list_d[min_appearance.ljust(key_length," ")]=meaning[min_appearance]
            list_c[min_appearance.ljust(key_length," ")]=appearance[min_appearance]
            del appearance[min_appearance]
    
    else:
        for co in range(length):
            max_appearance = 0
            for st in appearance:
                if max_appearance < appearance[st]:
                    max_appearance = appearance[st]
                    max_st = st
            print(max_st+"の意味を入力してください")
            meaning[max_st] = input()
            list_d[max_st.ljust(key_length," ")] = meaning[max_st]
            list_c[max_st.ljust(key_length," ")] = appearance[max_st]
            if meaning_length < len(meaning[max_st]):
                meaning_length = len(meaning[max_st])
            del appearance[max_st]
        print("-----------------------------------------")
        print(("単語").ljust(key_length-2," ")+"|"+("意味").ljust(meaning_length+6," ")+"|出現回数")
        print("-----------------------------------------")
        for str_st in list_d:
            mean_len = (len(list_d[str_st].encode())-len(list_d[str_st]))/2
            print(str_st+"|"+list_d[str_st].ljust(meaning_length+8-int(mean_len)," ")+"|"+str(list_c[str_st]))
        print("-----------------------------------------")
    
    print("ファイルを作成しますか？(y or n)")
    y_or_n = input()
    if y_or_n == "y":
        print("作成するファイル名を入力してください(拡張子不要、jsonファイル確定)")
        string_output = input()
        jsonfile = open(string_output+".json",'w',encoding='utf-8')
        for l in list_d:
            mean_len = (len(list_d[l].encode())-len(list_d[l]))/2
            list_d[l] = "意味:"+str(list_d[l]).ljust(meaning_length+8-int(mean_len)," ")+" 出現回数:"+str(list_c[l])
        json.dump(list_d,jsonfile,ensure_ascii=False, indent=2)
        jsonfile.close()
    fileread.close()


def update():
    print("ファイル名を入力してください(拡張子不要、jsonファイル確定)")
    string_input = input()
    try:
        jsonfile = open(string_input+".json","r",encoding='utf-8')
    except FileNotFoundError:
        print(string_input+".jsonというファイルは存在しません。もう一度ファイル名を入力してください")
        update()
        return 0
    up_d = json.load(jsonfile)
    for line in up_d:
        int_up_d_key = len(line)
        int_up_d_value = len(up_d[line])
        print(line+up_d[line])
    print("意味を登録したい英単語を入力してください")
    while True:
        string_key = input()
        string_key = string_key.ljust(int_up_d_key," ")
        if string_key in up_d:
            print(string_key.strip(" ")+"の意味を入力してください")
            string_meaning = input()
            str_mean = up_d[string_key].split()
            int_up_d_value = int_up_d_value - len(str_mean[1])
            jsonfile.close()
            jsonfile = open(string_input+".json","w",encoding='utf-8')
            up_d[string_key] = ("意味:"+string_meaning).ljust(int_up_d_value," ")+str_mean[1]
            for line in up_d:
                print(line+up_d[line])
            json.dump(up_d,jsonfile,ensure_ascii=False, indent=2)
            jsonfile.close()
            return 0
        else:
            print(string_key+"は"+string_input+".jsonに含まれていません。もう一度単語名を入力してください")


def display():
    print("ファイル名を入力してください(拡張子不要、jsonファイル確定)")
    string_input = input()
    try:
        jsonfile = open(string_input+".json",'r',encoding='utf-8')
    except FileNotFoundError:
        print(string_input+".jsonというファイルは存在しません。もう一度ファイル名を入力してください")
        display()
        return 0
    for line in jsonfile:
        print(line,end="")
    print()
    jsonfile.close()

if __name__ == '__main__':
    main()

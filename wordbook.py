# coding= utf-8
import re

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

def create():
    print("input内にある入力ファイル名を入力してください(.txtを除く)")
    string_input = input()
    f = open("input\\"+string_input+".txt",'r',encoding='utf-8')
    fread = f.read()
    delete_p = fread.replace("."," ")
    delete_ps = delete_p.replace(";"," ")
    delete_psc = delete_ps.replace(":"," ")
    delete_psck = delete_psc.replace(","," ").lower().split()
    c = {}
    d = {}
    for s in delete_psck:
        if s in c:
            c[s] += 1
        else:
            c[s] = 1
            d[s] ="未入力"
    tmpl = "{0:15}"
    tmp = "{0:>5}"
    print(tmpl.format("単語帳")+tmpl.format("意味")+tmp.format("出現回数"))
    
    
    
    for s in c:
        print(tmpl.format(s)+tmpl.format(d[s])+tmp.format(c[s]))
    
    print("ファイルを作成しますか？(y or n)")
    s=input()
    if s == "y":
        print("ファイル名を選択してください")
        string_output = input()
        fwrite = open(string_output,'w',encoding='utf-8')
        fwrite.write("rty")
    f.close()

def update():
    print("output内にある入力ファイル名を入力してください(.txtを除く)")
    string = input()
    f = open(string+".txt",'w',encoding='utf-8')
    

def display():
    print("output内にある入力ファイル名を入力してください(.txtを除く)")
    string = input()
    f = open(string+".txt",'r',encoding='utf-8')

if __name__ == '__main__':
    main()

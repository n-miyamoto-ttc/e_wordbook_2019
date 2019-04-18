# coding= utf-8
import re
from collections import Counter
import json

def main():
    print("私は英単語帳アプリです。")
    try:
        with open("input\\article1.txt","r",encoding="utf-8") as pfr,open("input\\remove.txt","r",encoding="utf-8") as pfr_h:
            dictw = {}
            fr = pfr.read()
            fr_h = pfr_h.read()
            words = re.split("\s|\,|\.|\(|\)|\\-|[0-9]|\;|:|\n", fr.lower())
            words_h = re.split("\n",fr_h)
            #print(words)
            #print(words_h)
            counter = Counter(words)
            #print(counter)
            print("除去リストに登録された単語を除きますか。 1 --> はい 2 --> いいえ : ",end="")
            w_bye = input()
            if w_bye == "1":
                for word, count in counter.most_common():
                    if len(word) > 0 and word not in words_h:
                        dictw[word] = ["意味サンプル",str(count)]
            if w_bye == "2":
                for word, count in counter.most_common():
                    if len(word) > 0:
                        dictw[word] = ["意味サンプル",str(count)]

        # JSONの書き込み方法
        # with open("input\\words.json","w",encoding="utf-8") as pfw:
        #         json_str = json.dumps(dictw, ensure_ascii=False)
        #         pfw.write(json_str+"\n")
                #pfw.close()
    
        # JSONの読み込み方法
        # with open("input\\words.json","r",encoding="utf-8") as pfrr:

        #     s = pfrr.read()
        #     str_dic = json.loads(s)

            #wor,imi,fru = "単語","意味","出現回数"
        print("**********************************************")
            #print('{0:<15}'.format(wor),'{0:<10}'.format(imi),'{0:<10}'.format(fru))
        print("単語             意味               出現回数      ")
        print("**********************************************")

        i = 0
        for k,v in dictw.items():
            if i < 10:
                #print(k,"         ｜",v[0],"  ｜",v[1])、
                print('{0:<15}'.format(k),"|",'{0:<10}'.format(v[0]),"|",'{0:<10}'.format(v[1]))
                i += 1
            else:
                break

        print("**********************************************")

        #pfrr.close()

        print("上記10個英単語に対応する日本語訳を追加してください")
        j = 0
        dictwt = {}
        for k,v in dictw.items():
            if j < 10:
                print(k," : ",end="")
                s = input()            
                dictwt[k] = [s,v[1]]
                j += 1
            else:
                dictwt[k] = v
        #print(dictwt)
    
        print("**********************************************")
        #print('{0:<15}'.format(wor),'{0:<10}'.format(imi),'{0:<10}'.format(fru))
        print("単語             意味         出現回数      ")
        print("**********************************************")

        i = 0
        for k,v in dictwt.items():
            if i < 10:
                print('{0:<15}'.format(k),"|",'{0:<10}'.format(v[0]),"|",'{0:<10}'.format(v[1]))
                i += 1
            else:
                break

        print("**********************************************")

        #with
        with open("input\\words_j.json","w",encoding="utf-8") as pfwj:
            json_words = json.dumps(dictwt, ensure_ascii=False)
            pfwj.write(json_words+"\n")
            #pfwj.close()

        #ソート順
        print("英単語のソート順の選んでください 1 --> 出現回数順、2 --> アルファベット順 : ",end="")
        check_s = input()
        if check_s == "1":
            print("**********************************************")
            print("単語             意味         出現回数      ")
            print("**********************************************")

            i = 0
            for k,v in dictwt.items():
                if i < 10:
                    print('{0:<15}'.format(k),"|",'{0:<10}'.format(v[0]),"|",'{0:<10}'.format(v[1]))
                    i += 1
                else:
                    break

            print("**********************************************")
        elif check_s == "2":
            so_w = sorted(dictwt.items())
            #print(so_w)
            #print(so_w[0][0],so_w[0][1][0],so_w[0][1][1])
            print("**********************************************")
            print("単語             意味             出現回数      ")
            print("**********************************************")

            i = 0
            for v_a in so_w:
                if i < 10:
                    print('{0:<15}'.format(v_a[0]),"|",'{0:<10}'.format(v_a[1][0]),"|",'{0:<10}'.format(v_a[1][1]))
                    i += 1
                else:
                    break

            print("**********************************************")
        else:
            print("入力エラー")


    except FileNotFoundError:
        print("ファイルは存在していません")

    # JSONの読み込み方法
    print("単語の意味を更新、追加しますか。 1 --> はい 2 --> いいえ : ",end="")
    update_ck = input()
    if update_ck == "1":
        with open("input\\words_j.json","r",encoding="utf-8") as pfrr:
            s = pfrr.read()
            str_dic = json.loads(s)
            print("英単語を入力してください --> ")
            str_in = input()
            if str_in in str_dic.keys():
                print(str_in,str_dic[str_in],"意味を追加・変更をしてください --> ",end="")
                w_up = input()
                str_dic[str_in] = [w_up,str_dic[str_in][1]]
                print("変更完了")
                print(str_in,str_dic[str_in])
            else:
                print("単語存在している")
    else:
        print("Thank you")
            


if __name__ == '__main__':
    main()
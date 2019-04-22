import re
from collections import Counter
import json

# 1·open the file and read it from list to list and create another file for putting result
def main():
    print('今から働きますーーyes or no')
    a = input()
    if a == 'yes':
        f_katai = open("input\\article1.txt","r",encoding="utf-8") 
        f_result = open("input\\result.txt","w",encoding="utf-8")
        data = f_katai.read()
        dic_list = {}
    # print(data) 

# 2·take out the every words in text, not including space and comma(method:regular expression or )
##方法1:  for word in data.split():
##方法1:  pre_words.append(word)

###方法2:
        per_words = re.split("\\s|\,|\.|\(|\)|\-|[0-9]|\;|:",data.lower())
    # print(per_words)

# 3·count how many times that every words were written in the text and put it in order
##方法1create a dictionary which include a word and how many times the word was written in th text
#使用回数，辞書形式でソートできないので、リストに変更して、順番を決める(http://input-and-output.hatenablog.com/entry/2017/08/28/151149)
##方法1:word_counter = {}  
##方法1:for w in pre_words:
##方法1:word_counter.setdefault(w,0) 
##方法1:word_counter[w] = word_counter[w]+1
##方法1:word_counter_listed = [(v,k) for k,v in word_counter_items()]
##方法1:word_counter_listed.sort() #决定顺序从小到大
##方法1:word_counter_listed.reverse() #顺序从大到小表示
    
###方法2:
        counter = Counter(per_words)
        # print(counter)
        for word, count in counter.most_common(): # most_common():https://blog.csdn.net/zyx_ly/article/details/88202672
            if len(word) > 0:
                dic_list[word] = ['意味サンプル',str(count)]#create a space for meaning in 'count'
    #print(dic_list)
        print("*******************************************")
        print("単語             意味            出現回数")
        i=0
        for word,count in dic_list.items():
            if i <10:
                print('{0:15}|{1:10}|{2:10}'.format(word,count[0],count[1]))
                i+= 1
            else:
                break

        print("*******************************************")      
    

        dic_new={}
        i=0
        for word,count in dic_list.items():
            if i<10:
                a = input()
                dic_new[word] = [a,count[1]]
                i+=1
            else:
                dic_new[word] = [count[0],count[1]]
    
        print("*******************************************")
        print("単語             意味            出現回数")
        i=0
        for word,count in dic_new.items():
            if i <10:
                print('{0:15}|{1:15}|{2:10}'.format(word,count[0],count[1]))
                i+=1
            else:
                break
        print("*******************************************")
        json_fw = open("input\\result.json","w",encoding="utf-8") 
        json.dump(dic_new,json_fw, ensure_ascii=False)
        # print('順番を変わりますか---1.yes  2.no')
        # b = input()
        # if b=='1':
        #     counter2 = 
  
    
    elif a =='no':
        print('サヨナラ')
    else:
        print('入力エラー')

if __name__ == "__main__":
    main()



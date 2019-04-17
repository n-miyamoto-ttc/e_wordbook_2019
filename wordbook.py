# import re
# 导入文件，之阅读，不改写，逐列阅读



# 把英文单词提取出来，用今天交的方法
# def main:
#     f = open("article1.txt","r",encoding="utf-8")
#     s = f.read()
#     print('電子辞書です。')

#     s = re.split(r'\s|\,|\.|\(|\--[0,9])', target_text.lower())
# # 计算哪些文字在文章中最多，并且计算个数
#     counter = Counter(words)
#     for word, count in counter.most_common():
#     if len(word) > 0:
#         print("%s,%d" % (word, count))
f = open("input\\article1.txt","r",encoding="utf-8") 
article1_txt = f.read()
print(article1_txt) 



# 把结果打印出来，但是必须全部是小写，还要加上日文的解释



# 把结果打印成一栏的形式，显示的形式必须是JSON
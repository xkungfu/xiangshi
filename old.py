import os
import re
import math
import jieba 
import time
import xiangshi as xs

start_time = time.time()


CalFile = input("哪个计算文件? Which file do you want to calculate?\n")
UseLog = input("是否使用 log()? Do you want to use log? Y/N\n").upper()

StopWords = ["、","“", "”","#","$","：","‘","’", "(",")","*","+", "\n"]
# 对句子进行中文分词
def SegDepart(sentence):
    # 对文档中的每一行进行中文分词
    SentenceDepart = jieba.cut(sentence.strip(), cut_all=False)
    # 输出结果为output
    output = []
    # 去停用词
    for word in SentenceDepart:
        if word not in StopWords:
            if word != '\t':
                output.append(word)
    return output

def file2list(file):
    result = []
    with open(file, encoding='gb18030') as f:
        corpus = f.read()
        LineSplit = re.split(r'[。！；？，]', corpus.strip()) #按符号分句
        for line in LineSplit:
            temp = SegDepart(line)
            result.extend(temp)
    return result

#计算tf值 
def GetTF(corpus):
    tf = {}
    for x in corpus:
        tf[x] = corpus.count(x)
    
    wordsSum = sum(tf.values())
    for key, value in tf.items(): 
        tf[key] = value / wordsSum
    return tf

#计算idf值
def GetIDF(TFDict):
    freq = {}
    for x in TFDict:
        freq[x] = 0
        
    idf = {}
    FileLists = []
    for filename in os.listdir("data/"):
        FileLists.append(file2list("data/" + filename))

    total = len(FileLists)

    print(FileLists)
    #对于每个文档
    for word in TFDict:
        #对于文档中的每个词，统计其在文档中的出现频率
        for x in FileLists:
            if word in x:
                freq[word] += 1

    #将每个词的出现次数转换为idf值    
    for word in freq:
        #idf的公式
        TempIDF = total / (freq[word] + 1)
        if UseLog == "Y":
            idf[word] = TFDict[word] * math.log(TempIDF)
        else:
            idf[word] = TFDict[word] * TempIDF
        print(word, ":", idf[word])
    return idf
 
def GetTFIDF(file):
    '''doc_id是语料库中文档的id，file是txt的路径'''
    corpus = file2list(file)
    tf = GetTF(corpus)
    idf = GetIDF(tf)
    result = {}

    for key, value in tf.items():
        result[key] = idf[key]

    result = dict(sorted(result.items(), \
        key=lambda kv: kv[1], reverse=True))
    
    open('result.txt', 'w').close()
    f = open("result.txt", "a")
    
    for key, value in result.items():
        f.write(str(key) + ": " + str(value) + "\n")
    f.close()
    print("\nResult saved in 'result.txt'")
        
GetTFIDF(CalFile)
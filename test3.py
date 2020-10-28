from xiangshi import noweight as xsn
from xiangshi import tfweight as xst

print(xsn.cossim("OriginalData/test1.txt", \
            "OriginalData/test2.txt"))

print(xst.cossim("OriginalData/test1.txt", \
            "OriginalData/test2.txt"))

FileDir = "data/"
FileLists = []
idf = {}
for inputname in os.listdir(FileDir):
    FileLists.append(xiangshi.input2list(FileDir + inputname))
result = []
for x in FileLists:
    result += x
result = list(set(result))
print(type(result))
print(xiangshi.GetIDF(result))
tf = {}
for x in range(1, 30):
    xiangshi.GetTF("data/test" + str(x) + ".txt")
print("--- %s seconds ---" % (time.time() - StartTime))"""
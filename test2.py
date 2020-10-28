from main2 import calculator
import time
import os

xs = calculator()

#清除之前的记录
open("result.txt", "w")

for i in range(1, 40):
    for j in range(i + 1, 40):
        #写入result.txt
        f = open("result.txt", "a")

        f.write(str(i) + " " + str(j) \
            + " " + str(xs.cossim("data2/text" + str(i) + ".txt", \
            "data2/text" + str(j) + ".txt")) + "\n")
        f.close()
        print(i, j)
        


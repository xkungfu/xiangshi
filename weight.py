import os
import logging
import time
import main2

cal = main2.calculator

class calculator(cal):
    def __init__(self):
        super(calculator, self).__init__()
        self.logger.info("Starting up Xiangshi Weight")
        self.weight = None

    #计算TF值 
    def GetTF(self, corpus):
        tf = {}
        for x in corpus:
            tf[x] = corpus.count(x)
        
        wordsSum = sum(tf.values())
        for key, value in tf.items(): 
            tf[key] = value / wordsSum
        return tf

    def Get1(self, corpus):
        tf = {}
        for x in corpus:
            tf[x] = 1
        return tf

    def GetTFIDF(self, input):
        if isinstance(input, list) == True:
            tf = self.GetTF(input[self.InputTarget])
            one = self.Get1(input[self.InputTarget])
        elif isinstance(input, str) == True:
            if os.path.isfile(input) != True:
                raise Exception("Wrong File")
            files = self.dir2list(input)
            tf = self.GetTF(files[input])
            one = self.Get1(files[input])
        
        if self.weight == "TF":
            return tf
        elif self.weight == None:
            return one
        else:
            raise Exception("self.weight can onle be set as \"TF\" or None")

xs = calculator()
print(xs.cossim("data/test1.txt", "data/test2.txt"))
xs.weight = "TF"
print(xs.cossim("data/test1.txt", "data/test2.txt"))
from main2 import calculator
import os
import time
import math
import threading
import queue
record = []
lock = threading.Lock()
    
cal = calculator()

def EuclideanDistance(a, b):
    LenA = len(a)
    LenB = len(b)
    if LenA < LenB:
        a += [0] * (LenB - LenA)
    elif LenB < LenA:
        b += [0] * (LenA - LenB)
    
    ans = 0
    for i in range(len(a)):
        ans += pow(a[i] - b[i], 2)
        
    return ans

def kcluster(k, dir):
    print("Calculating")  
    q = queue.Queue()
    s = time.time()
    TFIDFFiles = {}
    for x in os.listdir(dir):
        thread = threading.Thread(target=lambda q, arg1: q.put(cal.GetTFIDF(arg1)), args=(q, dir + x))
        thread.start()
        thread.join()
        q.get()
    
    print(time.time() - s)
    return TFIDFFiles

def kclusterslow(k, dir):
    s = time.time()
    TFIDFFiles = {}
    for x in os.listdir(dir):
        TFIDFFiles[x] = cal.GetTFIDF(dir + x)

    print(time.time() - s)
    return TFIDFFiles


kcluster(1, "data/")


"""204.73085045814514"""
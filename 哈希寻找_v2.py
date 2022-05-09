import hashlib
import random as r
import time
import math
import os


def length_asker():
    digits = "Doge forever"
    print("几位数？(通常是8-12位数)")
    while type(digits) != int:
        digits = input("输入位数\n")
        try:
            digits = int(digits)
        except:
            print("你刚才输入的不是整数")
    return digits

def hash_asker():
    the_hash = "Doge forever"
    while len(the_hash) != 64:
        the_hash = input("把你的64位长的哈希粘贴到下面并按回车\n")
    return the_hash

def pin_generator():
    try:
        f = open("hash.txt", "r")
        print("\n当前存在一个哈希，并且你还没找到它的pin")
        print("你得首先找到当前hash的pin才行!!")
        digit_finder()
    except:
        digits = length_asker()
        x0 = str(r.randint(0,10**digits))
        print("你的pin是"+x0[-8:])
        len_of_x0 = len(x0)
        print("你刚才输入了"+str(len_of_x0)+"位数")
        x1 = "0"*(digits-len_of_x0) +str(x0)
        x2 = x1.encode()
        x3=hashlib.sha256(x2).hexdigest()
        f = open("hash.txt", "w")
        f.write(x3)
        f.close()
        print("哈希是"+x3)

def digit_finder():
    digits = length_asker()
    f = open("hash.txt", "r")
    the_hash = f.read()
    f.close()
    try:
        f = open("progress.txt", "r")
        progress = int(f.read())
        f.close()
        print("发现了之前的进度，继续寻找")
    except:
        progress = 0
        print("没发现之前的进度，从零开始")
    for i in range(progress,10**digits):
        len_of_i = len(str(i))
        str1 = "0"*(digits - len_of_i) +str(i)
        str2 = str1.encode()
        str3 = hashlib.sha256(str2).hexdigest()
        if str3 == the_hash:
            print("We found it!, it is "+ str1)
            try:
                os.remove("progress.txt")
                f = open("result.txt", "a")
                hash_and_pin = "\n"+the_hash+"\n"+str1+"\n"
                f.write(hash_and_pin)
                f.close()
                os.remove("hash.txt")
            except:
                print("progress.txt does not exist")
            break
        else:
            if i % 4000000 ==0:
                print("\n"+str1+" Tested")
                print("最悲观地已经找了: "+"{0:.2%}".format(i/10**digits))
                print("当前已经找了几位数:"+ str(math.log(i+1,10)) )
                if i % 20000000 ==0:
                    print("保存进度")
                    f = open("progress.txt", "w")
                    f.write(str(i))
                    f.close()
            else:
                pass
                       

def test():
    the_hash = "ce3a598687c8d2e5aa6bedad20e059b4a78cca0adad7e563b07998d5cd226b8c"
    digits = 10
    print("测试将用差不多10秒钟，等一下")
    start_time = time.time()
    for i in range(10**digits):
        len_of_i = len(str(i))
        str1 = "0"*(digits - len_of_i) +str(i)
        str2 = str1.encode()
        str3 = hashlib.sha256(str2).hexdigest()
        time_spent = time.time() - start_time
        if str3 == the_hash:
            print("找到了，它是"+ str1)
            break
        elif time_spent>10:
            hash_per_day = i/(time_spent/86400)
            for ii in range(7,14):
                print("最多会花 "+ str(round((10**(ii+1))/hash_per_day,2)) +" 天来找 "+str(ii+1)+" 位数在这台电脑上")
            break   
        else:
            if i % 1000000 ==0:
                print("\n"+str1+" Tested")
                print("最悲观地已经找了: "+"{0:.2%}".format(i/10**digits))
                print("当前已经找了几位数:"+ str(math.log(i+1,10)) )
            else:
                pass

def overall():
    header = "\n1.pin码生成 2.pin码寻找 3.测试速度 4.退出"
    options = ["1","2","3","4"]
    x = "doge"
    while x not in options:
        print(header)
        x = input("选择你要做的事，输入1，2，3或4然后按回车\n")
    if x == "1":
        pin_generator()
        overall()
    elif x == "2":
        digit_finder()
        overall()
    elif x == "3":
        test()
        overall()
    else:
        exit()

if __name__ == "__main__":
    print("这个py文件可以帮你:")
    print("1.的冷钱包生成随机pin码")
    print("2.把pin码转换成对应的哈希")
    print("3.寻找哈希的对应pin码")
    overall()
else:
    print(__name__ + " has been imported")
        
    
    


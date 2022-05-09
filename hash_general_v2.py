import hashlib
import random as r
import time
import math
import os


def length_asker():
    digits = "Doge forever"
    print("You need to type in your digits(recommended 8-12)")
    while type(digits) != int:
        digits = input("Type your digits\n")
        try:
            digits = int(digits)
        except:
            print("What you just typed is not integer")
    return digits

def hash_asker():
    the_hash = "Doge forever"
    while len(the_hash) != 64:
        the_hash = input("You need to paste in your 64 characters hash\n")
    return the_hash

def pin_generator():
    try:
        f = open("hash.txt", "r")
        print("\nExisting hash found, and you have not found its pin")
        print("You need to find existing pin first!!")
        digit_finder()
    except:
        digits = length_asker()
        x0 = str(r.randint(0,10**digits))
        print("Your pin is "+x0[-8:])
        len_of_x0 = len(x0)
        print("The digit is "+str(len_of_x0))
        x1 = "0"*(digits-len_of_x0) +str(x0)
        x2 = x1.encode()
        x3=hashlib.sha256(x2).hexdigest()
        f = open("hash.txt", "w")
        f.write(x3)
        f.close()
        print("The hash is "+x3)

def digit_finder():
    digits = length_asker()
    f = open("hash.txt", "r")
    the_hash = f.read()
    f.close()
    try:
        f = open("progress.txt", "r")
        progress = int(f.read())
        f.close()
        print("Previous progress found, resuming")
    except:
        progress = 0
        print("No previous pregress, starting from 0")
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
                print("Worst scenario: "+"{0:.2%}".format(i/10**digits))
                print("Current digits explored:"+ str(math.log(i+1,10)) )
                if i % 20000000 ==0:
                    print("Progress saved")
                    f = open("progress.txt", "w")
                    f.write(str(i))
                    f.close()
            else:
                pass

def test():
    the_hash = "ce3a598687c8d2e5aa6bedad20e059b4a78cca0adad7e563b07998d5cd226b8c"
    digits = 10
    print("It'll take about 10 seconds to finish the test")
    start_time = time.time()
    for i in range(10**digits):
        len_of_i = len(str(i))
        str1 = "0"*(digits - len_of_i) +str(i)
        str2 = str1.encode()
        str3 = hashlib.sha256(str2).hexdigest()
        time_spent = time.time() - start_time
        if str3 == the_hash:
            print("We found it!, it is "+ str1)
            break
        elif time_spent>10:
            hash_per_day = i/(time_spent/86400)
            for ii in range(7,13):
                print("it will take "+ str(round((10**(ii+1))/hash_per_day,2)) +" max days to find "+str(ii+1)+" digits number on this PC")
            break   
        else:
            if i % 1000000 ==0:
                print("\n"+str1+" Tested")
                print("Worst scenario: "+"{0:.2%}".format(i/10**digits))
                print("Current digits explored:"+ str(math.log(i+1,10)) )
            else:
                pass

def overall():
    header = "\n1.pin_generator 2.digit_finder 3.test 4.exit"
    options = ["1","2","3","4"]
    x = "doge"
    while x not in options:
        print(header)
        x = input("Choose what you want to do\n")
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
    print("This py file will help you:")
    print("1.generate random pin for your cold wallet")
    print("2.convert the pin into hash")
    print("3.find original input/pin of the hash")
    print("In a hope that it can decrease your trading frequency")
    print("by finding original input/pin of your hash that you keep somewhere")
    print("without losing total access to your cold wallet.\n")
    print("You can type your digit to determine the length of your pin.")
    print("However, the maximum digit of your pin that can be generated is 8.")
    print("That is to say, if you type 10, the excessive 2 digit")
    print("will be used as additional input to make the finding harder")
    overall()
else:
    print(__name__ + " has been imported")
        
    
    


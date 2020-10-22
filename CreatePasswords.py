import string
import random


def GeneratePassword (passLength):
    s = input("Random password ?  y / n : ")
    ran = s[0].lower()
    if ran.lower() == 'y':
        password = string.ascii_letters + string.digits + "!@#$%^&*()_+=-./?><|\}{[]"
        passwordList = []
        for passChar in range(passLength):
            passRandom = random.choice(password)
            passwordList.append(passRandom)

    elif ran.lower() == 'n':
        k1 = int(input("How much Small letter   : "))
        k2 = int(input("How much Capital letter : "))
        k3 = int(input("How much Digits ?       : "))
        k4 = int(input("Special symbols ?       : "))
        
        let1 = string.ascii_letters.lower()
        let2 = string.ascii_letters.upper()
        let3 = string.digits
        let4 = "!@#$%^&*()_+=-./?><|\}{[]"
        password = string.ascii_letters + string.digits + "!@#$%^&*()_+=-./?><|\}{[]"
        
        passwordList = []
        totallen = k1 + k2 + k3 + k4
        if totallen > passLength:
            print("Combined size will go out of your size limit ! ")
            
        remlen = passLength - totallen
        if remlen < 0:
            remlen = 0
        
        for ka1 in range(k1):
            passRandom = random.choice(let1)
            passwordList.append(passRandom)
            
        for ka2 in range(k2):
            passRandom = random.choice(let2)
            passwordList.append(passRandom)

        for ka3 in range(k3):
            passRandom = random.choice(let3)
            passwordList.append(passRandom)

        for ka4 in range(k4):
            passRandom = random.choice(let4)
            passwordList.append(passRandom)
            
        for ka5 in range(remlen):
            passRandom = random.choice(password)
            passwordList.append(passRandom)

        random.shuffle(passwordList)
            
    finalpsw = "".join(passwordList)
    return finalpsw

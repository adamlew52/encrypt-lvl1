#start prep work
def positionFinder(char):
    alphabet = 'abcdefghijklmnopqrstuvwxyz123456789'
    characterCompare = alphabet.find(str(char)) #this is the computer view
    return characterCompare

def evenAlphabet(characterCompare):
    if ((characterCompare + 1) % 2) == 0:
        return True
    else:
        return False
#end prep work

def Encrypt1(password):
    passwordList = list(password) 
    encrypt1 = ''
    for i in range(len(passwordList)):
        #print(passwordList[i]) # '\n')
        even = evenAlphabet(positionFinder(passwordList[i]))

def Encrypt2(password): #reverse the string
    passwordList = list(password)
    encrypt2 = ''
    for i in range(len(password), 0 , -1):
        encrypt2 += passwordList[i-1]
    return encrypt2

def Encrypt3(password):
    firstHalf = ''
    secondHalf = ''
    encrypt3 = ''
    passwordLength = len(password)

    for i in range(0, passwordLength):
        if i <= len(password)//2-1:
            firstHalf = firstHalf + password[i]
        else:
            secondHalf = secondHalf + password[i]
    
    encrypt3 += secondHalf
    encrypt3 += firstHalf

    return encrypt3


def main():
    #password = (e.get())
    #label = Label(root, text = password)
    password = "passwordz"
    password2 = "watchlover"
    password3 = "ihavebadpasswords69"
    password4 = "password69420"
    #print(Encrypt1(password4))
    #print(Encrypt2(password))
    print(Encrypt3(password3))

#main()
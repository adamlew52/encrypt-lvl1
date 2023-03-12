import Encrypt as E

def Decrypt1(password):
    print(f'still working on this one')
    
def Decrypt2(password): #reverse it back
    passwordList = list(password)
    decrypt2 = ''
    for i in range(len(password), 0 , -1):
        #print(decrypt2)
        decrypt2 += passwordList[i-1]
    return decrypt2

def Decrypt3(password):
    firstHalf = ''
    secondHalf = ''
    decrypt3 = ''
    passwordLength = len(password)

    for i in range(0, passwordLength):
        if i <= len(password)//2-1:
            firstHalf = firstHalf + password[i]
        else:
            secondHalf = secondHalf + password[i]
    
    decrypt3 += secondHalf
    decrypt3 += firstHalf

    return decrypt3


def main():
    password = E.Encrypt3("passwordz")
    #print(Decrypt1(password))
    #print(Decrypt2(password))
    print(Decrypt3(password))

main()
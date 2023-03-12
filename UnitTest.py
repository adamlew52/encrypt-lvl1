import Encrypt as E
import Decrypt as D

def TestPasswords():
    passwordList = []
    
    password = "passwordz"
    password2 = "watchlover"
    password3 = "ihavebadpasswords69"
    password4 = "password69420"

    #passwordList.append(password)
    #passwordList.append(password2)
    passwordList.append(password3)
    #passwordList.append(password4)
    return passwordList

def TestProcess1(passwordsList):
    for password in passwordsList:
        print(f'testing password {password}: ')
        E.Encrypt1(password)

def TestProcess2(passwordsList):
    for password in passwordsList:
        print(f'testing password: {password} ')
        ep = E.Encrypt2(password)
        print(f'encrypted password is {ep}')
        dp = D.Decrypt2(ep)
        print(f'decrypted password is {dp}')
        TestGrading(password, dp)
        print(f"--------------------------Done with test of {password}---------------------------")

def TestProcess3(passwordsList):
    for password in passwordsList:
        print(f'testing password {password}: ')
        E.Encrypt3(password)
        
def TestGrading(password, dp):
    if password == dp:
        print("\t\tsuccess!!")
    else:
        print(f"failure in the decryption process: \n requested outcome: \n actual outcome:{dp}")    


def main():
    #print(TestProcess1(TestPasswords()))
    #print(TestProcess2(TestPasswords()))
    print(TestProcess3(TestPasswords()))

main()
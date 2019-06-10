import string, pyperclip
from random import randint

class Main():
    def __init__(self):
        #z is abc[25]
        abc = list(string.ascii_lowercase)
        ABC = list(string.ascii_uppercase)
        O12 = []

        for i in range(26):
            O12.append(str(i))

        kar = [abc, ABC, O12]

        pwd = ""
        pwdlen = randint(8,12)

        for i in range(pwdlen):
            r0 = randint(0,2)
            r1 = randint(0,25)
            pwd += kar[r0][r1]

        print(pwd)
        pyperclip.copy(pwd)

if __name__ == "__main__":
    Main()
    input("\nPassword copied to clipboard - Press ENTER to exit")

import os
characters = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z','1','2','3','4','5','6','7','8','9','0']
encryption = ['n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z','a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','6','9','4','2','0','1','3','5','7','8']
punctuation = ['.',',','?','!',':',';',"'",'"','-','+','/','%','*']
def encrypt():
    output = []
    for x in plain:
        if x == ' ':
            converted = ' '
            output.append(converted)
        elif x in characters:
            converted = characters.index(x)
            output.append(encryption[converted])
        elif x in punctuation:
            converted = x
            output.append(converted)
    final = ''.join(output)
    print(final)
    return final
choice = input(" 1. Convert message\n 2. Exit program\nSelect an option:-- ")
if choice == '1':
    plain = input("Enter text to convert by ROT13: ")
    encrypt()
    os.system('pause')
else:
    exit

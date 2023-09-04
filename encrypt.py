import os
characters = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z','1','2','3','4','5','6','7','8','9','0']
encryption = ['n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z','a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','6','9','4','2','0','1','3','5','7','8']
punctuation = ['.',',','?','!',':',';',"'",'"','-','+','/','%','*']
def encrypt(plain):
    output = []
    for x in plain:
        if x == ' ':
            converted = ' '
            output.append(converted)
        elif x in punctuation:
            converted = x
            output.append(converted)
        else:
            converted = characters.index(x)
            output.append(encryption[converted])
    final = ''.join(output)
    print("Converted message: ", final)
    return final

choice = input(" 1. Encrypt message\n 2. Decrypt message\n 3. Exit program\nSelect an option:-- ")
if choice == '1':
    plain = input("Enter plaintext to encrypt by ROT13: ")
    encrypt(plain)
    os.system('pause')
elif choice =='2':
    cipher = ("Enter ROT13 ciphertext to decrypt: ")
    encrypt(cipher)
    os.system('pause')
else:
    exit
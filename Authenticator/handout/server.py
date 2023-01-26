from names import get_name
from secret import key,flag
from Crypto.Cipher import AES
from os import urandom
from random import randint

def get_token():
    cipher = AES.new(key,AES.MODE_CBC,urandom(16))
    auth = '{"user":'+get_name()+',"userId":"'+str(randint(0,100))+'","isWorking":"idk!!","admin":"no!"}'
    auth = auth.encode()
    return cipher.encrypt(auth).hex()

def get_decrypted(cipherText):
    try:
        cipherText = bytes.fromhex(cipherText)
    except:
        print(""" HEX?? """)
        return None

    cipher = AES.new(key,AES.MODE_ECB)
    l=0
    if len(cipherText)%16==0:
        plaintext = cipher.decrypt(cipherText).hex()
    
    else:
        l=16-(len(cipherText)%16)
        cipherText+=b'x\00'*l
        plaintext = cipher.decrypt(cipherText)

    return plaintext[:len(plaintext)-l]

def verify(cipherText,iv):
    try:
        cipherText = bytes.fromhex(cipherText)
        iv=bytes.fromhex(iv)
    except:
        print("""    HEX??    """)
        return False

    try:
        cipher = AES.new(key,AES.MODE_CBC,iv)
        x=eval(cipher.decrypt(cipherText).decode())
        if x['user']=="4n4c15t":
            if x["admin"]=='yes':
                return True
            else:
                return False
        else:
            return False
    except:
        print('Are sure that is the correct cipherText')


if __name__=="__main__":

    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣰⣿⣿⣒⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡝⢿⣿⣽⢿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣤⣽⣷⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣸⣿⣭⣭⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣷⡶⠶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣯⡿⠿⠾⠿⠾⠿⢿⣷⣥⣄⣀⠙⡗⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣻⡿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠙⣛⠻⢿⣳⢤⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣆⣴⠋⠀⠀⠀⠀⠀⢀⣾⣿⣆⠀⠀⠀⠀⣸⡟⢧⠀⢹⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⡀⠀⠀⠀⠀⢸⣿⣯⣽⠀⠀⠀⠰⣿⣿⣿⠀⣬⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣯⣷⡀⠀⠀⠀⡘⣿⣇⣝⣀⣤⠤⢤⣿⣧⣏⡀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡿⣄⠀⠀⠈⠉⢀⡀⠀⠀⠀⠀⠀⣀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⠀⠀⠀⠀⠉⠢⢤⣀⣀⠤⠖⠉⠀⢸⢻⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢈⣿⣫⣤⡤⠤⠶⠶⠒⠒⠒⠒⠒⠒⠒⠒⠬⠾⣄⣀⣠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡼⣏⠉⠁⣀⠀⠀⠀⣀⣀⣀⡠⠤⠤⠤⠤⣀⣀⡴⠀⠆⣿⠁⠀⠀⢠⢀⣀⣤⣸⠉⣧⠀⠀⠴⠄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠞⠁⠀⠘⣆⠀⠸⣶⣯⡭⠥⠞⠒⠓⠒⠒⠒⠒⢶⢊⠇⠀⣼⣇⣠⣤⣤⣾⡏⣸⣿⠟⠓⠊⢹⣧⣤⣒⣭
⠀⠀⠀⠀⠀⠀⠀⠀⡾⣿⣧⡤⠖⠛⠒⢜⡄⠀⢻⠀⠀⠀⢀⠀⣰⡆⠀⠀⠀⢸⣼⠀⢀⡟⣽⠨⣿⢹⡟⠁⣿⡏⠀⠀⠀⣸⢙⣯⣥⠬
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣃⠔⠉⠉⢹⣿⡄⠘⡇⢆⠀⡼⣀⢿⡇⡆⣰⢀⣼⣿⠰⢼⡇⢸⠇⢿⡈⡧⠀⠸⣿⣄⣀⣶⡿⠿⣈⢙⠆
⠀⠀⠀⠀⠀⢀⡄⢀⣤⡞⡟⣷⣦⣤⣤⡼⠉⡇⠀⢻⠘⢆⠃⣿⠈⣿⢹⡿⠟⣻⡟⠀⣾⠉⠉⠉⠉⠉⠙⠒⠂⠛⠛⠃⠀⠀⠀⠈⠁⠀
⠀⠀⠀⣠⣠⣾⣷⢻⡜⣧⠑⢬⣭⣟⠋⠀⠀⢱⠀⢸⡄⠈⠂⠙⠀⠈⠀⠀⠀⣧⡇⣀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⠘⣿⣌⠻⡈⢳⠿⠻⣿⣓⠀⠀⠈⡷⠀⢧⠀⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⠄⠼⣿⣿⡄⠘⢿⣿⣾⡇⠀⠀⢻⣋⡇⠀⠀⢱⠀⠼⠦⠶⠖⠒⠒⠒⠒⠚⠛⠃⣀⣇⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣹⠶⠀⠘⢿⣿⣦⣀⣉⠽⠃⠀⠀⢈⣿⣗⣀⣀⣸⣤⣠⣤⣔⣦⣶⣤⣠⣤⠤⣦⠶⠞⠿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠙⠶⡷⢠⡶⣄⢹⡍⠁⠀⠀⠀⠀⠀⠀⢀⣸⡯⣍⡙⠳⠮⡏⠉⠹⣿⣏⡠⢊⠩⢷⣀⣶⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠋⠀⠈⠉⠁⠀⠀⠀⠀⠀⢠⣿⣾⣿⡏⠲⢍⣙⣾⠁⠀⠀⠹⣿⡴⢃⡴⠚⠁⠘⢿⣦⡀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⣿⡟⣿⣿⣈⠓⠤⣼⠇⠀⠀⠀⠀⠘⣷⠏⠀⠀⠀⣠⣴⣫⣇⠀⢀⡠⠔⠊⠉⢙⣫⡿⠷⢶⡆⣀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡀⠙⠻⢿⢭⣿⠄⠀⠀⠀⠀⢰⣿⡀⣀⣠⣾⠞⠁⠀⢙⣷⠋⠀⠀⣀⡴⠚⠁⣀⣴⡾⣿⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⣾⣯⣿⠋⠛⠦⣤⣿⣟⠁⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⣤⡀⡠⠋⠀⠀⣠⠞⠁⣠⣴⡿⣿⢙⣾⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠘⢿⣿⣅⡀⣀⣴⡃⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣿⣿⡿⠁⠀⣠⢞⠁⣠⣾⣭⠻⣁⣽⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠀⠈⠙⠹⠋⠉⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⠁⠀⣴⣷⣨⣾⣷⠍⠻⣤⡾⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⣼⣟⣾⣿⢻⣎⡷⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⡄⠀⠀⠀⠀⠀⠀⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⣷⣿⡿⠶⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡀⠀⢤⣀⣤⣾⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢮⣉⠒⠢⣽⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


 _______  __   __  _______  __   __  _______  __    _  _______  ___   _______  _______  _______  _______  ______   
|   _   ||  | |  ||       ||  | |  ||       ||  |  | ||       ||   | |       ||   _   ||       ||       ||    _ |  
|  |_|  ||  | |  ||_     _||  |_|  ||    ___||   |_| ||_     _||   | |       ||  |_|  ||_     _||   _   ||   | ||  
|       ||  |_|  |  |   |  |       ||   |___ |       |  |   |  |   | |       ||       |  |   |  |  | |  ||   |_||_ 
|       ||       |  |   |  |       ||    ___||  _    |  |   |  |   | |      _||       |  |   |  |  |_|  ||    __  |
|   _   ||       |  |   |  |   _   ||   |___ | | |   |  |   |  |   | |     |_ |   _   |  |   |  |       ||   |  | |
|__| |__||_______|  |___|  |__| |__||_______||_|  |__|  |___|  |___| |_______||__| |__|  |___|  |_______||___|  |_|
""")



print("""
 _____      _           _   
/  ___|    | |         | |  
\ `--.  ___| | ___  ___| |_ 
 `--. \/ _ \ |/ _ \/ __| __|
/\__/ /  __/ |  __/ (__| |_ 
\____/ \___|_|\___|\___|\__|
                            
1 -> Get token
2 -> Decrypt
3 -> Verify
4 -> Exit

""")

while True:
    user_input = input("Enter Option : ")

    if user_input=='1':
        print("\n\n\nHere is your tocken : "+get_token()+'\n\n\n')

    elif user_input=='2':
        x=get_decrypted(input('Enter ciphertext (hex) : '))
        if x:
            print("\n\n\nHere is your plaintext (hex) : "+str(x))

    elif user_input=='3':
        if verify(input('Input token Here (hex) : '),input('Input IV Here (hex) : ')):
            print(f'Here is your flag : {flag}')
            exit()

        else:
            print("Who are you")

    elif user_input=='4':
        exit()
    
    else:
        print("""
        
        
        
        Wrong Input
        
        
        """)

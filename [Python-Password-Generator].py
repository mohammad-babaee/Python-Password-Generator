import string
import secrets
import random

cutie = random.randint(369 , 999666333)

user_input = ""

print ('''

             .-"""-.
            /       )
            \       /
     .-"""-.-`.-.-.<  _
    /      _,-\ O_O-_/ ) 
    \     / ,  `   . `|
     '-..-| \-.,__~ ~ /        
           \ `-.__/  /         
          / `-.__.-\`-._    ,",          ------------------------
         / /|    ___\-._`-.;  , .----.   ||     S I M I N      ||
        ( ( |.-"`   `'\ '-(     -.---'   ||   SECURE PASSWORD  ||  
         \ \/    {}{}  |   \.__.-'       ||  G E N E R A T O R ||
          /|            )                || [Random Passwords] ||
          \|           /                 ||   Version:1.1.1.1  ||
           \        , /                  ||  Script Coded By : || 
           ( __`;-;'__`)                 ||   Mohammad Babaee  ||
           `//'`   `||`                  ------------------------
          _//       ||
  .-"-._,(__)     .(__).-""-.
 /          \    /           )
 \          /    \           /
  `'-------`      `--------'`
----------------------------------------------------------------
>>> What Type Of Password Is Your favorite ?
    1 - Secure Password [With Special Characters]
    2 - Very Strong Secure Password [With Special Characters & Numbers]
    3 - Normal Password [Classic Secure Password]
----------------------------------------------------------------
    ''')

user_input = str(input(">>> Please Enter The Number Of The List (From 1 to 3) : "))

if user_input == "1":
    special_char1 = "~!@#$%^&*()-_=+"
    alphabet = string.ascii_letters + str(cutie) + string.digits + special_char1
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(39))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 9):
            break

    print (" ---------------------------------------------------------------- ")
    print (" \n ")
    print("|||>>>   The Strong Password [With Special Characters] : " + str(password) )
elif user_input == "2":
    special_char1 = "~!@#$%^&*()-_=+"
    special_num_arr = "0123456789"
    alphabet = string.ascii_letters + str(cutie) + string.digits + special_char1 + special_num_arr
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(39))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 9):
            break
    
    print (" ---------------------------------------------------------------- ")
    print (" \n ")
    print("|||>>>   The Strong Password [With Special Characters & Extra Security] : " + str(password) )
else:
    alphabet = string.ascii_letters + str(cutie) + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(39))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 9):
            break

    print (" ---------------------------------------------------------------- ")
    print (" \n ")
    print("|||>>>   The Normal Classic Password : " + str(password) )

print (" \n ")
print (" --------- Follow Me On Github : @mohammad-babaee --------- ")
print (" \n ")
print ("   ------ This App Is Published Under (MIT License) ------ ")
print (" \n ")
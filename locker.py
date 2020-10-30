#!python3
#locker.py
password={'email':'My love is crush',
          'fb':'dkfjkdf',
          'sabiha':'dkfkdk'}
import sys,pyperclip
if len(sys.argv)<2:
    print('Usage: python locker.py acountname')
    sys.exit()
acount=sys.argv[1]
if acount in password:
    pyperclip.copy(password[acount])
    print("your password is copied")
else:
    print("you dint copied")
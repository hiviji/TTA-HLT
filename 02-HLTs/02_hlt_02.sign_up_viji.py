import string
import sys

username = input("Enter username: ") 

if len(username) >15 or len(username)<6:
    print("Username should be between 6 and 15 chartacters.")
    sys.exit(1)

if not username[0].isupper():
    print("Username should start with Uppercase.")
    sys.exit(1)  

#get and validate password
password = input("Enter password: ")

if len(password) >256 or len(password)<8:
    print("Password should be between 8 and 256 chartacters.")
    sys.exit(1)

if ' ' in password:
   print("no spaces should in password")
   sys.exit(1)

if password.find(username)>0:
   print("Password shouldn't contain username")
   sys.exit(1)

if ('(' or ')' or '{' or '}' or '[' or ']') in password:
  print("no brackets should in password")
  sys.exit(1)

#get the password again and validate
reentered_password=input("Re-enter password: ")

if password != reentered_password:
   print ("The second password entry must match the first one")
   sys.exit(1)

#print(username)
#print(password)
#print(reentered_password)
#print(password.find(username))

print("Thank you. You are now signed up.")

import string
import secrets

number= string.digits
otp=''

for i in range(4):
    otp+=''.join(secrets.choice(number))

print(otp)

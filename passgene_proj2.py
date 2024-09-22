import random
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['#','$','%','^','&','*','(',')']
let=int(input("Number of letters: "))
num=int(input("Number of numbers: "))
sym=int(input("Number of symbols: "))
passw=""
for i in range(0,let):
    letter=random.choice(letters)
    passw=passw+letter
for i in range(0,num):
    number=random.choice(numbers)
    passw=passw+number
for i in range(0,sym):
    symbol=random.choice(symbols)
    passw=passw+symbol
password=list(passw)
random.shuffle(password)
fin=""
for ch in password:
    fin+=ch
print(fin)




import random 
z =random.randint(1,6)

x = int (input ("hats khod ra vared konid: "))
count   = 1
while x !=  z :
    x = int (input("hats khod ra vared konid: "))
    count+=1
else :
    print("barikala")
    print(f"shoma dar {count} talash moafagh shoodid. ")
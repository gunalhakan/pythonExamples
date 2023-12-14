# * işaretini kullanarak aşağıdaki görünümü elde eden kodu döngü kullanarak yazınız.
'''
***********
 *********
  *******
   *****
    ***
     *
'''
'''
print("*"*11)
print(" ","*"*9," ",sep="")
print("  ","*"*7, "  ",sep="")
print("   ","*"*5, "   ",sep="")
print("    ","*"*3,"    ",sep="")
print("     ","*"*1,"     ",sep="")

for i in range(11):
    print("*",end="")
print()
print(" "*1,end="")
for i in range(9):
    print("*",end="")
print()
print(" "*2,end="")
for i in range(7):
    print("*",end="")
print()
print(" "*3,end="")
for i in range(5):
    print("*",end="")
print()
print(" "*4,end="")
for i in range(3):
    print("*",end="")
print()
print(" "*5,end="")
for i in range(1):
    print("*",end="")
print()
'''
for i in range(6):
    print(" "*i,end="")
    for k in range(11-(i*2)):
        print("*",end="")
    print()
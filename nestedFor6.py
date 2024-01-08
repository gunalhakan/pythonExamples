
for i in range(5):
    for k in range(5):
       
        if i > 0 and i < 4:
            if k == 0 :
                print("* ", end="")
            elif k == 4:
                print("* ", end="")
            else:
                print(" ",end=" ")
        else:
             print("* ", end="")
    
    print()

'''
print("* "*10)
for i in range (8):
    print("*                 *")
print("* "*10)
'''

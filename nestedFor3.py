#0, - ve + karakterlerini kullanarak aşağıdaki şekli ortaya çıkartan programı yazınız.
'''
0 - - - - - - - - - 
+ 0 - - - - - - - - 
+ + 0 - - - - - - - 
+ + + 0 - - - - - - 
+ + + + 0 - - - - - 
+ + + + + 0 - - - - 
+ + + + + + 0 - - - 
+ + + + + + + 0 - - 
+ + + + + + + + 0 - 
+ + + + + + + + + 0 
'''
for i in range(1,11):
    for k in range(1,11):
        if i == k :
            print("0",end=" ")
        elif i > k :
            print("+", end=" ")
        else:
            print("-", end=" ")
    print()
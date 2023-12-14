#Döngüleri kullanarak 1 den 10 a kadar olan sayıların olduğu bir çarpım tablosu yapınız
for i in range(1,11):
    for k in range(1,11):
        print(i*k, end="\t")
    print()
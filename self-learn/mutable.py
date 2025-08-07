#mutable
#def changeA(a):
#    print('1,before assign:',a) #3
#    a = 1
#    print('2,after assign:',a) #1
#    return a



#    a=[3]
#    changeA(a)
#    print('3,final:',a)#[1]

#immutable
#def changeB(b):
#        b = 1
#        return b

#        b = 3
#        changeB(b)
#        print(b)


#a =1
#b =[1,2,3,4]
#c=1.3 #float
#d={'a'=100}
#print("this value for key a:",d["a"])
#d["a"]= 101
#print(d)
#print({1,1,2,2,3})

#a = 11 / 10
#print(a)

#a = 1.0#folat
#print(a)

#print(int(a))
#print(str(a) + "b")

try:
    print('this is beginning')
    int("a")
    print('this is not reachable')

except:
    print(1)

    for i in range(5):
        if i >=4:
            print("")
            #couninue
        print(i)
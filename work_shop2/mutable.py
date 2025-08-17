# #mutable
# def changeA(a): #5dc23d
#     print('1, before assign:', a) # [3]
#     a[0] = 1 # [3] => [1]
#     print('2, after assign:', a) # [1]
#     return a

# a = [3] #5dc23d
# a = changeA(a)
# print("3, final: ", a) # [1] #5dc23d

# #immutable
def changeB(b):
    b = 1
    return b
    c = 2
    def changeC(c):
        b = c

c =2
# b = 3
# changeB(b)
# print(b)

# a = 1
# b = [1, 2, 3, 4, 5]
# c = 1.3 #float
# d = {"a" : 100}
# # print("this is value for the key a:", d["a"])
# d["a"] = 101
# print(d)
# print({1,1,2,2,3})


# a = 12 / 10
# print(a)
# a = 12 % 10
# print(a)
# a = 12 // 10
# print(a)

# a = "1"# string
# print(a)
# a = 1 # Integer
# print(a)
# a = 1.0 # float
# print(a)

# print(int(a))
# print(str(a) + "b")

# try:
#     print('this is beginning')
#     int("a")
#     print('this is not reachable')
# except:
#     print(1)


# for i in range(5):
#     if i == 2:
#         break
#     print(i)
# b = 1
# b = 1
def foo(a):
    global b
    b = 102
    print(b)
    def foo_child():
        b = 101
        print(b + 1)
    foo_child()

foo(1)
c = b + 1
print(c)



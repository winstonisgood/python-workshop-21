b=100

def foo(a):
    b=100
    print(b)
    def foo_child():
        print(b+1)
    foo_child()

foo(1)
c= b +1
print(c)
print('helloword')


def function(b):
    b = [2 ,3] # refresh address, address2
    b.append(4)
    print("Value of b in function:", b)
    return b

b = [1, 2, 3] # address 1
function(b)
print("Value of b out of function:", b)

#0 ,1 ,2, 3, 4, 5 integer

a = 1 # find a address for a, assign a value to a, define the type for a;
1
a = 1
a = "abc"
a = [1,2,3,4]
b = a
a = 1;
b = a;
# Array a; # find a address for a
# a = [1, 2, 3]; # find a address for [1,2,3], create the array, point to a

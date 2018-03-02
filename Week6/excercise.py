"""
Robert W. Curtiss
6/26/2018
"""


def sqrt(n):
    return n ** .5


def exp(n, m):
    return n ** m


print(sqrt(4))
print(sqrt(64))
print(exp(4, 2))
print(exp(5, 2))
print(exp(5, 4))

some_list = ["Line 1\n", "line 2\n", "line 3\n"]

f = open("fun.txt", "w")
f.write("this is line 1\n".capitalize())
f.write("this is line 2\n".capitalize())
f.write("this is line 3\n".capitalize())
f.close()


def read_the_file():
    print("====================")
    f = open("fun.txt", "r")
    lines = f.readlines()
    for l in lines:
        print(l, end='')
    f.close()
    print("====================")

read_the_file()

f = open("fun.txt","w")
f.writelines(some_list)
f.close()

read_the_file()




input("Press enter to continue!")

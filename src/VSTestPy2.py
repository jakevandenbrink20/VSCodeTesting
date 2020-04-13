import sys

from icecream import ic

print("\n")
print(sys.version, "\n")
print(sys.executable, "\n")

x = input("Enter input: ")
print(x)

print("#00BCD4")
print("#103C24")
print("Hi")
# print("\x1b[0;30;47m#00BCD4")


def myPrintFunction(arg):
    testvar = "test"
    print(arg)
    return "Joe"


myPrintFunction("Hello World")
print("\n")

ic("Testing icecream module")
ic(myPrintFunction("Icecream function"))

# greetings == "joe"

import os

from art import logo


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def rem(a,b):
    return a%b

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
    "%" : rem
}

#< Using Loop
# choice = True
# while(choice):
#     a = float(input("What's the first number?: "))
#     choice2 = True
#     ans = 0
#     while (choice2):
#         for ops in operations:
#             print(ops)

#         op = input("Pick an operation: ")
#         operation = operations[op]
#         b = float(input("What's the next number?: "))

#         ans = operation(a,b)

#         print(f"\n{a} {op} {b} = {ans}\n")
#         a = ans
         # ch = input(
         #   f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new 
         #   calculation, or type 'e' to exit: ")
#         if ch == 'n':
#             choice2 = False
#             os.system('cls')
#         elif ch == 'e':
#             choice2 = False
#             choice = False

#< Using Recursion
def calculator():
    print(logo)
    a = float(input("What's the first number?: "))
    def continue_calculator(a):
        for ops in operations:
            print(ops)

        op = input("Pick an operation: ")
        operation = operations[op]
        b = float(input("What's the next number?: "))

        ans = operation(a,b)

        print(f"\n{a} {op} {b} = {ans}\n")
        a = ans
        ch = input(f"Type 'y' to continue calculating with {ans}, or  type 'n' to start a new calculation, or type 'e' to exit: ")
        if ch == 'n':
            os.system('clear')
            return calculator()
        elif ch == 'y':
            continue_calculator(a)
        elif ch == 'e':
            return
    continue_calculator(a)
    return

calculator()
# Simple Calculator by Abhishek B

# takes first number as input from the user
firstnum = int(input("Enter the first number: "))
# takes second number as input from the user
secondnum = int(input("Enter the second number: "))

# user_defined sum function


def add_num(num1, num2):
    sum_result = num1 + num2
    print("The sum of given 2 numbers is: ")
    return sum_result


def sub_num(num1, num2):
    sub_result = num1 - num2
    print("The difference of given 2 numbers is: ")
    return sub_result


def mul_num(num1, num2):
    mul_result = num1 * num2
    print("The product of given 2 numbers is: ")
    return mul_result


def div_num(num1, num2):
    div_result = num1 / num2
    print("The quotient of given 2 numbers is: ")
    return div_result


def mod_num(num1, num2):
    mod_result = num1 % num2
    print("The remainder of given 2 numbers is: ")
    return mod_result


def pow_num(num1, num2):
    pow_result = num1 ** num2
    print("The exponentiation is: ")
    return pow_result


print(add_num(firstnum, secondnum))
print(sub_num(firstnum, secondnum))
print(mul_num(firstnum, secondnum))
print(div_num(firstnum, secondnum))
print(mod_num(firstnum, secondnum))
print(pow_num(firstnum, secondnum))

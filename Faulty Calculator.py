num1 = int(input("Enter first integer "))
num2 = int(input("Enter second number "))
print("Choose an operator from following\n","+,-,*-/,%,**")
operator = input()
if operator == '+':
    if num1 == 56 and num2 == 9:
        print(77)
    else:
        num3 = num1 + num2
        print(num3)
if operator == '/':

    num3 = num1 / num2
    print(num3)
if operator == '-':

    num3 = num1 - num2
    print(num3)
if operator == '*':

    num3 = num1 * num2
    print(num3)
if operator == '**':

    num3 = num1 ** num2
    print(num3)
if operator == '%':

    num3 = num1 % num2
    print(num3)

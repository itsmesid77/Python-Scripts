def calculator(num1,sign,num2):
    if sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2
    elif sign == "*":
        return num1 * num2
    elif sign == "/":
        return num1/num2
    elif sign == "%":
        return num1%num2
    elif sign == "**":
        return num1**num2
    elif sign == "//":
        return num1//num2
a = int(input("Enter first number: "))
b = input("Enter Operation: ")
c = int(input("ENter the 2nd number: "))
print("Your Answer is:", calculator(a,b,c) )
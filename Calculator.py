def calculator(num1,sign,num2):
    if sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2
    elif sign == "/":
        return num1/num2
    elif sign == "%":
        return num1%num2
    elif sign == "**":
        return num1 ** num2
    elif sign == "//":
        return num1 // num2
    elif sign == "*":
        return num1 * num2

a = int(input("Enter First Number: "))
b = input("Enter Operation to be Performed: ")
c = int(input("Enter Second Number: "))
print("Your Answer is : ", calculator(a,b,c))
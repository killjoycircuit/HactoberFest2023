a=float(input("Enter your 1st no "))
c=str(input("Enter operator "))
b=float(input("Enter your 2nd no "))
match c:
    case '+':
        print("The ans is ",a+b)
    case '-':
        print("The ans is ", a-b)
    case '*':
        print("The ans is ", a*b)
    case '/':
        print("The ans is ", a/b)
    case '**':
        print("The ans is ", a**b)
    case '%':
        print("The ans is ", a%b)

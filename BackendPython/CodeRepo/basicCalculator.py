num1 = (input('Enter First Number'))
num2 = input('Enter Second Number')
operator = input('Enter Operator')

if operator == '+': 
    print(int(num1) + int(num2))

elif operator == '-':
    print(int(num1) - int(num2))

elif operator == '*': 
    print(int(num1) * int(num2))

elif operator == '/':
    print(int(num1) / int(num2))

else:
    print("invalid operator")




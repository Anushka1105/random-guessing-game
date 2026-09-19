print('''
    + add
    - subtract
    * multiply
    / divide
''')

num1= int(input("Enter num1:"))
num2= int(input("Enter num2:"))
op=input("Enter op:")

if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num1/num2)
else:
    print("Invalid operator")


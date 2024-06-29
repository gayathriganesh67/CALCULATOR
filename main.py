print("-------calculator allows the user to perform the following operations------")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
print("5.REMAINDER")

operation = input("Enter the operation you want to perform:")

if operation=="1":
  num1= int(input("Enter the first number:"))
  num2=int(input("Enter the second number:"))
  sum=print("The sum of two numers:",num1+num2)
elif operation=="2":
  num1= int(input("Enter the first number:"))
  num2=int(input("Enter the second number:"))
  sub=print("The difference of two numbers is:",num1-num2)
elif operation=="3":
  num1= int(input("Enter the first number:"))
  num2=int(input("Enter the second number:"))
  mult=print("The multiplication of two numbers:",num1*num2)
elif operation=="4":
  num1= int(input("Enter the first number:"))
  num2=int(input("Enter the second number:"))
  div=print("The division of two numbers:",num1/num2)
elif operation=="5":
  num1= int(input("Enter the first number:"))
  num2=int(input("Enter the second number:"))
  rem=print("The remainder of two numbers:",num1%num2)
else:
  print("operation is invalid")
  

print("Welcome".center(50),"\n")
print("1. For Addition  '+' \n2. For Subtraction  '-' \n3. For Multiplication  '*' \n4. For Division '/' \n5. For Exponent  '^' ")
print("6. For Result  '=' ")
num =float(input("Enter the number: "))# First number
var=input("Enter the operator: ")# First Operator

# Calculator function using recursion

def calculator(num,var):
    # Addition
     if var=='+':
           num2=float(input("Enter the number: "))
           num= num +num2
           var=input("Enter the operator: ")
           calculator(num,var)
     # Subtraction
     elif var=='-':
         num2=float(input("Enter the number: "))
         num=num-num2
         var=input("Enter the operator: ")
         calculator(num,var)
     # Multiplication
     elif var=='*':
         num2 = float(input("Enter the number: "))
         num = num * num2
         var = input("Enter the operator: ")
         calculator(num,var)
    # Division
     elif var=='/':
         num2 = float(input("Enter the number: "))
         if num2 == 0:
             print("Error: Cannot divide by zero.")
             return
         num=  num / num2
         var = input("Enter the operator: ")
         calculator(num,var)
    # Exponent
     elif var=='^':
         num2 = float(input("Enter the number: "))
         num=  num ** num2
         var = input("Enter the operator: ")
         calculator(num,var)
    # Result
     elif var=='=':
         print(">>",num)
         return
     # Invalid Entry
     else:
         print("\nINVALID OPERATOR!!!!!!!!!!!!!!!")
         return
calculator(num,var) #Starting the function


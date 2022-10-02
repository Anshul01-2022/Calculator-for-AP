#Its a calculator for Hacktoberfest.
#Created by Anshul
while(True):
    n=int(input("Operations:\n \t1)Sum\n\t2)Multiplication\n\t3)Division\n\t4)Quit\nInput: "))
    if(n==4):
        print("Exiting..")
        break
    x = int(input("Please enter a number?"))
    y = int(input("Enter another number?"))
    if(n==1):
        print("Sum is ",x+y)
    elif(n==2):
        print("Multiplication is",x*y)
    #Develop more operations
        

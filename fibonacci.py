a=int(input("Enter how many Fibonacci numbers to print:"))
print(a)
if a>0:
    x,y=0,1
    for i in range(a):
        print(x)
        x,y=y,x+y  
else:
    print("You entered an invalid number.")

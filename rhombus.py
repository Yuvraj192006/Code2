a=int(input("Enter a number"))
if a%2==0:
    print("Enter an odd number")
else:
    b=(a+1)//2
    for i in range(1,b+1):
            spaces=" " * (b-i)
            stars=i*"* "
            print(spaces+stars)
    for n in range(b-1,0,-1):
        spaces=(b-n)*" "
        stars=n*"* "
        print(spaces+stars)

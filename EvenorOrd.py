number=int(input("Enter a number to check if it is odd or even: "))
def even_or_odd(number):
    
    if(number%2==0):
        print(number," is an even")
    else:
        print(number," is an odd")
even_or_odd(number)
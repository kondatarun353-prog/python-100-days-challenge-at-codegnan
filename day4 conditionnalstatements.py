#if the given number is zero
num = int(input())
if num == 0:
    print("number is zero")
print("program executed")


#check if the given number is even or odd
num=int(input("enter the number:"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")
    

#check whether given  number is zero,even or positive
num=int(input('enter a number:'))
if (num%2==0 and num>=0):
    print('number even and positive')
elif (num%2!=0 and num<0):
    print('number is odd and negative')
elif (num%2!=0 and num==0):
    print('number is odd and positive')
elif (num%2==0 and num!=0):
    print('number is even and negative')
print('program executed')

            
# check whether the given number is factor of 3 and 5

n=int(input("enter a number: "))
if n%5==0 and n%3==0:
    print("numer is a factor of 5 and 3")
elif n%5==0 and n%3!=0:
    print("number is a factor of 5 but not 3")
elif n%5!=0 and n%3==0:
    print("number is a factor of 3 but not 5")
else:
    print("number is not factor of 5 and 3")        

 

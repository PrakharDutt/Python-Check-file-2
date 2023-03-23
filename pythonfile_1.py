#  code for checking wether a number is prime or not 

def func_prime_or_not (input_a):
    count=1
    for i in range (2,input_a):
        if(input_a==1):
            print(f"{input_a } is neither a prime nor a composite number")
        elif(input_a%i==0):
            count=count+1
        # print(i)
    else:
        count=count+0

    if(count==1 and input_a!=1):
        return(print(f"the {input_a } is a prime number "))
    else:
        return(print(f"the {input_a } is a not a prime number .i.e. is a composite number  "))
    



input_a=int(input("enter the number 1 \n"))
func_prime_or_not(input_a)

print("jai sia ram jai sia ram jai sia ram")


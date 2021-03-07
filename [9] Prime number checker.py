
def prime_checker(number):
    is_prime = True
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
        if is_prime:
            print("The number is a prime number.")
        else:
            print("The number is not a prime number.")
    else:
        print("number is not a prime number")
        
print("Welcome to Python prime number checker!")

n = int(input("Check this number: "))
prime_checker(number=n)

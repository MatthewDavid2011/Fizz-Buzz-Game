This game prints "fizz" when a number is divisible by 3, prints "Buzz" if a number is divisible by 5", prints "FizzBuzz if a number is divisible by both 5 and 3 else prints the number as it is.

        #Fizz Buzz Game Solution

for number in range (1,101):
    if number %5 ==0 and number %3 ==0:
        print("fizz buzz")
    elif number %5 == 0:
        print("buzz")
    elif number %3 ==0:
        print("fizz")
    else:

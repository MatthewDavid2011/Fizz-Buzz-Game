#Fizz Buzz Game Solution

for number in range (1,101):
    if number %5 ==0 and number %3 ==0:
        print("fizz buzz")
    elif number %5 == 0:
        print("buzz")
    elif number %3 ==0:
        print("fizz")
    else:
        print(number)
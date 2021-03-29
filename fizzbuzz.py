
def Fizz(a = 0, b = 0):
    for number in range(a, b):
        # if number % 3 == 0 and number % 5 == 0:
        #     print('FizzBuzz')
        if number % 3 == 0:
            print('Fizz')
        # elif number % 5 == 0:
        #     print('Buzz')
        else:
            print(number)
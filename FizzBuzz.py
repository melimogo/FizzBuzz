print('Fizz_buzz :)')

def Fizz_buzz():
    for i in range(1,100):
        if(i % 3 == 0 and i % 5 == 0):
            # if the number is multiple of 3 and 5, print fizzBuzz
            print('fizzBuzz')
        elif(i%3 == 0):
            # if the number is multiple of 3, print fizzBuzz
            print('fizz')
        elif(i%5 == 0):
            # if the number is multiple of 5, print fizzBuzz
            print('Buzz')
        else:
            print(i)

Fizz_buzz()

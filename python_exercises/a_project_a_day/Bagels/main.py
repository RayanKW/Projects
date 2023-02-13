import random

num_digits = 3
max_guess = 10

def main():
    print('''Bagels, a deductive logic game.
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:
That means:
Pico
One digit is correct but in the wrong position.
Fermi
One digit is correct and in the right position.
Bagels
No digit is correct.
For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(num_digits))
    while True:
        secrete_num = getSecreteNum()
        print('I have thought of a number')
        print('you have {} guesses to get it.'.format(max_guess))
        numGuesses = 1
        while numGuesses <= max_guess:
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print('guess #{}: '.format(numGuesses))
                guess = input('> ')
                
                clues = getClues(guess, secrete_num)
                print(clues)
                numGuesses +=1
                if guess == secrete_num:
                    break
                if numGuesses  > max_guess:
                    print('ran out of guesses')
                    print('the answer was {}.'.format(secrete_num))
        print('do you want to play again? Y)ess or N)o')
        if not input('> '.lower().startswith('y')):
            break
    print('Thanks for playing')
def getSecreteNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secrete_num = ''
    for i in range(num_digits):
        secrete_num += str(numbers[i])
    return secrete_num
def getClues(guess, secrete_num):
    if guess == secrete_num:
        return 'you\'ve got it'
    clues = []
    for i in range(len(guess)):
        if guess[i] ==secrete_num[i]:
            clues.append('fermi')
        elif guess[i] in secrete_num:
            clues.append('pico')
    if len(clues) ==0:
        return 'bagels'
    else:
        clues.sort()
        return ' '.join(clues)
if __name__ == '__main__':
    main()
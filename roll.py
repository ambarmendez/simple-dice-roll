from random import randint

while True:

    n_roll_input = input('Times for rolling the dice: ')
    if n_roll_input.isnumeric():
        for _ in range(int(n_roll_input)):
            value = randint(1, 6)
            print(value)
    else:
        print(n_roll_input, 'is not a number.')

    option = input('Roll again? ')
    if option.lower() == 'yes' or option.lower() == 'y':
        continue
    else:
        break

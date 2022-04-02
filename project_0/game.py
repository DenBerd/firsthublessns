"""Guess a number game"""

import numpy as np

number = np.random.randint(1,100)

count = 0

while True:
    count += 1
    predict_number = int(input('Guess a number 1 to 100: '))
    
    if predict_number > number:
        print('The number is less')
        
    elif predict_number < number:
        print('The number is more')
        
    else:
        print(f"You guessed in {count} tries! It's {number}")
        break        

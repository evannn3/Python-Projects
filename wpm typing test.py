import random
import time

options = 'about', 'after', 'again', 'alone', 'apple', 'beach', 'begin', 'below', 'black', 'brave', 'bread', 'bring', 'brown', 'build', 'carry', 'catch', 'chair', 'child', 'clean', 'clear', 'clock', 'cloud', 'dance', 'dream', 'drink', 'drive', 'early', 'earth', 'eight', 'every', 'field', 'final', 'first', 'found', 'fresh', 'glass', 'great', 'green', 'happy', 'heart', 'house', 'large', 'learn', 'light', 'money', 'music', 'night', 'ocean', 'paint', 'paper',
print ('Typing game starting..')
gah = input("Type 'start' when you're ready: ")
while True:

  if  gah.lower() == 'start':
      break
while True:


    e = random.choice(options)
    f = random.choice(options)
    g = random.choice(options)
    h = random.choice(options)
    b = random.choice(options)

    hi = (e + ' ' +  f +' '+ g +' '+ h + ' '+b)

    hey = time.time()
    ez = input('Type ' + '[ ' +  hi + ' ] ' + 'as fast as you can:  ')
    end = time.time()
    lol = end - hey
    hep = str(lol)
    hah = 60/lol
    la = hah*5

    if ez == hi:

        print('You can type ' + str(la) + ' words in a minute! (wpm)')
        what = input('Do you want to retry? (yes/no): ')
        if what == 'no':
            break
    elif ez is not hi:
        print('You made a spelling mistake. ')
        what = input('Do you want to retry? (yes/no): ')
        if what == 'no':
            break


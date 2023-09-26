import random

greeting = ['Hello there!', 'Hello Yellow!', 'Heya!']
for _ in range(1): 
  print(random.choice(greeting))
#https://stackoverflow.com/questions/63571701/python-random-change-random-value-from-list-each-time-i-use-print

print()

name = input('May I please get your name?: ')

print()

age = input(f'And your age, {name}?: ')

print()

opener = ['alrighty then', 'okie-dokie', 'Now lets get to buisness']
for _ in range(1): 
  print(f'{random.choice(opener)}, {name}!')

print()

print('Lets see how may I help you today!')
choice = input('please choose the following from the list,\n(1):Place holder\n(2):Place holder\n(3):Place holder\n(4):Exit\n\n:')
while choice != '4':
  if choice == '1':
    print('Sorry! but due to lack of code, their isnt anything here for you!')
  elif choice == '2':
    print('sorry, nothin, nill!')
  elif choice == '3':
    print('▒▒▒▒▒▒▒▒▒▄▄▄▄▒▒▒▒▒▒▒\n▒▒▒▒▒▒▄▀▀▓▓▓▀█▒▒▒▒▒▒\n▒▒▒▒▄▀▓▓▄██████▄▒▒▒▒\n▒▒▒▄█▄█▀░░▄░▄░█▀▒▒▒▒\n▒▒▄▀░██▄░░▀░▀░▀▄▒▒▒▒\n▒▒▀▄░░▀░▄█▄▄░░▄█▄▒▒▒\n▒▒▒▒▀█▄▄░░▀▀▀█▀▒▒▒▒▒\n▒▒▒▄▀▓▓▓▀██▀▀█▄▀▀▄▒▒\n▒▒█▓▓▄▀▀▀▄█▄▓▓▀█░█▒▒\n▒▒▀▄█░░░░░█▀▀▄▄▀█▒▒▒\n▒▒▒▄▀▀▄▄▄██▄▄█▀▓▓█▒▒\n▒▒█▀▓█████████▓▓▓█▒▒\n▒▒█▓▓██▀▀▀▒▒▒▀▄▄█▀▒▒\n▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
  else:
    print(f'\nSorry {name}! thats not an option,')
  choice = input(':')

print('\nalright, ciao! for variation in conversation, try starting the code again! there are 6 alternating messages!')

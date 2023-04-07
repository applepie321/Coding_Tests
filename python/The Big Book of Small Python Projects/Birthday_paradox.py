import datetime, random


def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA

print("intro")
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBdays = int(response)
        break
print()

print('Here are', numBdays, 'birthdays:')
birthdays = getBirthdays(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month -1]
    dateText = f'{monthName} {birthday.day}'
    print(dateText, end='')
print()
print()

match = getMatch(birthdays)

print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = f'{monthName} {match.day}'
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

print('Generating', numBdays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0
for i in range(100000):
    if i % 10000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBdays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

probability = round(simMatch / 100000 * 100, 2)
print('Out of 100,000 simulations of', numBdays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')





"""
The Birthday Paradox, also called the Birthday Problem, is the surprisingly high probability 
that two people will have the same birthday even in a small group of people. In a group of 70 people, 
there’s a 99.9 percent chance of two people having a matching birthday. But even in a group as small as 23 people, 
there’s a 50 percent chance of a matching birthday. 
This program performs several probability experiments to determine the percentages for groups of different sizes. 
We call these types of experiments, in which we conduct multiple random trials to understand the likely outcomes, Monte Carlo experiments.

You can find out more about the Birthday Paradox at https://en.wikipedia.org/wiki/Birthday_problem.
"""

"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, math, simulation"""
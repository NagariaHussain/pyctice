import yaml
import markdown

from pprint import pprint
with open('tests.yaml', 'r') as yamlfile:
    test_data = yaml.load(yamlfile.read(), Loader=yaml.Loader)
    pprint(test_data)

print(markdown.markdown('''
# H1
* 1 - *one*
* 2 - **two**
* 3
[Link](http://google.com "Title text")
'''))

import random
 
highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
 
print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())
 
while guess != answer:
    if guess < answer and guess != 0:
        print("Please guess higher")
        guess = int(input())
    elif guess == 0:
        quit()
    else:
        print("Please guess lower")
        guess = int(input())
print("You guessed the number correctly")
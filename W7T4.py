import random
Quote = ('inspirationalquotes.txt', 'r')

def random_line(Quotes):
    lines = open(Quotes).read().splitlines()
    return random.choice(lines)
print(random_line('inspirationalquotes.txt'))
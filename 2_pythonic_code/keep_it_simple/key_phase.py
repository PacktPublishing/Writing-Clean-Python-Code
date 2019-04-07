import random

"""Find a random letter in a password num times """

num = 3
password = "thisisaveryweakpassword"


""" Complicated example """
choices = []
for x in range(num):
    choice = random.choice(password)
    choices.append(choice)

print(choices)

""" Simple example """
key_phase = random.sample(password, num)

print(key_phase)



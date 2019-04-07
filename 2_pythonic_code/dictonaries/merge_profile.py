name = {'first_name': 'Peter', 'last_name': 'Fisher'}
job = {'company': 'Websomatic', 'role': 'Co Founder'}
contact = {'twitter': 'pfwd', 'youtube': 'howtocodewell'}


""" Example 1: Very clunky and complicated """
items = [name, job, contact]
profile1 = {}

for i in items:
    for s in i:
        profile1[s] = i[s]

print("Example 1: Multiple for loops")
print(profile1)


""" Example 2: More pythonic """
profile2 = {}
profile2.update(name)
profile2.update(job)
profile2.update(contact)

print("Example 2: Pythonic update a dictionary")
print(profile2)

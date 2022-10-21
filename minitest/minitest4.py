#6
# stats = {
#     'Name': 'Light',
#     'Age': 17,
#     'Strength': 8,
#     'Defense': 10,
#     'HP': 100,
#     'Backpack': ['Shield', 'Bread Loaf'],
#     'Gold': 100,
#     'Level': 2
# }

# stats.update({'Gold':150})
# print(stats)

# stats['Backpack'] += ['FlintStone']
# print(stats)

#7,8
# skills = {
#     'Skill 1': [
#         {'Name': 'Tackle'},
#         {'Minimum level': 1}, 
#         {'Damage': 5},
#         {'Hit rate': 0.3}
#         ],
#     'Skill 2': [
#         {'Name': 'Quick Attack'}, 
#         {'Minimum level': 2}, 
#         {'Damage': 3}, 
#         {'Hit rate': 0.5}],
#     'Skill 3': [
#         {'Name': 'Strong Kick'}, 
#         {'Minimum level': 4}, 
#         {'Damage': 9}, 
#         {'Hit rate': 0.2}]
# }

# for i in skills.keys():
#     print(i, end = ': ')
#     print(skills[i][0]['Name'])

# import random
# t = random.randint(1, 2)
# d = random.randint(2, 10)
# n = input("Choose your skills (1 to 3): ")
# # Too lazy to use 'for'
# if n == "1":
#     print(f"You chose {skills['Skill 1'][0]['Name']}")
#     if t == 1:
#         print(f"Damage: {skills['Skill 1'][2]['Damage']}")
#     else:
#         print(f"Cannot deploy. Required level {t*d}")
# elif n == "2":
#     print(f"You chose {skills['Skill 2'][0]['Name']}")
#     if t == 1:
#         print(f"Damage: {skills['Skill 2'][2]['Damage']}")
#     else:
#         print(f"Cannot deploy. Required level {t*d}")
# elif n == "3":
#     print(f"You chose {skills['Skill 3'][0]['Name']}")
#     if t == 1:
#         print(f"Damage: {skills['Skill 3'][2]['Damage']}")
#     else:
#         print(f"Cannot deploy. Required level {t*d}")

# import random
# t = random.random()
# n = input("Choose your skills (1 to 3): ")
# # Too lazy to use 'for'
# if n == "1":
#     print(f"You chose {skills['Skill 1'][0]['Name']}")
#     if t > skills['Skill 1'][3]['Hit rate']:
#         print(f"Damage: {skills['Skill 1'][2]['Damage']}")
#     else:
#         print("Missed.")
# elif n == "2":
#     print(f"You chose {skills['Skill 2'][0]['Name']}")
#     if t > skills['Skill 2'][3]['Hit rate']:
#         print(f"Damage: {skills['Skill 2'][2]['Damage']}")
#     else:
#         print("Missed.")
# elif n == "3":
#     print(f"You chose {skills['Skill 3'][0]['Name']}")
#     if t > skills['Skill 3'][3]['Hit rate']:
#         print(f"Damage: {skills['Skill 3'][2]['Damage']}")
#     else:
#         print("Missed.")

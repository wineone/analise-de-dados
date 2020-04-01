from __future__ import division
from funcoes_cap_1 import *
from collections import defaultdict



users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendship = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
              (4,5),(5,6),(5,7),(6,8),(7,8),(8,9)
]

for user in users:
    user["friends"] = []

for i,j in friendship:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

total = sum([number_of_friends(user) for user in users])

media = total / len(users)

print("Os usuarios tem em media %.2f amigos"%media)

print("Amigos de amigos de %d : %s"%(0,friend_of_a_friend(users[0]).__str__()))

print("Amigos de amigos de %d: %s"%( 3,friend_of_a_friend_pro(users[3]) ) )


# salarios e experiencia

salaries_tenures = {
    (83000,8.7),(88000,8.1),
    (48000,0.7),(76000,6),
    (69000,6.5),(76000,7.5),
    (60000,2.5),(83000,10),
    (48000,1.9),(63000,4.2),
}

dici = defaultdict(list)

for sala, anos in salaries_tenures:
    dici[class_ternure(anos)].append(sala)


media_salario = {key: sum(lista) / len(lista) for key,lista in dici.items()}


print("a media de salario eh:", media_salario)



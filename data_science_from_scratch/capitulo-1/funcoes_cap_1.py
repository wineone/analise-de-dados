from collections import Counter

def printa():
    print("hello world")


def number_of_friends(user):
    return len(user["friends"])


def friend_of_a_friend(user):
    return [foaf["id"] for friend in user["friends"] for foaf in friend["friends"]]

def not_same(a,b):
    return a["id"] != b["id"]

def not_friend(a,b):
    return all([not_same(a,friend) for friend in b["friends"]])


def friend_of_a_friend_pro(user):
    return Counter([foaf["id"] for friend in user["friends"] for foaf in friend["friends"] if not_same(user,foaf) and not_friend(foaf,user)])

def class_ternure(ternure):
    if(ternure < 2):
        return "less_2"
    elif(ternure < 5):
        return "less_5"
    else:
        return "more_5"
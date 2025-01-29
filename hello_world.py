# message = "Hello Python Crash Course reader!"
# print(message)

# name = "ada lovelace"
# print(name.title())

# first_name = "ada"
# last_name = "lovelace"
# name=first_name + " " + last_name
# print(name)
# print("\tHello")
# #it's just a simple code
# age = 23
# message = "Happy " + str(age) + "rd Birthday!"
# print(message)

# fav_num = 32
# print("My favorite number is "+ str(fav_num))

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0])

# names = ['ada', 'belle', 'chris', 'david']
# print(names[0].title())
# print("My first best friend is "+ names[1].title())
# names.insert(1,'carol')
# print(names)
# names.append('elaine')
# print(names)
# names.extend(['fiona','gina'])
# print(names)
# names[2] = 'daniel'
# print(names)
# names[1:2] = ['belle','carol']
# print(names)
# names.remove('daniel')
# print(names)
# del names[1]
# print(names)
# names.pop()
# print(names)
# print(names.pop())
# print(names)
# print(names.pop(1))
# print(names)
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# for car in cars:
#     print(car)
# for value in range(1,5):
#     print(value)
# numbers = list(range(1,6))
# print(numbers)
# even_numbers = list(range(2,11,2))
# print(even_numbers)
# squares = []
# for value in range(1,11):
#     square = value**2
#     squares.append(square)
# print(squares)
# print(min(squares))
# print(max(squares))
# print(sum(squares))
# squares = [value**2  for value in range(1,11)]
# print(squares)
# numbers = [value for value in range(1,10000000)]
# print(sum(numbers))
# odd_numbers = [value**3 for value in range(1,10)]
# print(odd_numbers)
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[-3:])
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# friend_foods.append('cannoli')
# print(my_foods)
# print(friend_foods)
# my_foods = friend_foods
# print(my_foods)
# simple_foods = ('rice', 'beans', 'yam', 'plantain', 'egg')
# for food in simple_foods:
#     print(food)
# simple_foods = ('rice', 'bread', 'yogurt', 'plantain', 'egg')
# for food in simple_foods:
#     print(food)
age = 17
if age < 4:
    print("Your admission cost is $0.")
elif age >=4 and age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

alien_color = ["green", "yellow", "red"]
if "green" in alien_color:
    print("You just earned 5 points!")
if "yellow" in alien_color: 
    print("You just earned 10 points!")
if "red" in alien_color:
    print("You just earned 15 points!")

age = 65
if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a kid.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are an adult.")
elif age >= 65:
    print("You are an elder.")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in requested_toppings:
    if topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.') 
    else:
        print('adding ' + topping + ".")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
request_toppings = ['mushrooms', 'french fries', 'extra cheese']
for topping in request_toppings:
    if topping in available_toppings:
        print('Adding ' + topping + ".")
    else:
        print('Sorry, we don\'t have ' + topping + ".")

usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + username + ', thank you for logging in again.')
else:
    print('We need to find some users!')

current_users = ['admin', 'ada', 'belle', 'carol', 'daniel']
new_users = ['elaine', 'fiona', 'daniel', 'helen', 'Ada']
for new_user in new_users:
    if new_user in current_users:
        print('Sorry, the username ' + new_user + ' is already taken. Please choose another username.')
    else:
        print('The username ' + new_user + ' is available.')

numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(str(number)+"st")
    elif number ==2:
        print(str(number)+"nd")
    elif number ==3:
        print(str(number)+"rd")
    elif number <= 9:
        print(str(number)+"th")

alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['color'] = "yellow"
print(alien_0)

person_details = {
    'first_name':"Mounika",
    'last_name':"Marella",
    'age':27,
    'city':'Tampa',
}
print(person_details['first_name'])
print(person_details['last_name'])
print(person_details['age'])
print(person_details['city'])

friends = {
    'neha' : 6,
    'raha' : 7,
    'jyo' : 5,
    'vi' : 2,
    'ka' : 3,
}
for friend,no in sorted(friends.items()):
    print(friend,no)

users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    },
}
for user,name in users.items():
    print(user,name)
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
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
for car in cars:
    print(car)
for value in range(1,5):
    print(value)
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
squares = [value**2  for value in range(1,11)]
print(squares)
numbers = [value for value in range(1,10000000)]
print(sum(numbers))
odd_numbers = [value**3 for value in range(1,10)]
print(odd_numbers)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
friend_foods.append('cannoli')
print(my_foods)
print(friend_foods)
my_foods = friend_foods
print(my_foods)
simple_foods = ('rice', 'beans', 'yam', 'plantain', 'egg')
for food in simple_foods:
    print(food)
simple_foods = ('rice', 'bread', 'yogurt', 'plantain', 'egg')
for food in simple_foods:
    print(food)

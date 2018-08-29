# This is my first python program ;) :thinking: :LUL: :Poggers: :FeelsBadMan:
'''
print('hello python')
print('Nice to meet you')#This is also a comment for you

#name = raw_input('What is you name? ')
#print("Hi there, " + name)

#ask for user input, and print it 5 times

x= raw_input('Who are you?')
print((x+ " ")*5)

#hello = raw_input('Who are you?')
#print("What's good "+ hello +"?")

user_input = int(raw_input("Enter any number: "))
print("You entered: " + user_input)
print(type(user_input))

num_1 = int(raw_input("Type a number: "))
num_2 = int(raw_input("Type a number: "))
sum = num_1 + num_2
print("The sum is: " + str(sum))

my_name = "Edgar"
friend1 = "Rasx"
friend2 = "Caaseeeeeee"
friend3 = "Julioh"

print("My naem is %s. My friends are: %s,%s,%s." %
(my_name,friend1,friend2,friend3))

print("My name is %s." % my_name)

food = "Pizza"
drink = "Sprite"

print("Today I ate %s for lunch. I also drank %s." % (food, drink))

noun1 = "Cow"
adjective1 = "extravagant"
noun2 = "rock"
verb1 = "planking"

print("The %s jumped over an %s %s.  Then the %s decided to stop being so %s and take up a hobby: %s" % (noun1, adjective1,noun2,noun2,adjective1,verb1))

print("A %s loves to eat %s %s , but sometimes a %s is bad for a %s due to its %s abilities." % (noun1, adjective1, noun2, noun2, noun1, verb1))

num = int(raw_input("Enter a number: "))
if num > 0:
    print("That's a positive number.")
elif num < 0:
    print("That's a negative number.")
else:
    print("Zero is neither")
#loops
i = 1;
while i<= 5:
    print(i)
    i = i + 1
# i | i <= 5 | output
# 1 | 1 <= 5 | 1
# 2 | 2 <= 5 | 2
# 3 | 3 <= 5 | 3
# 4 | 4 <= 5 | 4
# 5 | 5 <= 5 | 5

for i in range(5):
    print i + 1
    
print ("For Loop Below")
for i in range(5):
    print i + 1
    
string = "hello there"
for letter in string:
    print(letter.upper())

for i in range(5,9):
    print(i)
'''

def greetAgent(lastName, firstName):
    return("%s. %s %s." % (lastName, firstName, lastName))
    
print(greetAgent("Licup", "Edgar"))
from random import randint
'''
#if elif else statements

num1 = raw_input("Type in your number: ")
num2 = raw_input("Type in your number: ")
sum = int(num1) + int(num2)
print "Sum : " + str(sum)

if sum > 0:
    print("Positive")
elif sum < 0:
    print("Negative")
else:
    print("Neither")


#Loops

for i in range(5):
    print(i)
    
string ="Hello there!"
for letter in string:
    print(letter)
    
while True:
    print "Strawberry Fields"

user_input = raw_input("Enter a word: ")
print_again = 'y'

while print_again  == 'y':
    print (user_input + " ") * 3
    print_again = raw_input('Again? y|n: ')

#functions

def greet_agent(first,last):
    print("First: " + first)
    print("Last: " + last)
    
greet_agent("Edgar","Licup")

def getName(name):
    return name

print(getName('Anita'))
#or my_name = getName('Anita')
#print my_name


item_one = raw_input("What's on your bucket list?")
item_two = raw_input("What's on your bucket list?")
item_three = raw_input("What's on your bucket list?")

#Lists

bucket_list = ["Travel the world","See a magician perform live", "Get a job"]
print("Your bucket list: %s, %s, and %s" % (bucket_list[0],bucket_list[1],bucket_list[2]))
print(bucket_list[1:2])

bucket_list[0] = "Sky dive"
print bucket_list

#List methods
list = range(5)
print "Your list: " + str(list)

list.append(5)
print "Your list: " + str(list)

list.insert(2,6)
print "Your list: " + str(list)

list.append(6)
print "Your list: " + str(list)

list.remove(6)
print "Your list: " + str(list)

del list[0]
print "Your list: " + str(list)

list.insert(3,7)
print "Your list: " + str(list)

list.sort
print "Your list: " + str(list)

list_two = range(8,16)
print(list_two) # [8,9,10,11,12,13,14,15]

list.extend(list_two)
print "Your list: " + str(list)

list.sort()
print "Your list: " + str(list)

print (len(list))

list.append(20)
print "Your list: " + str(list)

list.insert(0,0)
print "Your list: " + str(list)

list.insert(6,16)
print "Your list: " + str(list)

list.sort
print "Your list: " + str(list)


siblings = ["Jeffrey", "Marynette"]
for sibling in siblings:
    print sibling + " Licup"
    
print "Siblings: " + str(siblings)
#siblings[0] = siblings[0] = " Licup"
#print "Siblings: " + str(siblings)

for i in range(len(siblings)):
    if i == 0:
        print siblings[i]
    else:
        siblings[i] = siblings[i] + " Licup"
        print siblings[i]

print "(outside of for loop)Sibligs: " + str(siblings)

name = "Chanel"
if name in siblings:
    print "Found"
else:
    print "Not Found"

numbers = [randint(1,100) for x in range(10)]

bad_number = raw_input("Which number would you like to remove? ")

numbers.remove(bad_number)

if bad_number in numbers:
    numbers.remove(bad_number)
else:
    print("That number is not in our list")

def crystal_ball():
    #This is in the function body
    raw_input("Ask a question: ")
    choices = ["Yes", "No", "Keep dreaming", "Eh, maybe?", 
                "Totally not, dude", "ask again later"]
    r_inx = randint(0,len(choices) - 1)
    return(choices[r_inx])
print(crystal_ball())
#(not indented) is not part of the function body

edgar_list =[]
#jennifer_list = []

def populate_bucket_list(list):
    
    answer = 'y'
    while(answer == 'y'):
        item = raw_input("Add something to your bucket_list: ")
        #TODO: append user input to the list that is passed in
        list.append(item)
        #TODO: Show list
        print "Your list so far: " + str(list)
        #TODO: Ask user if they would like to add something else
        answer = raw_input("Would you like to add more?(y/n): ")
        #TODO: If they say yes, keeping asking and adding to the list
        
            
populate_bucket_list(edgar_list)
#populate_bucket_list(jennifer_list)

#dictionaries

states_list = ["New York", "New Jersey", "Connecticut"]
states_dict = {
    "NY":"New York",
    "NJ":"New Jersey", 
    "CT":"Connecticut"
    
}

states_dict["CA"] = "California"
print states_dict

#key = "CA"
#print states_dict[key] # This will print "California"

for key in states_dict:
    print key + "." + states_dict[key]


pet = {
    "name": "Doggo",
    "animal": "dog",
    "age": 5,
    "friends":["charlie","capitan","luna","pancho"]
}

#dict_name[key]
print(pet["name"])
print(type(pet["friends"]))

#dict_name[key] = new value
pet["age"] = pet["age"] + 1
print("Happy bday! you are now " + str(pet["age"]))

#to change list names

pet["name"] = "babbage"
pet["animal"] = "fish"
pet["age"] = pet["age"] - 2
pet["friends"] = ["ada","bubbles"]
'''
pet = {
  "name": "babbage",
  "animal": "fish",
  "age": 3,
  "friends": ["ada","bubbles"]
}

if len(pet["friends"]) > 0:
    print pet["friends"][1]
else:
    print(pet["name"] + " has no friends ;(")

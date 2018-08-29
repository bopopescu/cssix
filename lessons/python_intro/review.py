'''
# Declare some lists
list_one = [1,2,3]
list_two = range(4) #[0,1,2,3]
list_three = []

print(type(list_two))

print(range(5,10)) #[5,6,7,8,9] 5 shows up but 10 doesn't (10 is excluded from the range)

print(range(len(list_one))) #[0,1,2] len(list_one) = 3 => range(3) = [0,1,2]

#Append to the end of a list
list_one.append(6)
list_two.append(6)
list_three.append(6)
print("**APPEND**")
print(list_one)
print(list_two)
print(list_three)
#Insert 0 to index 0
list_one.insert(0,0) #In parenthesis ("index","value")
list_two.insert(0,0)
list_three.insert(0,0)
print("**INSERT NO.1**")
print(list_one)
print(list_two)
print(list_three)
list_one.insert(0,2) #In parenthesis ("index","value")
list_two.insert(0,2)
list_three.insert(0,2)
print("**INSERT NO.2**")#Inserting another value in the same index just moves the original up one spot
print(list_one)
print(list_two)
print(list_three)
#Access the list
x = list_one[len(list_one) - 1] # value of list_one at 1
#print (list_three[x]) # list_two[x] = 2, list_one[1] = 0 => list_two[0] = 2

# %
x = 10
print(x % 2 != 0) # % divides the numbers and returns the remainder ex. 10/3 = 3.33 but % returns 33

#Function
#If the number is odd print "odd"
#If the number is even print "even"
def isOddOrEven(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
        
isOddOrEven(x)

#For each(iterate by element)
for i in range(3,10): #[3,4,5,6,7,8,9] but line breaks w/ each number
    print i 
#For each (iterate list by inx)
list = [99,98,97,96]
for i in range(len(list)):
    list[i] = (list[i] + 1)
    
print(list) #[100,99,9,97]

#Dictionary
# Declare a dictionary

empty = {}
event = {'name':'CSSIx Final Party',
         'date':'August 10th, 2018',
         'cost':'0.0',
         'attendees': ["Joey","Lexi"]
}

# Access a value
#name[key]
print "Cost: " + str(event['cost'])

#Re-assign cost to 10.0
event['cost'] = '10.0'
print event['cost']

# For each 
for key in event:
    print str(key) + ": " + str(event[key])
#search for a key in dict
if 'swag' in event:
    print event['swag']
else:
    print "There is no 'swag key'"
#add key to dict
event['swag'] = ["Water bottles", "Blankets", "Pillows"]
print event['swag']
'''
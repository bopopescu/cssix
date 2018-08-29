import random
person = {
    "name":"Anita",
    "friends":["Heather","Cassee","Evelyn"],
    "img_info":{
                'small':{
                    "url":"https:img",
                    "height":"50",
                    "width":"50"
                },
                'med':{
                    "url":"https:img",
                    "height":"100",
                    "width":"100"
                },
                'large':{
                    "url":"https://img",
                    "height":"200",
                    "width":"200"
                }
                }
}


#Access Values
#list = [4.5.6] list[0]
print person['name']
print person['friends']
print person['friends'][0]

group =[ 
    {
    "name":"Anita",
    "friends":["Heather","Cassee","Evelyn"]
    },
    {
    "name":"Anita2",
    "friends":["Heather2","Cassee2","Evelyn2"]
    }]

group = [person,person]
print type(group)
print group[0]
print group[0]['name']
print group[0]['friends'][1] #[list , key , index]

other_friends = ['person one','person two', 'person three']

print "Org. :" + str(other_friends)
random.shuffle(other_friends)
print "Shuffle :" + str(other_friends)

my_friends = person['friends']
my_friends.extend(other_friends)
print my_friends

random.shuffle(other_friends)
print "Shuffle :" + str(my_friends)
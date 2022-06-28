# This Python file uses the following encoding: utf-8
#create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida':'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '-'*10
print "NY State has:", cities['NY']
print "OR State has:", cities['OR']

#print some states
print '-'*10
print "Michigan's abbreviation is:", states['Michigan']
print "Florida's abbreviation is:", states['Florida']

#do it by using the state then city dict
print '-'*10
print "Michigan has:", cities[states['Michigan']]
print "Florida has:", cities[states['Florida']]

#print every state abbreviation
print '-'*10
for state, abbrev in states.items():   #用法：dict.items(),state用来保存冒号前面的；abbrev为冒号后面的！！！
    print "%s is abbreviated %s" % (state,abbrev)
    
#print every city in states
print '-'*10
for abbrev, city in cities.items():
    print "%s has the city %s" %(abbrev, city)

#now do both at the same time
print '-'*10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-'*10
#safely get a abbreviation by state that might not be there
state = states.get('Texas', None)# get(key，设置值)方法在 key（键）不在字典中时，可以返回默认值 None；返回的默认值可以自行设置来代替“None”的位置


if not state:
    print "Sorry, no Taxas."

#get a city with a default value
TX = cities.get('TX', 'Does not Exist')
print "The city for the state 'TX' is: %s" % TX
    






'''
Find all of the numbers from 1-1000 that are divisible by 7
'''
div7= [ i for i in range(1,1000) if i % 7 == 0]

'''
Find all of the numbers from 1-1000 that have a 3 in them
'''


have3= [n for n in range (1,1000) if '3' in str(n) ]


'''
Count the number of spaces in a string
'''

spaces= len([ s for s in 'hola como va' if s.isspace() ])


'''
Create a list of all the consonants in the string 
“Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
'''
string='Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'

all_consontants=[s for s in string if s not in 'aeiou ']


'''
Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’).
Result would look like (index, value), (index, value)
'''

List=['hi', 4, 8.99, 'apple', ('t,b','n')]

#1
index_value={key:[List[key]] for key in range(len(List))}

#2
result = [(index, item) for index, item in enumerate(List)]

#3
result2=[n for n in enumerate(List)]

'''
Find the common numbers in two lists (without using a tuple or set)
list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
'''

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

comon_numbers=[i for i in list_a if list_b.__contains__(i)] 

# other
common = [a for a in list_a if a in list_b]


'''
Get only the numbers in a sentence like
 ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
'''
string='In 1984 there were 13 instances of a protest with over 1000 people attending'

only_numbers= [n for n in string if n in '0123456789']


'''
Given numbers = range(20), produce a list containing the word ‘even’ 
if a number in the numbers is even,
 and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
'''

is_even=['odd' if n % 2 != 0 or n == 0  else 'even' for n in range(20)]

'''
Produce a list of tuples consisting of only the matching numbers in these lists 
list_a = 1, 2, 3,4,5,6,7,8,9 
list_b = 2, 7, 1, 12. 
Result would look like (4,4), (12,12)
'''
list_a = [1,2,3,4,5,6,7,8,9]
list_b = [2,7,1,12]

match=[(a,a) for a in list_a if a in list_b]


'''
Find all of the words in a string that are less than 4 letters

'''
string='Find all of the words in a string that are less than 4 letters'
four_letters=[word for word in string.split() if len(word)< 4]


'''
Use a nested list comprehension to find 
all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
'''

is_div=[i for i in range(1,1000) if any(i % digit == 0 for digit in range(2,10))]

print(is_div)

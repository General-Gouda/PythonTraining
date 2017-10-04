# Tuples are basically immutable lists and are surrounded by ()
months = ('January','February','March','April','May','June','July','August','September','October','November','December')

# Lists are mutable and are surrounded by []

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

# Dictionaries are key/value sorted. Not logically arranged so you cannot use dictionaryName[0] to call the first value. You have to use dictionary['key']

ages = {}

#Add a couple of names to the dictionary
ages['Sue'] = 23
ages['Peter'] = 19
ages['Andrew'] = 78
ages['Karren'] = 45

#Use the function has_key() - 
#This function takes this form:
#function_name.has_key(key-name)
#It returns TRUE
#if the dictionary has key-name in it
#but returns FALSE if it doesn't.
#Remember - this is how 'if' statements work -
#they run if something is true
#and they don't when something is false.
if 'Sue' in ages:
    print("Sue is in the dictionary. She is", \
ages['Sue'], "years old")

else:
    print("Sue is not in the dictionary")

#Use the function keys() - 
#This function returns a list
#of all the names of the keys.
#E.g.
print("The following people are in the dictionary:")
print(ages.keys())

#You could use this function to
#put all the key names in a list:
keys = ages.keys()

#You can also get a list
#of all the values in a dictionary.
#You use the values() function:
print("People are aged the following:", \
ages.values())

#Put it in a list:
values = ages.values()

#You can sort lists, with the sorted() function
#It will sort all values in a list
#alphabetically, numerically, etc...
#You can't sort dictionaries - 
#they are in no particular order
print(keys)
print(sorted(keys))

print(values)
print(sorted(values))

#You can find the number of entries
#with the len() function:
print("The dictionary has", \
len(ages), "entries in it")

fruits = ['apple', 'banana', 'kiwi', 'grape', 'coconut']
car = ['tesla', 'bmw', 'ford', 'subaru']
years = [1999, 2001, 2003, 2007, 2008, 2009, 2020, 2002, 2024]
names = ['fin', 'joe', 'john', 'steve', 'riley', 'reallylongnameicantthinkof', 'tn', 'g', 'normale']
dictionaries = [{'dinner': 'pasta', 'time': 19}, {'breakfast': 'eggs', 'time': 5}, {'lunch': 'sandwitch', 'time': 12}]

fruits.sort()
print(fruits)

years.sort()
print(years)
years.sort(reverse=True)
print(years)

car.sort(reverse=True)
print(car)

# function based on name
def sort_function(item):
    return len(item)

names.sort(key = sort_function, reverse=True)
print(names)

def sort_dictionaries(item):
    return item['time']

dictionaries.sort(key=sort_dictionaries, reverse=True)
print(dictionaries)
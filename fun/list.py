x=["a","c","d"]
# list operations
a=["1","2","3","4"]
# concatenation 
y=["a"+ ""+"b"]
# repetition
y=[i*2 for i in y]
dir(x)
fruits=["apple","mango","lemon","banana"]
# append adds a new value to the bottom of the list
fruits.append("pineapple")
# extend     extend the existing lists by appending all the items from the iterable.
fruits.extend(["orange","grape"])
# insert insert an item at a given position
fruits.insert(1,"avocado")
# remove removes the first item from the list
fruits.remove("apple")
print (fruits)
# pop() remove and returns the last element at a given position if no index is specified
fruits.pop(1)
print(fruits)
# sorts sorts the value in decending order
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
# count the number of times an element appears in the list
fruits.count("grape")
print(fruits)
fruits.copy()
print(fruits)
fruits.index("banana")
print(fruits.index("banana"))
print(fruits.clear())

# list comprehension
# using for loop
# Use a for loop to print the remainder of each number after division by 7.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x=[i/7 for i in x]
print(x)

a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a=[i%10 for i in a]
print(a)
a=[i/10 for i in a]
print(a)
a=[i+10 for i in x]
print(x)
b=[1,2,3,4,5,6]
b=[i+5 for i in a]
print(b)
y=[10, 20, 30, 40, 50, 60, 70, 80, 90]
print(y.count(10))
print(len(y))
# Write a function that takes a list of numbers as input and returns a new list with all duplicate numbers removed.
num=[2,1,5,1,6,2]
def numbers (num):
   return list(set(num)) 
print (numbers(num))
# Write a function that takes two numbers as input and returns their sum.
first=12
sec=13 
def sum_of(first,sec):
    return (first +sec)
print(sum_of(first,sec))

# Write a function that takes a string as input and returns the length of the string.
string="eating"
# def food(string):
#     return string(len(string))
# print(food(string))


student=list()
print(type(student))
people=["Mary","Boy","Girl","Doctor","Nurse"]
print(len(people)) 
print(people[0])
middle=(len(people)-1)//2
print(people[middle])
print(people[-1])
mixed_data_types=["clarine",20,6.4,"married",234]
print(mixed_data_types)
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0]) 
it_companies.append("JamboPay")
print(it_companies)
middle=(len(it_companies)-1)//2
print([middle])
it_companies.insert(3,"Spenn")
print(it_companies)
company = '#'.join(it_companies)
print(company)
print(it_companies[0].upper())
it_companies.reverse() 
print(it_companies)
print(it_companies[0:3]) 



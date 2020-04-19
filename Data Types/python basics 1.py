#**************************************************************************************************************
# Integers and floats
# Variable
# String
# List
# Tuples
# dictionary
# sets
#*****************************************************************************************************************

print(2+3)
print(type(2+3))                        # type int or float 

print(2-3)
print(type(2-3))

print(2*3)
print(type(2*3))        

print(2/3)                          # dividng two numbers (2/3) output is 0.6666666666666666
print(type(2/3))
                                    # if we see above line dividing two integer number gives float output

                                    # if two integer input are get divided and we need output in integer form 

print(2//3)                         # dividng two numbers (2//3) output is 0
print(type(2//3))

print(2%3)                        

#*******************************************************************************************************************
#Few commands

print(round(3.3))                    # round figure only integeral value
print(round(3.5))
print(round(3.332444,3))             # how many digits u need after decimal
print(complex(344))                  # ouput (344+0j)
print(complex(42567,62472))

#*********************************************************************************************************************
# Operator precedence

print(10-1*2)
print((5-3)+2**2)
print(3*2/2)
# ()
# **
# * /
# + -
#**********************************************************************************************************************
#binary
print(bin(5))
print(int("0b101",2))

#********************************************************************************************************************
#variable

num = 4
result = num/2
print(result)

a,b,c = 1,2,3
print(a,b,c)

#**********************************************************************************************************************

#str (string)
print(type("Hi i'm lokesh")) 
print("Hi i'm lokesh") 
print('hi I\'m lokesh')
print('hi I\'m \"lokesh"')

#*********************************************************************************************************************
#string concatenation (combining two strings)

a = "hi"
b = "frds"
c = a + "\t" + b
print(c)

#*********************************************************************************************************************
#Formatted string or f string

a = "hi"
b = 55

print(f" {a} {b} number")

#**********************************************************************************************************************

#string index (sring slicing)

# [start : stop : sepover]

name = "para lokesh"
print(name[1])
print(name[1:5])
print(name[0:-1])
print(name[0:-1:2])
print(name[3::-1])
print(name[:0:-1])
print(name[::-1])


#*********************************************************************************************************************

#immutability

"""

   immutability means we can't change 
   
   strings are immutable
   
   

a = "hi bro"
a[0] = "H"
print(a) # You get error as "TypeError: 'str' object does not support item assignment"
"""

#*******************************************************************************************************************


#Length  and few method

Greet = "hello loki"
print(len(Greet))
print(Greet[0:len(Greet)])

print(Greet.capitalize())
print(Greet.count("l"))
print(Greet.replace("hello", "hi"))
print(Greet.casefold())

#********************************************************************************************************************

#Type conversion
 
name = input("Enter the nmae :")
born_year = int(input("enter the year u born : "))
present_year = int(input("enter present year : "))
age = present_year - born_year
print(f"hi {name} ur age is {age}")


#******************************************************************************************************************

#list

"""

      List is a collection of items
      Lists are mutable
      List are form of array (it is not completely right)
      List is a bag in a bag u can have phone , books , pens , laptops etc...
      same way list also contains strings , numbers , boolean values , integers , floats
      
"""    

bag = ["books" , "pens" , "phone" , 345 , 56.78 , True] 
print(bag[3])     

#*********************************************************************************************************************
 
# list slicing
 
print(bag[0::2])
#******************************************************************************************************************
# mutable

bag[0] = "laptop"
print(bag)


#**********************************************************************************************************************


#Matrix
matrix = [
    [1,0,1],
    [1,0,1],
    [1,0,1]]
print(matrix)
print(matrix[0][2])

#********************************************************************************************************************

#list methods

bag = ["laptop" , "pen" , "book" , "phone" , 1 , 2 , 3]

bag.append("bottle")
print(bag)
bag.insert(1, "earphone")
print(bag)
bag.extend([100,101])
print(bag)
 
bag = [1,3,5,723,2458,31,67]
bag.sort()
bag.reverse()
print(bag)


empty_string = " ! "
new_string = empty_string.join(["hi", "dajdh"])
print(new_string)

new_string = " ".join(["hi", "dajdh"])
print(new_string)

#********************************************************************************************************************

# list unpacking

a , b , c , *other , d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(other)
print(d)

#*********************************************************************************************************************

# dictinory
"""

   dictinory is unsorted 
   dictinory key are immutable
"""

dictionary ={ 
    "a" : [1,2,3],
    "b" : "qewfr",
    "c" : False}
print(dictionary)

lists = [
    {
     "a": [1,2,3],
     "b": "efsg",
     "c": True
     },
    
    {
     "a":[4,5,6],
     "b":"rgfhh"
     }]
print(lists[0]["a"][2])


dictionary ={ 
    "a" : [1,2,3],
    "b" : "qewfr",
    True : False}
print(dictionary)
print(dictionary.get("age"))
print(dictionary.get("age",300))
print("a" in dictionary.keys())
print(dictionary.items())

user = dict(name = [1,2,3,4] , lab = True)
print(user)

#******************************************************************************************************************

#tuple

my_tuple = (1,2,3,)
print(my_tuple[1:2])

#***************************************************************************************************************

#sets

my_set = {1,2,3,4,5}
ur_set = {4,5,6,7,8,9,10}
print(my_set)
print(my_set.difference(ur_set))
print(my_set.discard(5))
print(my_set)
print(my_set.difference_update(ur_set))
print(my_set)
print(my_set.intersection(ur_set))
print(my_set & ur_set)
print(my_set.isdisjoint(ur_set))
print(my_set.union(ur_set))
print(my_set | ur_set)
print(my_set.issubset(ur_set))
print(my_set.issuperset(ur_set))

#****************************************************************************************************************




















































































#Data Types

#Numeric - Includes int, float and complex
#String
#List
#Tuple
#Dictionary

######################################## List ########################################
#1 List is Mutable, as we can update data
values = [1, 2, "dheeraj", 4, 5]

print("######################################## List ########################################")
print("Values : ", values)
print(type(values))
print(values[0]) #Value at index 0

print(values[-1]) #Value at last index , prints 5
print(values[1:3]) #Print values from index 1 to 3, prints [2, 'dheeraj']

#Insert new value in the list
values.insert(3, "g1")
print("Updated values: ", values)

#Append value in the list at end
values.append("last value")
print("Updated values 2: ", values)

#Update value in the list
values[3] = "gangalakurthi"

#Delete value in the list
del values[0]

print("Updated values: ", values)

######################################## Tuple ########################################
#1 Tuple is immutable and cannot be updated once declared

print("######################################## Tuple ########################################")
tupleValues = (1, 2, "dheeraj", 3.4)
print(tupleValues)

print(tupleValues[2])

######################################## Dictionary ########################################
#1 Key value pair data type

dic = {1: "firstName", 2:"lastName", "age":33}
print("######################################## Dictionary ########################################")
print(dic)
print(dic[1])
print(dic[2])
print(dic["age"])
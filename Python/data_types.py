#We will learn Data Types in python 
''' 1)Numbers
    2)String
    3)List
    4)Tuple
    5)Dictionary '''


# Before starting data types we can get any data type just by

number = 0x4215F
print(type(number))

# 1)Numbers

#Integers
num1 = 33
print("This is integer",num1)

#Float
num2 = 44.5
print("This is float",num2)

#long
num3 = 55444555655526465 #This represents long number
num4 = 0x421F5 #This represents Hexa-decimal number

print("Example of long number",num3)
print("Example of long number containing hexa-decimal number",num4)


# 2)String
str = "Hello my name is Ashokraj Dhole"

#Various functions can be performed on the string
print(str) #print whole string
print(str[0]) #Print index of the string denoted
print(str[2:9]) #This will print charecter from indexed number 2 to 9
print(str[8:]) #This will print the charecters from index number onwards
print(str*3) #This is repetation of string 
print(str[-1]) #print string index number from backward

# 3)List
#Array and List are same but List is dynamic
list1 = ["Government Polytechnic Achalpur",25 ,"Ashmit Narkhede",85 ,"Chakradhar Chokhande", 95]
list2 = [145, "Vishal Padol"]

#same operations can be performed as string
print(list1)
print(list1+list2)
print(list1[0])
print(list1[1:3])
print(list1[3:])
print(list2*2)
print(list1[-1])

# 4)Tuple
tup1 = (45,20,3,145,"Ravi",89 ,"Teja")
tup2 = (55, "Hello")
print(tup1)  #Prints complete tuple
print(tup1[0])  #Prints first element of list
print(tup1*2)   #prints tup1 2times
print(tup1+tup2) #conctent both tuple


# 5)Dictionary
#   In dictonary we can give custom index number to our values

dict1 = {"Ashokraj" : "9689222156","Baba" : "9822183406",  "Nana" : "9850417446", "Aai" : "7387297506" } 

print(dict1) #Prints everything
print(dict1.keys()) #prints every key from the above list
print(dict1.values())   #prints every value from the above list

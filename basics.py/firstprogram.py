# name = "ANUSHKA SINGH"
# age =20
# print("My name is:",name)
# print("my age is:",age)

# name = "Anushka singh"
# age = 51;
# print("MY name is:",name)
# print("my age is:",age)
# print("Anushka is a genius")

# name =input("what is your name?\n")
# print(name)

# secret = input("tony tell me your superhero name:")
# print(secret)


##############################
#type conversion

# old_age=input("enter your old age:")
# new_age=int(old_age)+2 #int is used to change the old_age string into integer
# print(new_age)

# number = 18
# print(float(number))
# float()
# str()
# bool()


# first = int(input ("enter first number:"))
# second = int(input("enter second number:"))
# sum=first+second;
# print(sum)

# name = "tony stark"
# print (name.upper())
# print(name.lower())
# print(name.find('S'))
# print(name.replace("tony stark","ironman"))

# name="Tony Stark"
# print('T' in name)
# print('m' in name)

# print(3>2 or 5>9)
# print(3>2 and 5>9)
# print(not 3>2)

# age=int(input("enter your age:"))
# if(age>=18):
#     print("you are an adult")
#     print("you can vote")
# elif(age<18 and age>3):
#     print("you are in school")
# else:
#     print("you are a child")

################CALCULATOR########

# first = int(input("Enter first number:"))
# operator= input("enter operator(+,-,*,/,%): ")
# second=int(input("enter second number:"))

# if operator == "+":
#     print(first + second)
# elif operator == "-":
#     print(first - second)
# elif operator == "*":
#     print(first * second)
# elif operator == "/":
#     print(first / second)
# elif operator == "%":
#     print(first % second)
# else:
#     print("invalid operation")

###########range###########
# for i in range(8):
#     print(i)

##############list#########

# marks = [95,78,90]
# print("maths marks",marks[-3])
# print(marks[0:3])


#############loop in list############
# marks =[98,58,78]
# marks.append(99)  #add element at last inedex
# marks.insert(3,56) #add element at any index
# print(88 in marks)
# print(len(marks))#length of list
# print(marks)

#tuple is immutable means we can not change it like list,set and dictionaries
#list is mutable and we can change it by ussing append insert,

#tuple
#square bracket hota h tab ota h list
#parenthesis hota h tab hota h tuple
#curly bracket hota h tab hota h set
#set are known as unorderd because they can not contain index

########set##########3
# marks={95,78,98,97,97}
# print(marks)

#dictionaryyyy
#key and value pair 

marks={"english":95,"chemistry":98,"maths":78}

print(marks["chemistry"])
marks["physics"]=97
print(marks)
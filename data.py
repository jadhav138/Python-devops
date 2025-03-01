#list collection of multiple data types, enclosed in square brackets
first_list = [122333, "devops", 'm', 'str1', 'num1' ]

print(first_list)

#tuple ( WE CAN EDIT LIST BUT NOT TUPLE . FOR TUPLE WE HAVE TO REWRITE)
first_tuple = (122333, "devops", 'm', )

print(first_tuple)


print("variable first_list is a:", type(first_list))
print("variable first_tuple is a:", type(first_tuple))


#DICTONARY it has the curly bracket and comes with pair (key: value)



#different ways to print

name = "kashappa omkar jadhav"
gender = "male"

print("my name is ", name)
print("my name is  {} " .format(name) )
print("{} is my name" .format(name))
print("my name is {} and my gender is {}".format(name , gender))

print(f"my name is {name} and my gender is {gender} ")



#concatination
print("my self " + " " + name + " " + " my gender is" +  " " +gender)






##scicling


name="kashappa omkar jadhav"

print(name)
print(name[1])
print(name[15])
print(name[10])


print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])


print(name[1:4])
print(name[0:25])
print(name[ 0:3 ])
print(name[14: 21])


#scling further (includes the gap for further slicing)
#() tuple , list [], dictionary {}

my_interest = ("aws", "Azure" , "GCP", "devop" , "data analyst", "Web Developer")

print(my_interest[0])
print(my_interest[-3])

print(my_interest[1:5])
print(my_interest[2:5])
print(my_interest[-4:-1])
print(my_interest[1:5])
print(my_interest[1:5][3])
print(my_interest[1:5][3][0:6])
print(my_interest[1])


#dctornary

skills = { "devops": ("aws", "Azure" , "GCP", "devop"), "development_skills":["pyhton","yaml","json","node.js"]}

print(skills)

print(skills["devops"][0:4][2][-1])




#different types of operators in python

#arthimatic varables

x = 10
y = 5

total = x + y
minus = x - y
multi = x * y
div = y/x
power = y**x
print(total)
print(minus)
print(multi)
print(div)
print(power)



#comarison operator

a = 30
b = 34

out = (a > b)
print(out)

out = (a < b)
print(out)

out = (a != b )
print(out)

out = (a == b)
print(out)


#assignment operators

c = 2
d = 11

#c+=d # c = c+d
c-=d
print(c)


#logical operator

# and
# or
a = 60
b = 67

x = 2
y = 4

out = (a > b) or (x < y)
print(out)
out = (a < b) or (x < y)
print(out)
out = (a < b) or (x < y)
print(out)
# both case has to be true to return true
out = (a < b) and (x < y)
print(out)
out = not(a < b) and (x < y)
print(out)



#membership operator

first_tuple = ("str1", "devops", 47, "7,6,6,")
find = "devops" in first_tuple

print(find)

ans = 67 in first_tuple
print(ans)

ans = 67 not in first_tuple
print(ans)


# identity operator
a = 15
b = 67


result = a is  b
print(result)

result = a is not b
print(result)


#if/else/elif condition

z = 80

if z < 80:
    print("z is less than 80")
elif z ==80:
    print("z is eaqual to 80")
else:
    print("if z is greater than 80")



##loops for/while (use for repetative task)

# for loop ends after an event , while loops end when an condition become false
"""
planet = "earth"
for i in planet:
    print(i)

print("rest in code")
"""
"""

skills = { "devops": ("aws", "Azure" , "GCP", "devop"), "development_skills":["pyhton","yaml","json","node.js"]}

if skill in skills:
    print(f"I have this talent {skills}")
"""

'''
k = 0
while k <=10:
    print("value is not equal to 10 or greater")
    print("looping")
    k= k+1

    print("iam greater than 10 ")
'''


'''
import time
x = 45
while True:
    print("value of x is: " , x )
    print("still calculating")
    x*=2
    time.sleep(1)
'''




'''
# break statements

for  i in "devops":
    print(i)
    if i== "o":
        print("i have found what am i looking for")
        break
    print("out of loops")
'''
#continue
for i in "devops":
        print(i)
        if i == "0":
            print("Found MY digit hurry!")
            continue
            print(f"value of i is : {i}")
        print("out of loops")
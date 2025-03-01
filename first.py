
"""
multi line alinment
which helps in line multiple lines code

"""
"""
# varibles exmaples
var1= "python"
var2= "12334"


## dir() function
message = "this is kashappa omkar jadhav"

print(dir(message))

print(message.upper())
print(message.lower())
print(message.isalpha())
print(message.isnumeric())
print(message.find("omkar"))
print(message[15:20])
print(message.find("zero"))  #returns -1 because it not able to find zero in the message variable





ip = ("123","656", "765" , "78")

print("." .join(ip))
print("/" .join(ip))
print("'" .join(ip))


places = ( "thailand", "singapoor", "paris", "berlin" , "swizerland")
print(places)

places.append(["japan"])
print(places)

places.extend(["us", "uk"])
print(places)




# creating our own function
def add(arg1 , arg2):
    total= arg1 +arg2
    return total

out = add(2 , 3)
print(out)


def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)

adder(50,50)
print(adder(50,69))




def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x

 out = summ([7,8,8])
print(out)




#defalut argument


def greetings(MSG="Morning"):
    print(f" good {MSG}")
    print("welcome to this function")

greetings()
greetings( MSG="Evening")


def vac_feedback(vac, efficacy):
    print(f"{vac} vaccine is having {efficacy} % efficacy.")
    if (efficacy > 50) and (efficacy <= 78):
        print("this is consider safe")
    elif (efficacy > 50) and (efficacy <=90):
        print("we can give it a shot")
    elif(efficacy >=90):
        print("atleast we can try ")
    else:
        print("no need to try this vaccine")

vac_feedback("aster" , 98)
vac_feedback("sputink", 55)
vac_feedback(efficacy=90,vac="known")



#function can take any number of argumenets

def order_food(min_order, *args):
    print(f"you have order: {min_order}")
    #print(args)
    for item in args:
        print(f"you have ordered: {item}")
    print("your food will be delivered in 30 mins:")
    print("enjoy your food")

order_food("vegen" ," chicken ","lettuce ", "chipoltae" )





import random


def time_activity(*args , **kwargs):
  #print(args)
  #print(kwargs)

  min = sum(args) + random.randint(0,60)
  print(min)
  choice = random.choice(list(kwargs.keys()))
  print(choice)
  print(f"you have to spend {min} for {kwargs[choice]}.")

time_activity(10,20,30, hobby="dance", sport="running", fun="tv", work="backend programmer")


import random

def free_time(*args , **kwargs):
    print(args)
    print(kwargs)

    day_time = sum(args) +random.randint(0 , 8)
    print(day_time)
    activity = random.choice(list(kwargs.values()))
    print(activity)


free_time(2,3, morning="yoga", afternoon="playing sports",evening="indoor sports", night="playstation")
"""





##module like random  we can create our own modeule



import random


def vac_feedback(vac, efficacy):
    print(f"{vac} vaccine is having {efficacy} % efficacy.")
    if (efficacy > 50) and (efficacy <= 78):
        print("this is consider safe")
    elif (efficacy > 50) and (efficacy <=90):
        print("we can give it a shot")
    elif(efficacy >=90):
        print("atleast we can try ")
    else:
        print("no need to try this vaccine")


def time_activity(*args , **kwargs):
  #print(args)
  #print(kwargs)

  min = sum(args) + random.randint(0,60)
  print(min)
  choice = random.choice(list(kwargs.keys()))
  print(choice)
  print(f"you have to spend {min} for {kwargs[choice]}.")

time_activity(10,20,30, hobby="dance", sport="running", fun="tv", work="backend programmer")



def order_food(min_order, *args):
    print(f"you have order: {min_order}")
    #print(args)
    for item in args:
        print(f"you have ordered: {item}")
    print("your food will be delivered in 30 mins:")
    print("enjoy your food")

order_food("vegen" ," chicken ","lettuce ", "chipoltae" )



import random

def free_time(*args , **kwargs):
    print(args)
    print(kwargs)

    day_time = sum(args) +random.randint(0 , 8)
    print(day_time)
    activity = random.choice(list(kwargs.values()))
    print(activity)


free_time(2,3, morning="yoga", afternoon="playing sports",evening="indoor sports", night="playstation")

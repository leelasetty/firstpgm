"""
foods = ['puri','sagu','chicken','dosa','chapathi']

for f in foods :
    print (f)
    print("length of " + f + "is " + str(len(f)))

    # travers partially
for f in foods[1:3]:
    print("value of f " + f )
 """

"""
# loop for certain iteration
for x in range(2,10,2):
    print(x)
    print("learn python")

s1 = 5
while s1 < 10 :
    print ("s1 is " + str(s1))
    s1 +=1
"""

# string concatination
#print("this is " + "concatination")

magicnumber = 26
for i in range(100):
    j = i/2
    if j == 0:
        print ("i is even with value = " + str(i))

#keyword NOT IT
txt = "The best things in life are free "
if "expensive" in txt:
    print("yes, 'expensive' is present. ")
else:
    print("expensive" not in txt)

age = 10
if age < 21:
    print("No beer for you")

"""
ages = "101"
if ages is "10":
    print("OHH age is a string")
elif ages is "12":
    print (" its a number 12")
elif ages is "23":
    print ("the number is 23")
else:
    print("None of the option true")
"""
# continue and break

numbertaken = [2,3,16,13,18]

for n in range(0,20):
    if n in numbertaken:
        continue
    print(n)

def function1():
    print("I am in the function1")
    return "hello"

print("the value from function1 " + function1())
r = function1()

def bitcoin_to_usd(btc):
    amount_usd = btc*527
    print(amount_usd)

bitcoin_to_usd(12)
bitcoin_to_usd(3.4)

def defaultargument(var="unknown"):
    if var is 'red':
        var = 'red_yes'
    elif var is 'blue':
        var = 'blue_yes'
        print("value is " + var)

defaultargument()
defaultargument('red')
defaultargument('blue')













    






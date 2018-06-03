# (0) Shebang
# Execute using Python by looking up the path to the Python interpreter automatically via env
# ---------------------------------------------------------------------------------------- #
#!/usr/bin/env python3


# (1) Print Statements
# ---------------------------------------------------------------------------------------- #
# Print a simple string
print("Hi")

# Print the contents of a variable
someVar = "Hello"
print(someVar)
anotherVar = 10+20
print(anotherVar)

# Print a string containing a variable 
myName = "Ashley"
print("My name is {} ".format(myName))

# Print a string concatenated with a variable
print("My name is also " + myName) 



# (2) Operators
# ---------------------------------------------------------------------------------------- #
"""
    + (addition)
    - (subtraction)
    * (multiplication)
    / (division)
    // (integer division)
    % (modulo)
    = (assignment)
    == (comparison)
    > (greater than)
    < (less than)
"""
myName = "Dany"
yourName = "Yuvraj"

print(myName == yourName) #returns false

myName = yourName
print("My name is " + myName)
print(myName == yourName) #returns True



# (3) Data Types
# ---------------------------------------------------------------------------------------- #
# Print the type of the data. type() is function
print(type("1")) #string
print(type(1)) #integer
print(type(False)) #boolean
print(type("three point five")) #string
print(type(3.5)) #float
print(type(False)) #boolean



# (4) Data Structures
# ---------------------------------------------------------------------------------------- #
# List (mutable)
cities = ['Dubai','Amsterdam','New York','London']

# Tuple (immutable)
seasons = ('Winter','Spring','Summer','Autumn')

# Set (mutable, non-repeating elements)
englishAlphabet = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}

# Dictionary (mutable, non-repeating keys)
superHeroRealName = {
    "Batman": "Bruce Wayne", 
    "Hulk": "Bruce Banner", 
    "Wonder Woman": "Diana Prince"
    }

# Dictionary (another way to do the above)
superHeroRealName = dict(cat="mammal",lizard="reptile",salmon="fish",parakeet="bird")    



# (5) Conditional Statement
# ---------------------------------------------------------------------------------------- #
# If/Else
if (1>2):
    print("1 is greater than 2")
elif (1==2):
    print("1 is equal to 2")
elif ("2"==2):
    print("The string 2 is equal to the integer 2")
else:
    print("None of the above are true")

# Inline
gender = "Abu Dhabi"
fact = "This is the capital city of the UAE" if(gender == "Abu Dhabi") else "This is not the capital city of the UAE"
print(fact)



# (6) Loops
# ---------------------------------------------------------------------------------------- #
# range
start = 0
end = 60
for secondInAMinute in range(start,end+1):
    print(secondInAMinute)

# while
percent = 0
while(percent<100):
    print("{}% is not enough! You need to do better.".format(percent))
    percent+=1
if(percent == 100):
    print("{}% well done!".format(percent))    

# for
theUAE = ['Dubai', 'Abu Dhabi', 'Sharjah', 'Ras Al Khaimah', 'Umm Al Quwain', 'Fujairah', 'Ajman']
for emirate in theUAE:
    print("Welcome to {}".format(emirate))



# (7) Functions
# ---------------------------------------------------------------------------------------- #
# Returns true if the number (arg) is even
def isEven(theNumber):
    if theNumber % 2==0:
        return True
    else:
        return False

answer = isEven(1)
print(answer)

# This function does not return a value!
def printTheName(name="jon doe"):
    print("The name is {}".format(name))

theName = printTheName("Dany")
print(theName)

# A function to print a hello statement
def sayHello(name):
    print('Hello ' + str(name) + "!")
    return name

sayHello("Jimmy")

# Will check the type of data
def printTheType(m=1):
    if(type(m) is int):
        print('It is an integer')
    elif(type(m) is str):
        print('It is a string')
    else:
        print('It is unrecognized')

printTheType(1)

# Scope
location = "Im outside"
def theLocation():
    location = "Im inside"
    return location

print(location)



# (8) Objects
# ---------------------------------------------------------------------------------------- #
class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()
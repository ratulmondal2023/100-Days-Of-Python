# strings are immutable
a = "Ratul!!! !!!!!!!!! Ratul"
print(len(a)) # strings lenth
print(a) # print the string

# upper() :
print(a.upper()) # use for uppercase

# lower() :
print(a.lower()) # use for lowercase

# rstrip() :
print(a.rstrip("!")) # strip the straling character

# replace() :
print(a.replace("Ratul", "John")) # use for replace the string what if you want

# split() :
print(a.split(" ")) # use for list the string

# capitalize() :
blogHeading = "introduction tO jS"
print(blogHeading.capitalize()) # use for capitalize the string

str1 = "welcome to the Console!!!"
print(len(str1)) # len use for string lenth

# center() :
print(str1.center(50)) # use for make the string line in center

# count() :
print(a.count("Ratul")) # use for count the string 

# endswith() :
print(str1.endswith("!!!")) # use for knowing that the line is end in the ending true/false
print(str1.endswith("to", 4, 10))


str1 = "He's name is Dan. He is an honest man."
# find() :
print(str1.find("is")) # use to find the letter in number format

# index() :
# print(str1.index("ishh")) # use for fix the errors in the string line

# isalnum() :
str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # use for knowing that are you have any number in the string then it will show false
str2 = "Welcome00"
print(str2.isalpha()) # If any other characters or punctuations or numbers(0-9) are present, then it returns False.

# islower() :

str1 = "hello world"
print(str1.islower()) # use for knowing that the string line has any Uppercase then its through false


# isprintable() :

str1 = "We wish you a Merry christmas\n"
print(str1.isprintable()) # returns True if all the values within the given string are printable, if not, then return False.

# isspace() :

str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

# istitle() :

str1 = "World Health Organization" 
print(str1.istitle()) # returns True only if the first letter of each word of the string is capitalized, else it returns False.

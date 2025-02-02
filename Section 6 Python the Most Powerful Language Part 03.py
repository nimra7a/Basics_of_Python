#!/usr/bin/env python
# coding: utf-8

# In[2]:


# take an inout from user, encrypt it so that no one can hack it but show the correct message to the user.
msg = input("Please enter your message here: ")[::-1]
print("Hacker is reading : " , msg)
print("Receiver is reading:  ", msg[::-1])


# # String

# # Slicing

# In[4]:


# Slice From the Start
message = "Hello World!"
print(message[:7])


# In[5]:


# Slice From the End
print(message[3:])


# In[10]:


# Negative Indexing
print(message[-10:-4])


# In[12]:


# Reverse Slicing
print(message[::-1])


# # Modify Strings

# # upper(): change the string to upper_case

# In[13]:


name = "nimra ansari"
print(name.upper())


# # lower(): change the string to lower_case

# In[14]:


name = "NIMRA ANSARI"
print(name.lower())


# # capitalize(): capitalize the 1st letter of string

# In[15]:


msg = "hello sansa! how you have been?"
print(msg.capitalize())


# # strip(): removes any whitespace from beginning and ending

# In[20]:


msg = " Hello, World "
print("This is the message: " ,msg)
# with strip
print("This is the message: ", msg.strip())


# # replace(): replaces a string with another string

# In[21]:


a = "Hello, World!"
print(a.replace("H", "J"))


# # split(): returns a list where the text between the specified separator becomes the list items

# In[22]:


msg = "Hello, World"
print(msg.split())


# # Escape Characters

# In[26]:


# escape character allows you to use double quotes when you normally would not be allowed
txt = "He said, \"This is my book.\""
print(txt)


# # Signle Quote

# In[27]:


txt = "It\'s alright."
print(txt)


# # \n for new line

# In[28]:


txt = "Hello\nWorld"
print(txt)


# # \t for Tab

# In[30]:


txt = "Hello\tWorld"
print(txt)


# # \b for backspace

# In[32]:


txt = "Hello \bWorld"
print(txt)


# # String Methods

# # capitalize(): Converts the first character to upper case

# In[37]:


name = "hello Nimra Ansari"
print(name.capitalize())


# # casefold(): Converts string into lower case

# In[38]:


print(name.casefold())


# # center(): Returns a centered string

# In[41]:


print(name.center(100))


# # count(): Returns the number of times a specified value occurs in a string

# In[47]:


print(name.count("s"))


# # encode(): Returns an encoded version of the string

# In[50]:


str = "Türkiye"
x = str.encode()
print(x)


# # endswith(): Returns true if the string ends with the specified value

# In[53]:


str = "This is my shirt."
x = str.endswith(".")
print(x)


# # expandtabs(): Sets the tab size of the string

# In[56]:


str = "This\t is\t my\t shirt\t."
x = str.expandtabs(8)
print(x)


# # find(): Searches the string for a specified value and returns the position of where it was found

# In[57]:


str = "Welcome! this is your new class."
print(str.find("your"))


# # format(): Formats specified values in a string

# In[59]:


str = "This book is of {price:.3f} dollars!"
print(str.format(price = 100))


# # index(): Searches the string for a specified value and returns the position of where it was found

# In[60]:


str = "Welcome! this is your new class."
print(str.index("your"))


# # isalnum(): Returns True if all characters in the string are alphanumeric

# In[65]:


str1 = "Welcome! this is your new class."
str2 = "100dollars"
print("String 1:" , str1.isalnum())
print("String 2:" , str2.isalnum())


# # isalpha(): Returns True if all characters in the string are in the alphabet

# In[68]:


str1 = "Welcome! this is your new class."
str2 = "dollars"
print("String 1:" , str1.isalpha())
print("String 2:" , str2.isalpha())


# # isascii(): Returns True if all characters in the string are ascii characters

# In[69]:


str = "recreate"
print(str.isascii())


# # isdecimal(): Returns True if all characters in the string are decimals

# In[72]:


str1= "89"
str2 = "89.8"

print(str1.isdecimal())
print(str2.isdecimal())


# # isdigit(): Returns True if all characters in the string are digits

# In[73]:


str1 = "Welcome! this is your new class."
str2 = "897"
print("String 1:" , str1.isdigit())
print("String 2:" , str2.isdigit())


# # isidentifier(): Returns True if the string is an identifier

# In[77]:


# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), 
# or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

str1 = "Welcome! this is your new class."
str2 = "hello_world1"
print("String 1:" , str1.isidentifier())
print("String 2:" , str2.isidentifier())


# # islower(): Returns True if all characters in the string are lower case

# In[87]:


str = "nimra ansari"
print(str.islower())


# # isnumeric(): Returns True if all characters in the string are numeric

# In[88]:


num = "1234"
print(num.isnumeric())


# # isprintable(): Returns True if all characters in the string are printable

# In[89]:


str = "Türkiye"
print(str)
print(str.isprintable())


# # isspace(): Returns True if all characters in the string are whitespaces

# In[98]:


str =  "  "
print(str.isspace())


# # istitle(): Returns True if the string follows the rules of a title

# In[99]:


# The istitle() method returns True if all words in a text start with a upper case letter, 
# AND the rest of the word are lower case letters, otherwise False.
str = "Türkiye"
print(str)
print(str.istitle())


# # ljust(): Returns a left justified version of the string

# In[105]:


# The ljust() method will left align the string, using a specified character (space is default) as the fill character.
# Syntex 
# string.ljust(length, character)
txt = "Türkiye"

print(txt.ljust(20), "is a beautiful place to visit.")


# # lower(): Converts a string into lower case

# In[106]:


name = "NIMRA ANSARI"
print(name.lower())


# # lstrip(): Returns a left trim version of the string

# In[129]:


fruit = "      Mango"
print("of all fruits, " , fruit.lstrip() , " is my favorite.")


# # maketrans(): Returns a translation table to be used in translations

# In[130]:


name = "Hello Sam"
trans = name.maketrans("S", "M")
print(trans)
print(name.translate(trans))


# # partition(): Returns a tuple where the string is parted into three parts

# In[131]:


txt = "He watches movies all day"
print(txt.partition("movies"))


# # replace(): Returns a string where a specified value is replaced with a specified value
# 

# In[132]:


str = "Nimra Ansari"
print("Original String: ", str)
print("After replacement: " , str.replace("Nimra", "Laiba"))


# # rfind(): Searches the string for a specified value and returns the last position of where it was found

# In[133]:


print(str.rfind("a"))


# # rindex(): Searches the string for a specified value and returns the last position of where it was found

# In[134]:


print(str.rindex("a"))


# # rjust(): Returns a right justified version of the string

# In[135]:


print(str.rjust(20), " is an MS student.")


# # rpartition(): Returns a tuple where the string is parted into three parts

# In[136]:


txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)


# # rsplit(): Splits the string at the specified separator, and returns a list

# In[137]:


fruits = "Apple , Banana, Mango, Orange, Cherry"
print(fruits.rsplit(","))


# # rstrip(): Returns a right trim version of the string

# In[138]:


txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")


# # split(): Splits the string at the specified separator, and returns a list

# In[139]:


fruits = "Apple , Banana, Mango, Orange, Cherry"
print(fruits.split(","))


# # splitlines(): Splits the string at line breaks and returns a list

# In[144]:


fruits = "Apple\nBanana \nMango \nOrange \nCherry"
print(fruits.splitlines())


# # startswith(): Returns true if the string starts with the specified value

# In[145]:


txt = "He watches movies all day"
print(txt.startswith("He"))


# # strip(): Returns a trimmed version of the string

# In[146]:


txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")


# # swapcase(): Swaps cases, lower case becomes upper case and vice versa

# In[147]:


fruits = "Apple , Banana, Mango, Orange, Cherry"
print(fruits.swapcase())


# # zfill(): Fills the string with a specified number of 0 values at the beginning

# In[148]:


txt = "50"
x = txt.zfill(10)
print(x)


# In[ ]:





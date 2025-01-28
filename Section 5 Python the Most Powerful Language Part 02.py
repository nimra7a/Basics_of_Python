#!/usr/bin/env python
# coding: utf-8

# # Basic Data Types

# # Integer

# In[1]:


integer_example = 42
print("Integer:", integer_example)


# # Float

# In[2]:


float_example = 3.14
print("Float:", float_example)


# # Complex Number

# In[24]:


complex_example = 2+3j
print("Complex Number:" , complex_example)
print("Real Part:", complex_example.real)
print("Imaginary Part:", complex_example.imag)


# # String

# In[6]:


string_example = "Hello, Nimra!"
print("String: " , string_example)


# # Boolean

# In[7]:


boolean_example = True
print("Boolean: " , boolean_example)


# # None

# In[8]:


none_example = None
print("None: " , none_example)


# # Mathematical Operators

# # Addition

# In[9]:


a , b = 3, 10
print("Addition:" , a+b)


# # Subtraction

# In[10]:


a, b = 800, 53
print("Subtraction:", a-b)


# # Multiplication

# In[11]:


a, b = 8, 9
print("Multiplication:", a*b)


# # Division

# In[12]:


a, b = 90, 5
print("Division:", a/b)


# # Exponential

# In[13]:


a, b = 5, 3
print("Exponential:", a**b)


# # Modulus

# In[15]:


a, b = 100 , 8
print("Modulus:", a%b)


# # Order of precedenece (PEMDAS)

# In[20]:


a, b, c, d = 2,5,6,9
print("PEMDAS: " , int((a+b) * b / c + (10-d)))


# # Augmented Assignments

# In[23]:


a = 64
a+=a
print("Augmented Addition: " , a) #128

b = 228
b-= a
print("Augmented Subtraction: ", b) #100

c = 4
c*=c
print("Augmented Multipication: " ,c) #16

d = 64
d/=c
print("Augmented Division: ", d) #4


# # String Methods

# # upper()/lower(): Converts to uppercase/lowercase.

# In[25]:


print("hello".upper())


# In[26]:


print("NIMRA ANSARI".lower())


# # strip(): Removes leading and trailing whitespace.

# In[27]:


print(" This is the jupter notebook. ".strip())


# # replace(): Replaces a substring with another.

# In[29]:


print("Hello World!".replace("World", "Nimra"))


# # split(): Splits a string into a list.

# In[30]:


print("a, b, c".split())


# # join(): Joins elements of a list into a string.

# In[32]:


print(":".join(["have", "a", "good", "day", "!"]))


# # find()/index(): Finds the position of a substring.

# In[35]:


print("Index():", "Forver!".index("ve"))
print()


# In[36]:


print("find():", "Forver!".find("ve"))
print()


# # count(): Counts occurrences of a substring.

# In[37]:


print("Count: ", "banana".count("a"))


# # Concatenation

# # Using + Operator

# In[40]:


str1= "Hello"
str2 = " Nimra Ansari! "
str3 = "Have a good day."

print(str1 + str2 + str3)


# # Using , Sign

# In[42]:


str1= "Hello"
str2 = " Nimra Ansari! "
str3 = "Have a good day."

print(str1 , str2 , str3)


# # Using join() Method

# In[43]:


words = ["Python", "is", "awesome"]
result = " ".join(words)
print(result)


# # Using format() Method

# In[44]:


name = "Alice"
greeting = "Hello, {}!".format(name)
print(greeting)


# In[51]:


name = "Alice"
time = 9
greeting = "Hello, {0}! its {1}am.".format(name,time)
print(greeting)


# # Using f-strings

# In[45]:


name = "Alice"
age = 25
result = f"My name is {name} and I am {age} years old."
print(result)


# # Using % Operator (Old-Style Formatting)

# In[52]:


name = "Nimra"
greeting = "hello, %s"%name
print(greeting)


# # Concatenating Multiple Lines

# In[53]:


long_str = ( 
    "Hello Ms.!"
    "Hope you're doing well."
    "How can I help you?"
)
print(long_str)


# # Using * for Repetition

# In[59]:


repeat = "Hello " * 5
print(repeat)


# # String Indexing

# # Positive Indexing

# In[60]:


text = "Python"

print(text[0])
print(text[1])


# # Negative Indexing

# In[61]:


print(text[-1])
print(text[-2])


# # Slice Indexing

# # Extract substring

# In[63]:


text = "Python"
print(text[0:3])  # 'Pyt' (characters from index 0 to 2)
print(text[:3])   # 'Pyt' (same as above)


# # Step (skip characters)

# In[65]:


print(text[::2]) #[start:stop:skip]


# # Negative Step (reverse) 

# In[66]:


print(text[::-1])


# In[ ]:





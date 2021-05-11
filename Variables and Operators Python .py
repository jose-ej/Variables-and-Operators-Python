#!/usr/bin/env python
# coding: utf-8

# # Variables and Operators

# ## Variables 

# ### Variables are containers for storing values 
# 
# Rule for Declraing variable 
# 
# 1.it cannot start with numbers
# 
# 2.it can A-Z,a-z,0-9 and _ ('underscores')
# 
# 3.variable names are case-sensitive(Jose,JOSE and jose are three differnt variables)/
# 
# 4.it can start with letter or _ ('underscores')
# 
# Example: 
#           Name= ' Jose E J'
# 
#           _2Name='Jose E J'
#           
#           x= 12, y= 15, A= 52, 
#           
#           2name= 'Jose E J' is Invalid (reff rule no 1)
#          
#        

# ## Operators

# ## These are used to perform Operations in variables or values.
#  Example:
#          10+15
#             Here the "+" sign is Operator(arithematic Operator) and 10 and 15 are operands.

# ## Type of Operators 
# 
# 1. Arithmetic Operators
# 
# 2. Logical Operators
# 
# 3. Comparison  Operators
# 
# 4. Assignment  Operators

# ### 1.Arithmetic Operators
# 
# these are used for common mathematical oprations performed with numerical values.
# 
# The oprations are addition, substraction,multiplication,division, moduls, exponentiation and floor division

# ##    +       Addition           x+y 

# In[20]:


x= 5
y = 10
x+y


# ## - Subtraction x-y

# In[23]:


x= 10
y=5
x-y


# ## * multiplication x*y

# In[25]:


x=10
y=5
x*y


# ## / Division x/y

# In[28]:


x/y # x and y will choose last values


# ## % Modulus x%y
# 
# In Python and generally speaking, the modulo (or modulus) is referred to the remainder from the division of the first argument to the second. The symbol used to get the modulo is percentage mark i.e. ‘%’.
# 

# In[31]:


x=25
y=2


# In[33]:


x%y


# ## ** Exponentiation x**y
# 
# Another way to exponentiate values is with the built-in pow () function (Python.org, n.d. a). This function accepts two arguments. The first is the base, or the number that we want to raise to a particular power. The second is the exponent to use. pow () always calculates an exact integer power.

# In[35]:


x=2
y=4
y**x


# In[36]:


x**2


# In[37]:


2**2


# ## // Floor Division x//y 
# 
# With floor division, one number, the dividend, is divided by another number, the divisor, and the result, or quotient – whatever it may happen to be – will be a rounded-down integer value.
# 
# 
# 

# In[39]:


x=10
y=3
x//y # x/y= 3.333333333


# ## 2.Logical Oerators  
# 
# logical operators are used for conditional statements(either true or fales)
# 
# And, Or and Not

# ## And
# both conditions are true 

# In[41]:


x= 8
x>3 and x<10 # both conditions are true 


# In[48]:


x<3 and x<10 # one condition is fales 


# ## Or
# 
# Atleast on condition is true  

# In[43]:


x=10
x>1 or x<15 # one condition is true


# In[47]:


x<1 or x>15 # both conditions are fales 


# In[50]:


x>1 or x>15 # both conditions are true 


# ## Not 
# 
# Reverse the result (if True it become False and if False it become True )

# In[51]:


x=10
x>10


# In[52]:


not(x>10)


# ## 3. Comparison Operators
#  it used to compare two values and/ or varables

# ## == Equal x==y
# Code for equal to operator

# In[54]:


x=5
y=10
x==y


# In[55]:


x=14
y=14
x==y


# ## != Not Equal x!=y
#   
# 

# In[57]:


x=14
y=14
x!=y


# In[58]:


x=15
y=13
x!=y


# ## >  Greater than 

# In[59]:


x=10
x>15


# In[60]:


x=10
y=5
x>y


# ## < Less than

# In[65]:


x=10 
x<5


# In[66]:


x=10
y=15
y>x


# ## >= Greater Than or Equal to

# In[67]:


x=10
x>=5


# In[69]:


x=10
y=5
x>=90


# ## <= Less than Or Equal to

# In[70]:


x=10
x<=15


# In[73]:


x=10
y=15
y<=x


# ## 4. Assignment Operators

# ## =

# In[96]:


x=5 #same as x=5
x


# ## +=

# In[97]:


x=3
x+=4 # same as x= x+4
x


# ## -=

# In[98]:


x=3
x-=4 #same as x= x-4
x


# ## *=

# In[99]:


x=3
x*=4 # same as x= x*4
x


# ## /=

# In[102]:


x=3
x/=4 # same as x= x/4
x


# ## %=

# In[103]:


x=3
x%=4 # same as x= x%4
x


# ## //=

# In[106]:


x=3
x//=4 #same as x= x//4
x


# ## **=

# In[112]:


x=3
x**=4 #samme as x=x**4
x


# ## &=

# In[120]:


x= {3,4}
x&={4,5} #same as x= x&{4,5}(intersection ) it is easy to understand using set oprations 
x


# ## |=

# In[121]:


x={3,4}
x|={4,5} # same as x= x&{4,5}(union) it is easy to understand using set oprations 
x


# In[ ]:





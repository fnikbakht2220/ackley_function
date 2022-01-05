#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import math
# Fitness function. The code maximizes the value of the fitness function
def Ackley_func(x_local):
    D=x_local.size     # size of Numpy vector x_local
    ackley_i=[0]
    for i,x_i in enumerate (x_local):
        ackley_i += -20.0 * np.exp(-0.2 * np.sqrt((1/D)* np.power(x_i,x_i)))        - np.exp((1/D) * (np.cos(2 * np.pi * x_i)))
    ackley_i += np.exp(1) + 20
    return ackley_i 


x_local=np.array([2,3,4,5])
b=Ackley_func(x_local)
print (b)


# In[ ]:





# In[ ]:





# In[ ]:





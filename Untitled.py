#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World!!")


# In[ ]:





# In[ ]:





# In[3]:


import numpy as np


# In[4]:


import matplotlib.pyplot as pl


# In[5]:


u = 2


# In[6]:


sigma = .5


# In[10]:


v = np.random.normal(u, sigma, 1000)


# In[12]:


pl.plot(v)


# In[13]:


pl.hist(v)


# In[17]:


help(pl.hist)


# In[28]:


help(np.arange)


# In[22]:


x = np.arange(0, 2*np.pi, np.pi/20)


# In[23]:


y = np.cos(x)


# In[24]:


z = np.sin(x)


# In[26]:


pl.plot(y)


# In[27]:


pl.plot(z)


# In[29]:


pl.stem(x)


# In[30]:


pl.stem(y)


# In[31]:


pl.stem(z)


# In[32]:


help(pl.stem)


# In[34]:


help(pl.subplots)


# In[40]:


f, axarr = pl.subplots(2, sharex = True)


# In[46]:


axarr.plot(y,z)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





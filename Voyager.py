#!/usr/bin/env python
# coding: utf-8

# In[56]:


import matplotlib


# In[57]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[58]:


import pylab as plt


# In[59]:


from blimpy import Waterfall


# In[60]:


obs = Waterfall('voyager_f1032192_t300_v2.fil')
obs.info()


# In[61]:


print(obs.header)
print(obs.data.shape)


# In[62]:


obs.plot_spectrum


# In[63]:


obs.plot_spectrum(f_start=8420.18, f_stop=8420.25)


# In[64]:


plt.figure(figsize=(8, 6))
plt.subplot(3,1,1)
obs.plot_spectrum(f_start=8420.193, f_stop=8420.195) # left sideband
plt.subplot(3,1,2)
obs.plot_spectrum(f_start=8420.2163, f_stop=8420.2166) # carrier
plt.subplot(3,1,3)
obs.plot_spectrum(f_start=8420.238, f_stop=8420.24) # right sideband
plt.tight_layout()


# In[ ]:





# In[ ]:





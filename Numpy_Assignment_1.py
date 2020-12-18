#!/usr/bin/env python
# coding: utf-8

# In[171]:


import numpy as np


# In[38]:


a=np.array(10)   #1
a


# In[18]:


x=np.zeros((4,4))   #2
x


# In[60]:


np.ndim(x)             #3
a


# In[50]:


a=np.arange(15,40)     #4
a


# In[53]:


b=a*2                 #5
b


# In[56]:


c=a+b                 #6
c


# In[62]:


1/c                   #7


# In[61]:


c>50                  #8


# In[64]:


c[8]                  #9


# In[75]:


d=c[c>96]             #10
d


# In[76]:


np.sqrt(d)             #11


# In[78]:


np.power(d,2)          #12


# In[101]:


np.exp(d)              #13


# In[91]:


x=np.ones((5,5))        #14
x


# In[97]:


x[1:-1,1:-1]=0          #15
x


# In[99]:


x[1:,1:]+=2             #16
x


# In[18]:


z=np.random.random((3,3))    #17
z


# In[21]:


z.min()                     #18


# In[25]:


z.max()                     #19


# In[33]:


z.mean()                    #20


# In[55]:


z[1:2]**2                   #21


# In[70]:


a=np.array([2,4,3,6,7,9])
a


# In[119]:


a[::-1]                     #22


# In[146]:


a = np.arange(-4,8).reshape(4, 3)   #23
a


# In[163]:


a[::3]       #24


# In[184]:


a[-1,2]=1     #25
a


# In[44]:


np.linspace(1,3,5)       #26


# In[201]:


y=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
y


# In[202]:


y[1]=50                 #27
y


# In[244]:


c=np.arange(0,12).reshape(4,3)
c


# In[245]:


c[1:3,2:3]           #28


# In[7]:


u=[-3,-2,0,1,2,4,6,7,9]


# In[8]:


v=[-2,1,3,5,7,8,9,10,11]


# In[9]:


w=np.intersect1d(u,v)    #29
w


# In[10]:


np.where(w)              #30


# In[21]:


np.setdiff1d(u,v)        #31


# In[15]:


k=np.concatenate((u,v))   #32
k


# In[16]:


k[k%2==1]                 #33


# In[18]:


k[k%2==0]                 #34


# In[20]:


np.where(k%2==1,-1,k)      #35


# In[39]:


j=np.arange(12).reshape(4,3)
j


# In[50]:


j[[0,3,2,1,],:]            #36


# In[71]:


j[[0],:]+2                 #37


# In[73]:


m=np.arange(20)
m


# In[87]:


np.set_printoptions(threshold=8)   #38


# In[91]:


m=np.arange(20)
m


# In[101]:


np.where(m<5,4,np.where(m>15,3,m))   #39


# In[104]:


np.random.seed(50)


# In[110]:


a=np.random.uniform(1,10)            #40
a


# In[111]:


np.sin(a)                            #41


# In[119]:


a=np.arange(3)
b=np.arange(1,4)                     #42
c=np.arange(0,2,5)


# In[126]:


d=np.array([a,b,c])                  #43
d


# In[140]:


x=np.zeros((7,7))
x


# In[141]:


x+=np.arange(7)                    #44
x


# In[143]:


y=np.random.random(15)              #45
y.sort()
y


# In[146]:


Z=np.arange(20)                     #46
np.add.reduce(Z)


# In[150]:


a=np.random.random(8)               #47
a[a.argmax()]=0
a


# In[154]:


m= [0,2,4,6,8]                      #48
n= [1,3,5,7,9]
r= np.bincount(m,n)
r


# In[164]:


a= np.arange(25).reshape(5,5)       #49
a[[0,1]] = a[[1,0]]
a


# In[173]:


z=np.random.randint(0,15,35)        #50
print(np.bincount(z).argmax())


# In[ ]:





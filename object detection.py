#!/usr/bin/env python
# coding: utf-8

# In[33]:


import cv2
import numpy as np


# In[34]:


a=cv2.imread('C:\\Users\\lakshman\\Desktop\\i1.jpg')


# In[35]:


plt.imshow(a)


# In[36]:


type(a)


# In[37]:


gray_img = cv2.medianBlur(cv2.cvtColor(a, cv2.COLOR_RGB2GRAY), 3)

circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=50, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))


# In[38]:


masking=np.full((a.shape[0], a.shape[1]),0,dtype=np.uint8)

for j in circles[0, :]:

    cv2.circle(masking, (j[0], j[1]), j[2]+3, (255, 255, 255), -1)


# In[39]:


mask = np.full((a.shape[0], a.shape[1]), 0, dtype=np.uint8)


# In[40]:


plt.imshow(masking)
plt.show()


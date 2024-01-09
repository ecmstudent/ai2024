#!/usr/bin/env python
# coding: utf-8

# # Week 1: Getting started with Anaconda, Jupyter Notebook and Python
# 
# Exercises to familiarise myself with Jupyter Notebook and its relationship to Python.

# ### a) I choose this course beacause I am very interested in the subject area and I think that it could benefit me in the future due to it being a field increasing in popularity and relevance.

# ### b) I have no experience in AI or Python. 

# ### c) I expect to learn
#     - The basics of python
#     - The developments occuring in AI
#     - Ethics surround AI
#     - More details about machine learning

# In[ ]:


greeting = ("Have a good day!")

print (greeting)


# In[ ]:


from IPython.display import *

YouTubeVideo("472AnCrHYVs")


# # Week 2: Exploring Data in Multiple Ways

# In[ ]:


from IPython.display import Image 


# In[ ]:


Image ("picture1.jpg")


# In[ ]:


from IPython.display import Audio


# In[ ]:


Audio ("audio1.mid")


# In[ ]:


Audio ("audio2.ogg")


# #### This file is licensed under the Creative Commons Attribution-Share Alike 3.0 Unported license.
#     You are free: 
#         •	to share – to copy, distribute and transmit the work
#         •	to remix – to adapt the work
#     Under the following conditions: 
#         •	attribution – You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
#         •	share alike – If you remix, transform, or build upon the material, you must distribute your contributions under the same or compatible license as the original.
# 
# The original ogg file was found at the url: 
# https://en.wikipedia.org/wiki/File:GoldbergVariations_MehmetOkonsar-1of3_Var1to10.ogg
# 

# In[ ]:


from matplotlib import pyplot
test_picture = pyplot.imread("picture1.jpg")
print("Numpy array of the image is: ", test_picture)
pyplot.imshow(test_picture)


# #### When using the 'pyplot.imshow(test_picture_filtered)' command the image is displayed more as points on a graph rather than as the actual image shown above. We assume this is due to the numbers being divided moaving them smaller and less visable as an image and more as points on the graph. 

# In[ ]:


from sklearn import datasets
dir(datasets)


# #### I chose load_wine because I like wine and load_diabetes as I don't know much about the condition so wanted to know more. 

# In[ ]:


from sklearn import datasets

wine_data = datasets.load_wine()

print(wine_data.target_names)

wine_data.keys()


# #### My dataset has 13 features. By running the command wine_data.target_names I believe that this dataset is aiming to classify the different wines into categories. However, from this command alone I am not able to tell anything further about those categories. 

# In[ ]:


from sklearn import datasets

load_diabetes = datasets.load_diabetes()

print(load_diabetes.DESCR)


# In[ ]:


from sklearn import datasets
import pandas

wine_data = datasets.load_wine()

wine_dataframe = pandas.DataFrame(data=wine_data['data'], columns=wine_data['feature_names'])

wine_dataframe.head()
wine_dataframe.describe()


# #### I think that these commands take the information from the dataset and display them in a table. This makes the information easier to read. 

# In[ ]:





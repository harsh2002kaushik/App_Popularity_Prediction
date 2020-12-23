#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.read_csv(r'C:\Users\harsh\Desktop\Extracted_games.csv')


# In[2]:


df.head()


# In[3]:


df['editors_choice'] = df['_editors_choice'].apply(lambda x: 0 if x=='0' else 1)
df['editors_choice'].value_counts()


# In[4]:


df['_game_types'].value_counts()


# In[5]:


types=df['_game_types'].apply(lambda x: x.split(',')[1])
types=df['_game_types'].apply(lambda x: x.replace(']','').replace(" ","").replace("'","").split(',')[1:])


# In[6]:


types.value_counts()


# In[7]:


types=df['_game_types'].apply(lambda x: x.replace(']','').replace(" ","").replace("'","").split(',')[1:])
c=types.apply(lambda x: ','.join(x)).apply(lambda x: x.lower().replace('inc.','').replace('inc','').replace('llc','').replace('ltd','').replace('ltd.','').replace('limited','').replace('calmgames)','').replace('&',',').replace('and',',').replace('educational','education').replace('.','').replace(' ',','))
df['game_types'] = c.apply(lambda x: x.split(',')[0])
df['game_types'] = df['game_types'].apply(lambda x: 'not_specified' if x=='' else x)
print(df['game_types'].value_counts())


# In[8]:


a=df['game_types'].value_counts()


# In[9]:


a.index


# In[10]:


df['comments'] = df['_comments'].apply(lambda x: x.lower().replace('not given','0').split(' ')[0].replace(',','')).apply(lambda x: int(x) )


# In[11]:


def f(y):
    if y=='Install':
        x=0
    else:
        if len(y.split(' '))==2:
            x=int(float((y.split(" ")[0])))
        else:
            x=int(float((y.split(" ")[1])))    # for games on offer
    return x 
df['price'] = df['_price'].apply(lambda x: x.replace('₹','').replace('.','').replace(',','')).apply(lambda x : f(x)) 


# In[12]:


df['updated'] = df['_updated'].apply(lambda x: x.split(' ')[2])


# In[13]:


size = df['_size'].apply(lambda x: '0' if x=='Varies with device' else x).apply(lambda x: int(float(x.split('M')[0])))
size_count = size.value_counts()
print(size_count)
d=0
for i in size_count.index: # to fill the data not given
    d+= size_count.get(key=i)*i
df['size'] = size.apply(lambda x: int(d/size_count.sum()) if x==0 else int(x))


# In[14]:


df['installs'] = df['_installs'].apply(lambda x: int(float(x.split('+')[0].replace(',',''))))


# In[15]:


req_android = df['_required_android'].apply(lambda x: 0 if 'Varies with device' in x else int(x.split('.')[0]))
req_android_count = req_android.value_counts()
print(req_android_count)
b = 0
for i in req_android_count.index:       # to fill the data not given
    b+= req_android_count.get(key=i)*i
df['required_android'] = req_android.apply(lambda x: int(b/req_android_count.sum()) if x==0 else int(x))


# In[16]:


df['content_rating'] = df['_content_rating'].apply(lambda x: 'Rated for 12+' if x=='unavailable' else x).apply(lambda x: x.split('\n')[0]).apply(lambda x: int(x.replace('Rated for ','').replace('+','')))


# In[17]:


df['_game_features']=df['_content_rating'].apply(lambda x: x.split('\n')[1])
df['game_features']=df['_game_features'].apply(lambda x: 0 if x.split(',')[0]=='Learn more' else len(x.split(',')))
df['game_features'].value_counts()
# will have to explain why only the length has been taken


# In[18]:


df['interactive_elements'] = df['_interactive_elements'].apply(lambda x: x.split(',')).apply(lambda x: 0 if 'none' in x else len(x))


# In[19]:


in_app_products = df['_in_app_products'].apply(lambda x: x.replace('per item','').replace('₹','').replace(',','').replace('.',''))
in_app_products_max = in_app_products.apply(lambda x: x.split(' – ')).apply(lambda x: 0 if len(x)==1 else int(x[1]))
in_app_products_min = in_app_products.apply(lambda x: x.split(' – ')).apply(lambda x: 0 if x[0]== 'none' else int(x[0]))
df['in_app_products_avg'] = in_app_products_min/2+in_app_products_max/2
df['in_app_products_avg'] = df['in_app_products_avg'].apply(lambda x: int(x))


# In[20]:


df['has_website'] = df['_developer'].apply(lambda x: x.split('\n')[0]).apply(lambda x: 1 if 'Visit website' in x else 0 )


# In[21]:


df.columns


# In[22]:


df=df.drop(['_editors_choice', '_game_types', '_comments', '_price', '_updated','_size', '_installs', '_version', '_required_android','_content_rating', '_interactive_elements', '_in_app_products','_offered_by', '_developer','_game_features'],axis=1)


# In[23]:


df.columns


# In[24]:


df.to_csv(r'C:\Users\harsh\Desktop\Cleaned_Games.csv',index=False)


import pandas as pd
import numpy as np
df = pd.DataFrame(pd.read_excel("C:/Users/vishn/OneDrive/Desktop/4th sem projects/DA/Preprocessed data.xlsx"))
df_new=df.drop(['Name'],axis=1)
matrix=np.matrix(df_new)
u, s, vh = np.linalg.svd(matrix, full_matrices=True)
print(u.shape, s.shape, vh.shape)
us=u.reshape((125, 20))
print(s.shape)
new_value=us*vh
print(u.shape)
print(new_value.shape)
new_value.resize(2500,1)
final=new_value*s
print(final.shape)
final.resize(50,20)
print(final.shape)
print(final)
from scipy import spatial
new_rating=[5,5,0,0,0,0,0,0,5,3,5,5,0,5,0,0,0,4,0,4]
a={}
a={i:1-spatial.distance.cosine(new_rating,final[i]) for i in range(0,50)}
print(a)
b=[]
list=[]
for j in range(0,50):
  b.append(a[j])
list=sorted(b)
for i in range(len(list)):
  for j in range(i+1,len(list)):
    if(list[i]<list[j]):
      list[i],list[j]=list[j],list[i]
print(list)
new_list=[]
neighbor=int(input("Enter the no. neighbor:"))
for i in range(0,neighbor):
  new_list.append(list[i])
print(new_list)
nl=[] 
for val in a.values(): 
    nl.append(val) 
print(nl)
user=[]
for i in range(0,50):
    if(nl[i] in new_list):
      user.append(i)
      print(i)
rating=[]
for i in range(0,50):
  if(i in user):
    rating.append(df_new.iloc[i].astype('int'))
counts =[]
counts=[[int(df_new.iloc[j,i]) for j in user]for i in range(0,20)] 
print(counts)
s=[]
for i in range(0,20):
  s.append((sum(counts[i]))/len(counts[i]))
print(s)
no_of_recommendation=int(input("Enter the no. of movies to recommend:"))
sa=[]
sa=s.copy()
print(s)
#print(sa)
sa.sort()
print(sa[-no_of_recommendation:])
l2=sa[-no_of_recommendation:]
index = 0
print(s)
recommended_movie=[]
def matched_index(s, l2):
    l2= set(l2)
    return [m+1 for m, n in enumerate(s) if n in l2]
print(matched_index(s, sa[-no_of_recommendation:]))
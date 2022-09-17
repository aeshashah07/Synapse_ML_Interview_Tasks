# -*- coding: utf-8 -*-
"""ML Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aSY63BFQijzE2kZB7RFxkBXkbn7LtyiS

#Task 2

Run the following cell to import your google drive
"""

from google.colab import drive
drive.mount("/content/gdrive")

"""Run the following cell to import the necessary libraries"""

import pandas as pd
import matplotlib.pyplot as plt

"""## Task 2.1

For aspiring data scientists and machine learning enthusiasts, it is vital that they understand the coding environment. We normally use a jupyter notebook for most of our programming. To understand its importance, lets perform a small exercise.

We are given 2 datasets, they have data of certain students from 2 different branches and their respective divisions.

Download the datasets from the links given below -

Task2p1_0 - https://drive.google.com/file/d/1sCGCErnf2iC_qKUHcGLrt2O2HwuiwZYD/view?usp=sharing

Task2p1_1 - https://drive.google.com/file/d/1Kb_TcAEfsUGi-KPZpsh8pXBaxfs4AsHh/view?usp=sharing

Create a folder named 'Task2p1' in your google drive and upload the datasets 'Task2p1_0' and 'Task2p1_1' there.

###Python Script
"""

data = pd.read_csv("/content/gdrive/MyDrive/Task2p1/Task2p1_0.csv")
data
data = pd.read_csv("/content/gdrive/MyDrive/Task2p1/Task2p1_1.csv")
data

"""###Jupyter Notebook"""

data = pd.read_csv("/content/gdrive/MyDrive/Task2p1/Task2p1_0.csv")

data

data = pd.read_csv("/content/gdrive/MyDrive/Task2p1/Task2p1_1.csv")

data

"""Note the difference between the outputs you get after using the code in cell 3 as a python script and after running it line by line in a jupyter notebook.

In python script, the last table gets printed (because thats the last value of the variable 'data') ;

but in the line by line format, both the tables are able to be shown (because for any particular cell, the individual value of 'data' is the last value assigned to it)

##Task 2.2

Download the dataset of fifty random Harry Potter spells from the link given below -

https://drive.google.com/file/d/1F2YEtVZaorL0WPGxOC5vXkMSixuYkI4v/view?usp=sharing

Create a folder named 'Task2hp' in your google drive and upload the dataset there.

Observe the dataset, it is a .csv file. Using pandas library, read the .csv file into a dataframe in the next cell. 

Tip : You can make use of the Files tab in the side bar on the left to navigate through your file structure.
"""

df = pd.read_csv("/content/gdrive/MyDrive/Task2hp/HPSpells.csv")

"""Display first five rows of the dataframe."""

df.head()

"""Remove all the rows having type as 'Hex'"""

df.drop(df[df.Type == 'Hex'].index, inplace = True)
df.head()

"""Now remove the rows from the dataframe having NaN values for column 'Light'."""

df.dropna(subset=['Light'], inplace = True)
df.head()

"""Filter out the spells on the basis of their Type and make a bar graph showing your analysis of the number of spells and their distribution in the five types - Charm, Jinx, Transfiguration, Curse."""

Types = []
number = []

for i in df.Type.unique():
  Types.append(i)

  count = 0
  for j in df.Type:
    if (i == j):
      count +=1
  number.append(count)



# print(df.Type.value_counts())

# for spell, number in df.Type.value_counts():
#   Types.append(spell)
#   number.append(number)

fig = plt.figure(figsize = (7, 7))
 
# Creating the bar plot
plt.bar(Types, number, color ='#f9225f', width = 0.4)
 
plt.xlabel("Types of Spells")
plt.ylabel("No. of spells")
plt.xticks(df.Type.unique())
plt.title("Spell Analysis")
plt.show()
# -*- coding: utf-8 -*-
"""Assn_3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TUCWBprLrnwJNAle6IldGn-HOtmSYV5-

# Assignment 03

# Problem Statement :: Descriptive Statistics - Measures of Central Tendency and variability
Perform the following operations on any open source dataset (e.g., data.csv)
1. Provide summary statistics (mean, median, minimum, maximum, standard deviation) for a dataset (age, income etc.) with numeric variables grouped by one of the qualitative (categorical) variable. For example, if your categorical variable is age groups and quantitative variable is income, then provide summary statistics of income grouped by the age groups. Create a list that contains a numeric value for each response to the categorical variable.
2. Write a Python program to display some basic statistical details like percentile, mean, standard deviation etc. of the species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris- versicolor’ of iris.csv dataset.
Provide the codes with outputs and explain everything that you do in this step.

#Import pandas
"""

#Dataset : "/content/Iris.csv"

"""#read Iris csv file"""

import pandas as pd
from sklearn import preprocessing
import numpy as np
import statistics
df = pd.read_csv("/content/Iris.csv")
df

#checking that categorical data in the dataset
df.select_dtypes(include='object')

#converting categorical data into numerical data
encoder = preprocessing.LabelEncoder()
df["Species"]=encoder.fit_transform(df["Species"])
df

#using groupby function to group data
data = df.groupby(["Species"])
data.groups.keys()  #checking how many groups are formed

df.groupby(["Species"])["SepalWidthCm"].std()

df.groupby(["Species"])["SepalWidthCm"].mean()

df.groupby(["Species"])["SepalWidthCm"].min()

df.groupby(["Species"])["SepalWidthCm"].max()

df.groupby(["Species"])["SepalWidthCm"].var()

df.groupby(["Species"])["SepalWidthCm"].std()

df.groupby(["Species"])["SepalWidthCm"].apply(statistics.mode)

data = df.groupby(["Species"])
data.agg([np.sum, np.mean, np.max])

df.groupby(["Species"])["SepalWidthCm"].agg(pd.Series.mode)
#Understand Your Data With Descriptive Statistics

#Peek at  Data
import pandas
from pandas import read_csv
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
peek = data.head(20)
print(peek)


#Dimensions of  Data
shape = data.shape
print(shape)

#Data Type For Each Attribute
types = data.dtypes
print(types)

#Descriptive Statistics
from pandas import set_option
set_option('display.width', 100)
set_option('precision', 3)
description = data.describe()
print(description)

#Class Distribution (Classification Only)
class_counts = data.groupby('class').size()
print(class_counts)

#Correlations Between Attributes
set_option('display.width', 100)
set_option('precision', 3)
correlations = data.corr(method='pearson')
print(correlations)


#Skew of Univariate Distributions
skew = data.skew()
print(skew)

















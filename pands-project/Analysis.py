import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

#open file with summary
f = open("Summary.txt", "r")
print(f.read())
###############################################################

#Create Histogram
#assign plot a color
sns.set_palette('Blues')
datafile = pd.read_csv('documentation/iris_data.csv')
datafile.columns = ['sepal length', 'sepal width', 'petal length', 'petal width','flower class']
flowers = datafile['flower class'].unique()
#plotting sepal width with flower type 
sns.histplot( x = 'flower class',y = 'sepal width', data = datafile )
plt.title('Sepal width by Flower species')
plt.savefig("histplot1")
plt.clf()

#now we are doing the same with the other three characteristics
sns.histplot( x = 'flower class',y = 'petal width', data = datafile )
plt.title('Petal width by Flower species')
plt.savefig("histplot2")
plt.clf()


sns.histplot( x = 'flower class',y = 'petal length', data = datafile )
plt.title('Petal length by Flower species')
plt.savefig("histplot3")
plt.clf()


sns.histplot( x = 'flower class',y = 'sepal length', data = datafile )
plt.title('Sepal length by Flower species')
plt.savefig("histplot4")
plt.clf()

###################################################################################
#Creating Scatterplot
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

datafile = pd.read_csv('documentation/iris_data.csv')
datafile.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'flower class']

# Group data by flower class and compute min and max values for petal length
datatable = datafile.groupby('flower class')['petal length'].agg(['min', 'max'])

# Create subplots with 1 row and 1 column
fig, ax = plt.subplots(1,1)
#Scatter plot the min and max values for each flower class
ax.scatter(datatable.index, datatable['min'], color='blue')
ax.scatter(datatable.index, datatable['max'], color='yellow')
ax.set_xlabel('Flower Class max/min')
ax.set_ylabel('Petal Length')
plt.suptitle('Petal Length',weight='bold')


datatable = datafile.groupby('flower class')['sepal length'].agg(['min', 'max'])
fig, ax = plt.subplots(1,1)
ax.scatter(datatable.index, datatable['min'], color='blue')
ax.scatter(datatable.index, datatable['max'], color='yellow')
ax.set_xlabel('Flower Class')
ax.set_ylabel('sepal length')
plt.suptitle('Sepal Length',weight='bold')


datatable = datafile.groupby('flower class')['sepal width'].agg(['min', 'max'])
fig, ax = plt.subplots(1,1)
ax.scatter(datatable.index, datatable['min'], color='blue')
ax.scatter(datatable.index, datatable['max'], color='yellow')
ax.set_xlabel('Flower Class')
ax.set_ylabel('sepal width')
plt.suptitle('Sepal Width',weight='bold')


datatable = datafile.groupby('flower class')['petal width'].agg(['min', 'max'])
fig, ax = plt.subplots(1,1)
ax.scatter(datatable.index, datatable['min'], color='blue')
ax.scatter(datatable.index, datatable['max'], color='yellow')
ax.set_xlabel('Flower Class')
ax.set_ylabel('petal width')
plt.suptitle('Petal Width',weight='bold')
plt.show()
plt.savefig('scatterplot.png')
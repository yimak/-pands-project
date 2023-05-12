pands-project


In this project we will be working on a Fisher's Iris data set. The objective is to make a research on te data set using Python, add the documentation and code to investigate it. The documentation will be summarised in this readme file:

First we will download the data set called iris.data Create a program named analysis.py. The program shouldbe able to:

1. Output a summary of each variable to a single text file,
2. Save a histogram of each variable to png files, and
3. Output a scatter plot of each pair of variables.
4. Perfors any other analysis you think is appropriate
First we created a repository name pands-project that included a readme file, then we added the same repository to our local drive: $ git clone git@github.com:yimak/pands-project.git once we have our repository cloned, add the file iris.data to it and now we can start to work on the project. https://support.atlassian.com/bitbucket-cloud/docs/clone-a-git-repository/

To start this assiggnment I thought first about sorting the data in columns, I assigned a name to each column of values using the library for data manipulation pandas: $ import pandas as pd $ coldata = pd.read_csv('iris_data.csv')

Then I added the pandas attribute column, and assigned each column a name: $ coldata.columns = ['sepal length', 'sepal width', 'petal length', 'petal width','flower class']

Now we have 5 columns and 149 rows: 5 x sepal length, sepal width, petal length, petal width,flower class

First we tried to install Pandas: $ import pandas as pd But it couldn't be installed in VS code and was showing this error import pandas as pd reportMissingModuleSource, as an alternative we opted to putting it this way:

$ pip install pandas Then did the same thing with seaborn (just in case we will need it) $ pip install seaborn https://stackoverflow.com/questions/71617057/import-pandas-could-not-be-resolved-from-source-pylancereportmissingmodulesourc

Now that we have the columns and all the modules installed we can start to work on the data, all the research made will be based on the types of flower class, so lets sort the flower class first using a pandas unique() function:

$ flowers = coldata['flower class'].unique() $ print (flowers) $ ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica'] https://www.sharpsightlabs.com/blog/pandas-unique/

#note tha unique is also a Numpy function, the reason is that Numpy is build on to of Panda, that's why they share mmany build in functions

We assigned each column a name using columns: dataframe.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'flower class'] https://www.geeksforgeeks.org/add-column-names-to-dataframe-in-pandas/

Histogram and Boxplot with each variableNow that we have the three types of flower, we can check the petal length depending on the flower class and then we will create a plot with all the data, for that we will use seaborn. For this case scenario I opted to use histogram and a boxplot, to change the visualisation from Histogram to Boxplot we just needed to change the parts of the code where $histplot was by $boxplot, that's the reason why the references are all related to boxplot:

$ import seaborn as sb $ sb.boxplot(x='flower class', y='sepal width', data=dataframe) https://matplotlib.org/stable/plot_types/stats/boxplot_plot.html#sphx-glr-plot-types-stats-boxplot-plot-pyhttps://www.turing.com/kb/how-to-create-a-boxplot-in-pythonhttps://www.tutorialspoint.com/python-pandas-draw-a-vertical-boxplot-grouped-by-a-categorical-variable-with-seaborn

Then we added a titlle using matplotlib: plt.title('Petal length by Flower species') https://www.scaler.com/topics/matplotlib/matplotlib-title/

We will also add a function to save the image for our project: $ plt.savefig("test.png")

#because the next plots would include the plots before,it's ncessary to include $ plt.clf() right after each plot https://www.activestate.com/resources/quick-reads/how-to-clear-a-plot-in-python/

Then, to give the plot a nice uniform color, I decided to apply seaborn color: $ sns.set_palette('Blues') https://seaborn.pydata.org/tutorial/color_palettes.html

So when I first tried to output this it didn't work, the reason was that we defined seaborn as sb, so I just changed it for sns and changed the other lines to sns as well: $ import seaborn as sns

Scatter Plot Maximum/MinimumI'm aware that the task was about presenting the two variables separately, but I couldn't figure out a way to do it (or better said, I found a way but I couldn't understand it) as an alternative I decided to sort the maximum and minimum of each variable depending on the flower type. I added .agg(['min','max']) right after the columns that includes the numerical data. By that, we will be extracting all the values of each column together and then filtering the maximum and minimum value of each attribute and classing it by the name of the flower type and that by using goupby() function 'flower class'. The result will be assigned to the function datatable: $ datatable = dataframe.groupby('flower class')[['sepal length'].agg(['min', 'max'])

https://sparkbyexamples.com/pandas/pandas-group-dataframe-rows-list-groupby/#:~:text=You%20can%20group%20DataFrame%20rows,the%20list%20for%20every%20group. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.htmlhttps://sparkbyexamples.com/pandas/pandas-groupby-explained-with-examples/

Now we can create the scatter plot that will represent the values. Because we want to create an image later out of our plot we will add fig, fig contains all the plot, thats is ax is part of fig, and ax contains the subplot with our attributes: $ fig, ax = plt.subplot()

Then we will define the rows and columns the subplot ax will contain: $ fig, ax = plt.subplots(rows=1,cols=1)

https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python

Then we provided a title to the plot Flowers types: $ plt.title('Flower Class max/min') However, because we also defined the names of the rows, the title was positioned on the attribute name. It was just by trying other options that I found suptitle, after trying this option the title was positioned on the top of the plot:. $ plt.suptitle('Flower Class max/min', weight='bold')

https://matplotlib.org/stable/gallery/text_labels_and_annotations/titles_demo.htmlhttps://www.statology.org/matplotlib-bold-font/https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html

Now we can define the plot. We want a scatterplot, the reason why we will use the Pandas function scatter(). We used index in order to indicate that we will be sorting data by the index, that is 'flower class' rows (assigned right before through groupby()): $ ax.scatter(datatable.index, datatable['min'], color='blue') $ ax.scatter(datatable.index, datatable['max'], color='yellow')

https://sparkbyexamples.com/pandas/get-row-number-in-pandas/#:~:text=You%20can%20get%20the%20row,can%20use%20the%20len(df. https://sparkbyexamples.com/pandas/pandas-groupby-explained-with-examples/

Then set the labels $ ax.set_xlabel('Flower Class') $ ax.set_ylabel('Petal Length')

Then finally to create and save the plot: $ plt.show() $ plt.savefig("test.png")
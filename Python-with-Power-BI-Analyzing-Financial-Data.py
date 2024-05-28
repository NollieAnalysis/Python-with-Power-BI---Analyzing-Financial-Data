import pandas as pd

import yfinance as yf

ticker = "TSLA"

data = yf.download(ticker, start = "2019-01-01", end = "2022-12-31")

data.reset_index(inplace=True)

data








#The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

#dataset = pandas.DataFrame(Date, Close)

#dataset = dataset.drop_duplicates()

#Paste or type your script code here:

import matplotlib.pyplot as plt

plt.plot(dataset['Date'], dataset['Close'], color = 'blue')

plt.show()






#The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

#dataset = pandas.DataFrame(Date, Close)

#dataset = dataset.drop_duplicates()

#Paste or type your script code here:

import matplotlib.pyplot as plt

plt.fill_between(dataset['Date'], dataset['Close'], color = 'skyblue')

plt.plot(dataset['Date'], dataset['Close'], color = 'blue')

plt.show()






#The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

#dataset = pandas.DataFrame(Close)

#dataset = dataset.drop_duplicates()

#Paste or type your script code here:

import matplotlib.pyplot as plt

import seaborn as sns

sns.boxplot(data=dataset, y='Close')

plt.show()





#The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

#dataset = pandas.DataFrame(Close)

#dataset = dataset.drop_duplicates()

#Paste or type your script code here:

import matplotlib.pyplot as plt

import seaborn as sns

sns.violinplot(data=dataset, y='Close')

plt.show()






#The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

#dataset = pandas.DataFrame(Close)

#dataset = dataset.drop_duplicates()

#Paste or type your script code here:

import matplotlib.pyplot as plt

import seaborn as sns

sns.violinplot(data=dataset, y='Volume')

plt.show()




#The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

#dataset = pandas.DataFrame(Close)

#dataset = dataset.drop_duplicates()

#Paste or type your script code here:

import matplotlib.pyplot as plt

import seaborn as sns

sns.violinplot(data=dataset, x='Year', y='Volume')

plt.show()





#The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

#dataset = pandas.DataFrame(Close)

#dataset = dataset.drop_duplicates()

#Paste or type your script code here:

import matplotlib.pyplot as plt

import seaborn as sns

sns.violinplot(data=dataset, x='Year', y='Volume', hue='Quarter')

plt.show()





#The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

#dataset = pandas.DataFrame(Year, Quarter, Month, Day, Volume)

#dataset = dataset.drop_duplicates()

#Paste or type your script code here:

import matplotlib.pyplot as plt

import seaborn as sns

sns.histplot(data=dataset, x='Volume', hue='Year', kde=True)

plt.show()





#The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

#dataset = pandas.DataFrame(Year, Quarter, Month, Day, Volume)

#dataset = dataset.drop_duplicates()

#Paste or type your script code here:

import matplotlib.pyplot as plt

import seaborn as sns

sns.lineplot(data=dataset, x='Date', y='Close', color='Purple')

plt.show()






#The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

#dataset = pandas.DataFrame(Year, Quarter, Month, Day, Close, Volume)

#dataset = dataset.drop_duplicates()

#Paste or type your script code here:

import matplotlib.pyplot as plt

import seaborn as sns

volume = dataset['Volume']

close = dataset['Close']

date = dataset['Year']

dataset['up_down'] = ['Up' if price > 0 else 'Down' for price in (close-close.shift(1))]

sns.scatterplot(data = dataset, x = date, y = volume, sizes = (20, 200), alpha = 0.7, hue = 'up_down', palette = {'Up': 'green', 'Down': 'red'})

plt.show()






#The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

#dataset = pandas.DataFrame(Year, Quarter, Month, Day, Close, Volume)

#dataset = dataset.drop_duplicates()

#Paste or type your script code here:

import matplotlib.pyplot as plt

import seaborn as sns

volume = dataset['Volume']

close = dataset['Close']

date = dataset['Quarter']

dataset['up_down'] = ['Up' if price > 0 else 'Down' for price in (close-close.shift(1))]

sns.scatterplot(data = dataset, x = date, y = volume, sizes = (20, 200), alpha = 0.7, hue = 'up_down', palette = {'Up': 'green', 'Down': 'red'})

plt.show()







#The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

#dataset = pandas.DataFrame(Year, Quarter, Month, Day, Close, Volume)

#dataset = dataset.drop_duplicates()

#Paste or type your script code here:

import matplotlib.pyplot as plt

import seaborn as sns

volume = dataset['Volume']

close = dataset['Close']

date = dataset['Month']

dataset['up_down'] = ['Up' if price > 0 else 'Down' for price in (close-close.shift(1))]

sns.scatterplot(data = dataset, x = date, y = volume, sizes = (20, 200), alpha = 0.7, hue = 'up_down', palette = {'Up': 'green', 'Down': 'red'})

plt.show()







#The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

#dataset = pandas.DataFrame(Year, Quarter, Month, Day, Close, Volume)

#dataset = dataset.drop_duplicates()

#Paste or type your script code here:

import matplotlib.pyplot as plt

import seaborn as sns

volume = dataset['Volume']

close = dataset['Close']

date = dataset['Day']

dataset['up_down'] = ['Up' if price > 0 else 'Down' for price in (close-close.shift(1))]

sns.scatterplot(data = dataset, x = date, y = volume, sizes = (20, 200), alpha = 0.7, hue = 'up_down', palette = {'Up': 'green', 'Down': 'red'})

plt.show()
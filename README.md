Python with Power BI: Analyzing Financial Data

Coursera guided project practicing python integration into Microsoft BI's platform. Course taught by Abhishek Jha.

Coursera's description of course:
"In this project, we will create a Financial dashboard for assets like stock and crypto.
The dashboard will be dynamic in nature meaning you will be able to get important information 
and graphs about any stock just by replacing the ticker symbol without ever leaving Power BI. 
The project begins with you importing real-time financial data from Yahoo Finance using Python libraries. 
You will harness the power of Python libraries and custom visuals in Power BI to visualize the data, creating 
approximately 10 different charts and graphs to analyze price and volume movement. 
This will be very helpful if you work in Finance or need to present Financial data to clients. 
Currently, financial websites provide limited visualizations. By using Python with Power BI, 
you can present financial data to clients in a far better way than currently available on internet. 
You can add tremendous value by incorporating python with Power BI."

Coursera's description of project objectives:
1. "Import real time financial data into Power BI using python library"
2. "Analyze historical trends by using Line and Area charts"
3. "Visualize Price using Box & Violin charts"
4. "Practice task: Create a line chart using Python Visual in Power BI"
5. "Visualize volume using histogram and violin plots"
6. "Visualize yearly, quarterly, monthly & daily variations using scatter plots"
7. "Challenge: Import the price of Bitcoin using Python in Power Bi & build a line chat  to visualize historical trend"

Python libraries used:
matplotlib.pyplot as plt, seaborn as sns, pandas as pd, yfinance as yf

Python functions used:
plt.plot, plt.show, plt.fill_between, sns.boxplot, sns.violinplot, sns.histoplot, sns.lineplot, sns.scatterplot


Project deliverables:

#Python script to import data into Microsoft BI
import pandas as pd
import yfinance as yf

ticker = "TSLA"

data = yf.download(ticker, start = "2019-01-01", end = "2022-12-31")
data.reset_index(inplace=True)
data

#Page one visulizations and code
![Page_1_Date_and_Close_1](https://github.com/NollieAnalysis/Python-with-Power-BI-Analyzing-Financial-Data/assets/163913188/89302e6d-0949-4ae9-8d4f-35c65f9e1ac5)

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Date, Close)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
plt.plot(dataset['Date'], dataset['Close'], color = 'blue')
plt.show()

![Page_1_Date_and_Close_2](https://github.com/NollieAnalysis/Python-with-Power-BI-Analyzing-Financial-Data/assets/163913188/28aa51ef-caa4-44bb-85fb-02a5f807d64c)

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Date, Close)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
plt.fill_between(dataset['Date'], dataset['Close'], color = 'skyblue')
plt.plot(dataset['Date'], dataset['Close'], color = 'blue')
plt.show()

#Page two visulizations and code
![Page_2_Close_1](https://github.com/NollieAnalysis/Python-with-Power-BI-Analyzing-Financial-Data/assets/163913188/1f2fa614-66c5-479b-a878-4321b15bc74b)

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Close)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import seaborn as sns

sns.boxplot(data=dataset, y='Close')
plt.show()

![Page_2_Close_2](https://github.com/NollieAnalysis/Python-with-Power-BI-Analyzing-Financial-Data/assets/163913188/19bf7f38-782d-41e5-a473-6b5331d02458)

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Close)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import seaborn as sns

sns.violinplot(data=dataset, y='Close')
plt.show()

![Page_2_Volume_Year_Quarter_Etc_1](https://github.com/NollieAnalysis/Python-with-Power-BI-Analyzing-Financial-Data/assets/163913188/5ea007f5-dbf0-4579-bb5f-d8ced755932c)

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Close)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import seaborn as sns

sns.violinplot(data=dataset, y='Volume')
plt.show()

![Page_2_Volume_Year_Quarter_Etc_2](https://github.com/NollieAnalysis/Python-with-Power-BI-Analyzing-Financial-Data/assets/163913188/7bbf5173-7251-4aaf-b458-a95f566aac67)

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Close)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import seaborn as sns

sns.violinplot(data=dataset, x='Year', y='Volume')
plt.show()

![Page_2_Volume_Year_Quarter_Etc_3](https://github.com/NollieAnalysis/Python-with-Power-BI-Analyzing-Financial-Data/assets/163913188/c1bdcdf9-0989-4351-9e61-3e18de46728a)

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Close)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import seaborn as sns

sns.violinplot(data=dataset, x='Year', y='Volume', hue='Quarter')
plt.show()

![Page_2_Year_Quarter_Etc_1](https://github.com/NollieAnalysis/Python-with-Power-BI-Analyzing-Financial-Data/assets/163913188/280f2f9f-9073-473a-b704-92e364472dc8)

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Year, Quarter, Month, Day, Volume)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(data=dataset, x='Volume', hue='Year', kde=True)
plt.show()

![Page_2_Date_and_Close_1](https://github.com/NollieAnalysis/Python-with-Power-BI-Analyzing-Financial-Data/assets/163913188/28ef0a04-35de-4dcb-a6da-f49ccf74b636)

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Year, Quarter, Month, Day, Volume)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(data=dataset, x='Date', y='Close', color='Purple')
plt.show()

#Page three visulizations and code
![Page_3_Year_Quarter_Month_1](https://github.com/NollieAnalysis/Python-with-Power-BI-Analyzing-Financial-Data/assets/163913188/7a887968-8bc4-4cba-ab70-542e79fee087)

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Year, Quarter, Month, Day, Close, Volume)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import seaborn as sns

volume = dataset['Volume']
close = dataset['Close']
date = dataset['Year']

dataset['up_down'] = ['Up' if price > 0 else 'Down' for price in (close-close.shift(1))]

sns.scatterplot(data = dataset, x = date, y = volume, sizes = (20, 200), alpha = 0.7, hue = 'up_down', palette = {'Up': 'green', 'Down': 'red'})

plt.show()

![Page_3_Year_Quarter_Month_2](https://github.com/NollieAnalysis/Python-with-Power-BI-Analyzing-Financial-Data/assets/163913188/8f504cd8-f3eb-4a16-9e92-dbcb6fc42ea6)

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Year, Quarter, Month, Day, Close, Volume)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import seaborn as sns

volume = dataset['Volume']
close = dataset['Close']
date = dataset['Quarter']

dataset['up_down'] = ['Up' if price > 0 else 'Down' for price in (close-close.shift(1))]

sns.scatterplot(data = dataset, x = date, y = volume, sizes = (20, 200), alpha = 0.7, hue = 'up_down', palette = {'Up': 'green', 'Down': 'red'})

plt.show()

![Page_3_Year_Quarter_Month_3](https://github.com/NollieAnalysis/Python-with-Power-BI-Analyzing-Financial-Data/assets/163913188/e6063b32-01ba-4075-aec2-23f6524ba758)

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Year, Quarter, Month, Day, Close, Volume)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import seaborn as sns

volume = dataset['Volume']
close = dataset['Close']
date = dataset['Month']

dataset['up_down'] = ['Up' if price > 0 else 'Down' for price in (close-close.shift(1))]

sns.scatterplot(data = dataset, x = date, y = volume, sizes = (20, 200), alpha = 0.7, hue = 'up_down', palette = {'Up': 'green', 'Down': 'red'})

plt.show()

![Page_3_Year_Quarter_Month_4](https://github.com/NollieAnalysis/Python-with-Power-BI-Analyzing-Financial-Data/assets/163913188/7d677604-27e0-4b88-9fb0-6fd785db57d1)

# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Year, Quarter, Month, Day, Close, Volume)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import seaborn as sns

volume = dataset['Volume']
close = dataset['Close']
date = dataset['Day']

dataset['up_down'] = ['Up' if price > 0 else 'Down' for price in (close-close.shift(1))]

sns.scatterplot(data = dataset, x = date, y = volume, sizes = (20, 200), alpha = 0.7, hue = 'up_down', palette = {'Up': 'green', 'Down': 'red'})

plt.show()

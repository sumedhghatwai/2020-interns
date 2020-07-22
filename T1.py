import json
from dateutil import parser
import matplotlib.pyplot as plt 

with open('data.json') as f:
    data = json.load(f)

date1=parser.parse('2019-01-01')
date2=parser.parse('2019-01-31')

dates=[]
prices=[]

for i in data['rates']:
    date = parser.parse(i)
    if date >= date1 and date <= date2:
        dates.append(i)
        prices.append(data['rates'][i]['INR'])

final=sorted(list(zip(dates,prices)))

dates,prices = zip(*final)
dates=list(dates)
prices=list(prices)

plt.plot(dates,prices)
plt.title('Exchange rate against EUR')
plt.xlabel('Dates between Jan 1st 2019 and Jan 31st 2019')
plt.xticks(rotation=90)
plt.ylabel('Rates in INR')
plt.show()
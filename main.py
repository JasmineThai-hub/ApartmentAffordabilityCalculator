from myApartmentFuncs import *
from ApartmentClass import *
import matplotlib.pyplot as plt
import pandas as pd

present = date.today()

renter = getRenterInfo()

firstMonthAmt, payDate, week = brokeCheck(renter)

yearReceipt = yearSimulator(renter,payDate, week)

data = {'date': yearReceipt.keys(),
        'balance': yearReceipt.values()}
new = pd.DataFrame.from_dict(data)

df = pd.DataFrame(new, columns=['date', 'balance'])

plt.plot(df['date'], df['balance'], color='red', marker='o')
plt.title('balance Vs date', fontsize=14)
plt.xlabel('date', fontsize=14)
plt.ylabel('balance', fontsize=14)
plt.grid(True)
plt.show()
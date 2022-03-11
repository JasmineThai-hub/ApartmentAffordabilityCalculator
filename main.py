from myApartmentFuncs import *
from ApartmentClass import *

present = date.today()

renter = getRenterInfo()

firstMonthAmt, payDate, week = brokeCheck(renter)

yearReceipt = yearSimulator(renter,payDate, week)

print(yearReceipt)



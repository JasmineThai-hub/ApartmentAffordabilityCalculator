from myApartmentFuncs import *

renter = getRenterInfo()

firstMonthAmt, payDate, week, yearReceipt = brokeCheck(renter)

yearReceipt = yearSimulator(renter, payDate, week, yearReceipt)

getStats(renter)

getHisto(yearReceipt)


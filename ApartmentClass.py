from datetime import date
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Renter:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.payFull = 0
        self.payPart = 0

    def setLoss(self):
        self.bills = int(input("How much do you pay in bills currently each month?\n"))
        self.fun = int(input("How much do you usually spend for fun?\n"))
        self.food = int(input("How much do you spend on food?\n"))
        self.rent = int(input("How much would rent be after the first month?\n"))
        self.loss = [self.bills, self.fun, self.food, self.rent]
        self.lossFirstMonth = [self.bills, self.food, self.fun]

    def getLoss(self):
        return sum(self.loss)

    def loseMoney(self, firstMonth):
        if firstMonth == True:
            print(f"-{sum(self.lossFirstMonth)}")
            self.balance -= sum(self.lossFirstMonth)
        else:
            print(f"-{sum(self.loss)}")
            self.balance -= sum(self.loss)

    def loseFirstMonth(self, firstMont):
        self.balance -= firstMont

    def setFullTimepay(self):
        self.payFull = int(input("How much do you make full-time bi-weekly?\n"))

    def setPartTimepay(self):
        self.payPart = int(input("How much do you make part-time bi-weekly?\n"))

    def getMoney(self, payDate):
        fullTimeDate = [date(payDate.year, 5, 20), date(payDate.year, 8, 8)]
        if fullTimeDate[0] < payDate < fullTimeDate[1]:
            self.balance += self.payFull
            print(f"+{self.payFull}")

        else:
            self.balance += self.payPart
            print(f"+{self.payPart}")









from ApartmentClass import *

def getDate(payDate):
    new = payDate.split('/')
    d = [int(x) for x in new]  # turn the given string data to ints
    # year, month, day
    dt = date(d[2], d[0], d[1])  # turn the date ints to a single date data type from datetime
    return dt

def getRenterInfo():
    name = input("What name will you put?\n")
    balance = int(input("How much do you have in your bank account right now?\n"))
    renter = Renter(name, balance)

    renter.setPartTimepay()
    renter.setFullTimepay()
    renter.setLoss()

    print(f'{renter.name}: {renter.balance}')

    return renter

def brokeCheck(renter):
    firstMonth = int(input("How much would the first month of moving out cost?(no furniture)\n"))
    furniture = int(input("How much would furniture/necessities cost?\n"))

    firstMonthAmt = firstMonth + furniture

    check = renter.balance - firstMonthAmt
    broke = check < 0

    if broke == True:
        print(f"You have a deficit of: ${check}")
        print("You cannot afford to move out currently, let's see when you can\n")
    if broke == False:
        print(f"You have a surplus of: ${check}")
        print("Congrats! You can afford to move out!\n")
    payDate, week, yearReceipt = BiweeklySimulate(renter, firstMonthAmt)

    return firstMonthAmt, payDate, week, yearReceipt

def BiweeklySimulate(renter, firstMonthAmt):
  print("~"*25, "SAVING UP FOR YOUR FIRST MONTH", "~"*25)
  yearReceipt = {}
  week = 1
  payDate = getDate(input("When did you last get paid?\n"))
  next = timedelta(7)
  while renter.balance <= (firstMonthAmt):
    payDate += next
    if week % 2 == 0:
      print(f"{payDate}:")
      renter.getMoneyStud(payDate)
      if week % 4 == 0:
        renter.loseMoney(True)
        print(f"Month balance: {renter.balance}")
        yearReceipt[str(payDate.month) + "/" + str(payDate.year)[2::]] = renter.balance

    week += 1
  print(f"At the current expenditures, I calculated that in {week} weeks, you will break even with the first month's costs with a surplus of:")
  print(f"${renter.balance - firstMonthAmt}\n")
  if renter.balance < sum(renter.loss)+firstMonthAmt:
    print(f"Which means you should wait two weeks (a paycheck) after {week} weeks to move out! Just to be on the safe side\n")
  else:
    print("Awesome! You're set for next month as well!\n")
  return payDate, week, yearReceipt

def yearSimulator(renter, payDate, week, yearReceipt):
  print("~" * 25, "A RECEIPT OF YOUR YEAR OF HAVING MOVED OUT", "~" * 25)
  next = timedelta(7)
  year = int(input("What year did you want to run the simulation to?\n"))
  grad = getDate(input("When do you graduate?\n"))
  renter.setSalary()
  while payDate < (date(year, 5, 24)):
    payDate += next
    if week % 2 == 0:
      print(f"{payDate}:")
      if payDate >= grad:
        renter.getMoneyFull()
      else:
        renter.getMoneyStud(payDate)
      if week % 4 == 0:
        renter.loseMoney(False)
        print(f"Month balance: {renter.balance}")
        yearReceipt[str(payDate.month)+"/"+str(payDate.year)[2::]] = renter.balance
    week += 1
  return yearReceipt

def getHisto(yearReceipt):
    data = {'date': yearReceipt.keys(),
            'balance': yearReceipt.values()}
    new = pd.DataFrame.from_dict(data)

    df = pd.DataFrame(new, columns=['date', 'balance'])

    x = df['date']
    y = df['balance']

    plt.plot(x, y, color='red', marker='o')
    plt.title('balance Vs date', fontsize=14)
    plt.xlabel('date', fontsize=14)
    plt.ylabel('balance', fontsize=14)
    plt.grid(True)
    plt.show()
    return df

def getStats(renter):
    print("~"*25,"RENTER STATS","~"*25)
    d = {
        'Pay per paycheck (bi-weekly)':['-'],
        'Part-Time': [renter.payPart],
        'Full-Time': [renter.payFull],
        'Salary': [renter.salary]
    }
    pay_df = pd.DataFrame(d)
    print(pay_df)

    losses = {
        'losses': ['Bills', 'Fun', 'Food', 'Rent'],
        'amounts' : renter.loss,
    }
    loss_df = pd.DataFrame(losses)
    print('\n', loss_df)
    print(f"Total: {sum(renter.loss)}")

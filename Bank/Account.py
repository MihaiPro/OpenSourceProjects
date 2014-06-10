class Account(object):
  """ Allow to user to have a personal account 
  and keep their money here, to buy , sell and borrow
  proprieties -> dictionary with name of propriety and its value
  ststus -> allowed, banned, waiting(must be accepted by admin im max 3 days)"""
  
  money = 0
  total_debt = 0
  pay_per_month = 0
  months = 0
  proprieties = {
    "cash":0
    }
  income = 0
  taxes = 0

  def __init__(self, username, password, credit_card, status):
    self.username = username
    self.password = password
    self.credit_card = credit_card
    self.status = status
    
  def buy(self, item, value):
    #add an item to proprieties and pay for it
    pass
  
  def sell(self, item):
    #sell an item from proprieties
    pass
  
  def pay_tax(self):
    #pay monthly taxes
    pass
  
  def withdraw_money(self, amount):
    #withdraw an amount of money from account
    pass
  
  def deposit_money(self, amount):
    #deposit an amount of money in bank
    pass
    
  def borrow(self, amount, guarantee):
    #borrow money, but user must have a guarantee(proprieties)
    pass

#here accounts will be made
Mihai=Account("Mihai","TEST","","waiting")
Mihai.money=1000
Mihai.income=300
Mihai.proprieties["cash"]=500
Alex=Account("Alex","1234","","waiting)"
Alex.money=1000
Alex.income=3000
Alex.proprieties["cash"]=6000

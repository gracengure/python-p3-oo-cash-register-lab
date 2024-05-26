#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0,items=None):
    self.total = 0
    self.discount = discount
    self.last_transaction = 0
    if items is None:
      self.items = []
    else:
      self.items = items
  pass
 
  def add_item(self,title,price,quantity = 1):
    self.items = [*self.items,*([title]*quantity)]
    price *= quantity
    self.last_transaction = price
    self.total += price
    pass

  def apply_discount(self):
    if self.discount != 0:  
      self.total -= (self.total*self.discount)/100
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")  
    pass

  def void_last_transaction(self):
    self.total -= self.last_transaction    

# new_register = CashRegister()
# new_register.add_item("eggs", 1.99, 2)
# new_register.add_item("tomato", 1.76, 3)
# print(new_register.items)
  pass

import threading
import time
from multiprocessing import Process 

class BankAccount():
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
 
  def __str__(self):
    return self.name
 
# These accounts are our shared resources
account1 = BankAccount("account1", 100)
account2 = BankAccount("account2", 0)
 
class BankTransferProcess(Process):
  def __init__(self, sender, receiver, amount):
    Process.__init__(self)
    self.sender = sender
    self.receiver = receiver
    self.amount = amount
   
  def run(self):
    sender_initial_balance = self.sender.balance
    sender_initial_balance -= self.amount
    # Inserting delay to allow switch between threads
    time.sleep(0.001)
    self.sender.balance = sender_initial_balance
     
    receiver_initial_balance = self.receiver.balance
    receiver_initial_balance += self.amount
    # Inserting delay to allow switch between threads
    time.sleep(0.001)
    self.receiver.balance = receiver_initial_balance
 
if __name__ == "__main__":
   
  processes = []
 
  for i in range(100):
    processes.append(BankTransferProcess(account1, account2, 1))
 
  for process in processes:
    process.start()
    
  for process in processes:
    process.join()
    
  print(account1.balance)
  print(account2.balance)
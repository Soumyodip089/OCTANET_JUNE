print ("Welcome to XYZ Bank \n\nInsert your card")
password= 1234
balance = 50000
choice = 0 
pin=int(input("Enter your four digit pin\n"))
transactions = []
if pin==password:
  while choice != 5:
    print("\n\n***** Menu *****")
    print("1 == balance")
    print("2 == deposit")
    print("3 == Withdrawl")
    print("4 == Transfer")  
    print("5 == Cancel\n")

    choice=int(input("\nEnter your option:\n"))

    if choice == 1:
      print ("Balance ", balance)
    elif choice == 2:
      dep=int(input("Enter your deposit"))
      balance += dep
      print ("\nDeposited amount" , dep)
      print ("Balance" , balance)
      transactions.append(("Deposit", dep)) 
    elif  choice == 3:
      wit=int(input("Enter the amount to withdraw"))
      balance -= wit
      print ("\nWithdrawl Amount" , wit)
      print ("Balance" , balance)
      transactions.append(("Withdrawal", wit)) 
    elif choice == 4:  
            amount = int(input("Enter the amount to transfer: "))
            if amount <= balance:
                receiver_account = input("Enter the receiver's account number: ")
                print(f"\nTransferred {amount} to account {receiver_account}")
                balance -= amount
                transactions.append(("Transfer", -amount))  
            else:
                print("Insufficient funds for transfer!")
    elif choice == 5:
            print("\nTransaction Ended!! Have a Good Day")
            
    else:
      print ("\n Invalid Entry!!")   
else:
 print("pin incorrent! try again")

print("\nTransaction History:")
for index, (transaction_type, amount) in enumerate(transactions, start=1):
    print(f"{index}. {transaction_type}: {amount}")
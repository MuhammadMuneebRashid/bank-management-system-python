# Import os module
import os
# Function of creating new bank account
def create_acc():
    name=input("enter the account holder name:")
    with open("account.txt","a") as f:
        f.write(name+",0\n")
        print("Account is created successfully")
# Function of Depositing money into an account
def deposit() :
    name=input("enter the name:")       
    amount=int(input("enter the amount:"))
    update=False
    accounts=[]
    with open("account.txt","r") as f:
        for records in f:
           acc_name,balance=records.strip().split(",")
           balance=int(balance)
           if acc_name==name:
            balance+=amount
            update=True
           accounts.append(f"{acc_name},{balance}\n")
    if update:
       with open("account.txt","w") as f:
          f.writelines(accounts)
          print("Amount is deposit successfully !")
    else:
       print("Account not found")
# Function of Withdraw money from an account
def withdraw():
   name=input("Enter the name:")
   amount=int(input("Enter the amount:"))
   update=False
   accounts=[]
   with open("account.txt","r") as f:
      for records in f:
         acc_name,balance=records.strip().split(",")
         balance=int(balance)
         if acc_name==name:
            balance-=amount
            update=True
         accounts.append(f"{acc_name},{balance}\n")
   if update:
         with open ("account.txt","w") as f:
            f.writelines(accounts)
            print("Amount is withdrawl successfully")
   else:
         print("Insufficient amount")
# Function of Check account balance
def check_balance():
   name=input("Enter the name:")
   found=False
   with open ("account.txt" , "r") as f:
      for records in f:
         acc_name,balance= records.strip().split(",")
         if acc_name==name:
            print(f"Current balance:, {balance}")
            found=True
            break
   if not found:
            print("Account not found")
# Function of View all accounts
def view_accounts():
   print("\n All Accounts")
   with open("account.txt","r") as f:
      for records in f:
         acc_name,amount=records.strip().split(",")
         print(f"Name:{acc_name},Balance:{amount}")    
if not os.path.exists("account.txt"):
   open("account.txt","w").close()  
# Main Menu
while True:
   print("===Bank Mnanagement System ===")
   print("1. Create Account")
   print("2. Deposit")
   print("3. Withdrawl")
   print("4. Check Balance")    
   print("5. View Accounts")
   print("6. Exit")
   # Take input from user
   choice=int(input("Enter the choice:"))
   # Create new account
   if (choice==1):
      create_acc()
   # Deposit money
   elif(choice==2):
      deposit()
   # Withdraw money
   elif(choice==3):
      withdraw()
   # Check account balance
   elif(choice==4):
      check_balance()
   # View all accounts
   elif(choice==5):
      view_accounts()
   # Exit the program
   elif(choice==6):
      print("Good Bye!")
      break
   # Handles the invalid input
   else:
      print("Invalid choice")

      

          
           
              

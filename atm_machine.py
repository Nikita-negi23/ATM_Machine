import sqlite3
import os



def create_table():
    database_file_name = 'ATM_DETAILS.db'
    con = sqlite3.connect(database_file_name)
    print("Connection Created")
    create_table_sql = '''
                       CREATE TABLE account_details(
                       user_name char(1000),
                       card_num  int,
                       pin int, 
                       amount int )
                       '''
    con.execute(create_table_sql)
    print("table account_details is created")

create_table()

"""
    
def cash_withdrawal():
    print("You can withdraw maximum 10,000 at a time")
    amount = int(input("Enter amount in the multiple of 1000 : "))
    if(amount % 1000 == 0 and amount <= 10000):
        print("Please collect your money")
    elif(amount > 10000):
        print("Process Interrupted as the entered amount is more than 10000")
    else:
        print("Process Interrupted as the entered amount is not the multiple of 1000")
        exit()
        
def balance_enquiry():
    show = 4000
    print("Your Available balance is : ",show)
    
def pin_change():
    new_pin = int(input("Enter your new pin : "))
    change = '''
             Your PIN is Successfully changed.
             Your New PIN is : "
             '''
    print(change,new_pin)




def start_atm_service():
    option = '''
             1) Cash Withdrawal
             2) Balance Enquiry
             3) ATM PIN Change
             4) Exit
             
             *Select one option( 1 / 2 / 3 / 4 )
             '''
    selected_option = int(input(option))
    if(selected_option == 1):
        cash_withdrawal()
    elif(selected_option == 2):
        balance_enquiry()
    elif(selected_option == 3):
        pin_change()
    else:
        print("Process interuppted")
        exit()
        
    

home_page = '''
WELCOME TO SBI ATM
ENTER YOUR ATM CARD NUMBER
'''
print(home_page)

#card_num = int(input())
card_num = 2222 ########
pin = 1111 ###########
#pin = int(input("Enter your PIN number - "))

# Proceed further if it a valid user.
if(pin == 1111 and card_num == 2222):
    print("Valid user")
    start_atm_service()
else:
    print("You have entered wrong ATM PIN or CARD NUMBER")

"""


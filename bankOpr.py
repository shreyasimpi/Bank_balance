import sys
def BankOper(initial_bal, deposit, withdraw):
    calculatTotal = initial_bal + deposit
    Total_amount = calculatTotal - withdraw

if __name__ == "__main__":
    initial_bal = int(sys.argv[1])
    deposit = int(sys.argv[2])
    withdraw = int(sys.argv[3])
print(BankOper())

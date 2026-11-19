import sys
def BankOper(initial_bal, deposit, withdraw):
    calculatTotal = initial_bal + deposit
    Total_amount = calculatTotal - withdraw
    return calculateTotal, Total_amount
if __name__ == "__main__":
    initial_bal = int(sys.argv[1])
    deposit = int(sys.argv[2])
    withdraw = int(sys.argv[3])

calculateTotal, Total_amount = BankOper(initial_bal, deposit, withdraw)
print(BankOper())

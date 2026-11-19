
from bankOpr import BankOper
def test_deposit():
    calculateTotal, Total_amount = BankOper(20000, 0, 2000)
    assert calculateTotal == 20000
    assert Total_amount == 18000
def test_withdraw():
    calculateTotal, Total_amount = BankOper(23000, 2000, 3000)
    assert calculateTotal == 25000
    assert Total_amount == 22000
def test_anyamount():
    calculateTotal, Total_amount = BankOper(50000, 0, 2000)
    assert calculateTotal == 50000
    assert Total_amount == 48000

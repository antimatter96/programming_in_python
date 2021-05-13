tim_bank_balance = 100000
# bank_balance is the amount in the savings account

tim_loan_amount = 20000
# loan_amount is the money owed by ram

bill_bank_balance = 500000
bill_loan_amount = 200000

net_bank_balance = tim_bank_balance + bill_bank_balance
# total bank balance of the family

net_liability = tim_loan_amount + bill_loan_amount
# total money owed

net_amount = net_bank_balance - net_liability
# final amount of money with the family
print(net_amount)

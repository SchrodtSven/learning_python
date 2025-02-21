import account
account_movements = [100, 233, -93, 24, 500, -100, -55.02]
accounts = [
    BankAccount('Peter Parker', 2300),
    PrimeAccount('Clint Barton',2300),
    SavingsAccount('Uncle Scrooge', 2300), 
    WasteFulAccount('Donald Duck', 2300)
]        
for acc in accounts:
    acc.set_debug(False)
    print(acc.owner, ' actions:')
    for action in account_movements:
        if(action > 0):
            acc.deposit(action)
            print('Balance:', acc.get_balance())
        else:   
            try:
                acc.withdraw(action)
            except LookupError as e:
                print(e)
            print('Balance:', acc.get_balance())
    
save = SavingsAccount('Duffy Duck', 123)  
inter_save = save.calc_interest(366)
print(inter_save)
try:
    save.withdraw(102.78)
except LookupError as e:
    print(e)

save.unblock_account()
try:
    save.withdraw(102.78)
    save.get_balance()
    print(save)
    save.apply_interest(125)
    print(save)
except LookupError as e:
    print(e)
  
  
# 
# inter_prime = prime.calc_interest(366)
# inter_norm = norm.calc_interest(366)
# inter_waste = waste.calc_interest(366)
# print('prime:', inter_prime) 
# print('savings', inter_save) 
# print('normal', inter_norm) 
# print('wasr', inter_waste)


# print('Lory foo Bar'.find('Helge'))
# print('Lory foo Bar'.find('foo'))
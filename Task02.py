class BankAccount:  #всегда имя существительное ВСЕГДА  и всегд апишется с большой буквы
# constructor
    def __init__(self):
        print(f"constructor from BankAccount{self}")
#destructor
    def __del__(self):
        print(f"destructor from BankAccount{self}")

account1 = BankAccount()
print(account1)
# --> BankAccount.__init__(account1)

# account1.name = "12345"
# account1.balance = 1_000_000

account2 = BankAccount()
print(account2)
# --> BankAccount.__init__(account2)
# account2.name = "6789"
# account2.balance = 1_000

account3 = account2

# print(account3 == account2) #--> True тк ссылаются на один и тот же обьект
# print(account1 == account2) #--> False


# class BankAccount():
#     pass
#
# class BankAccount(object):
#     pass